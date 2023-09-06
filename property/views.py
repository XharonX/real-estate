from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib import messages
from .models import *
from .forms import *
from django.forms import inlineformset_factory
# Create your views here.


class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'property/create_edit_property.html'
    NearbyInlineFormset = inlineformset_factory(Property, Nearby, fields='__all__', can_delete=False)
    ServiceInlineFormset = inlineformset_factory(Property, Service, fields='__all__', can_delete=False)
    ImageInlineFormset = inlineformset_factory(Property, Image, fields='__all__', can_delete_extra=True, can_delete=False)

    def get_named_formsets(self):
        if self.request.method == "GET":
            named = {
                'services': ServiceInlineForm(prefix='services'),
                'nearby': NearbyInlineForm(prefix='nearby'),
                'images': ImageInlineForm(prefix='images'),
            }
            print(named)
            return named
        else:
            return {
                'services': ServiceInlineForm(self.request.POST or None, self.request.FILES or None, prefix='services'),
                'nearby': ServiceInlineForm(self.request.POST or None, self.request.FILES or None, prefix='nearby'),
                'images': ServiceInlineForm(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['named_formsets'] = self.get_named_formsets()
        context['img_formset'] = self.ImageInlineFormset()
        context['service_formset'] = self.ServiceInlineFormset()
        context['nearby_formset'] = self.NearbyInlineFormset()
        return context

    def formset_images_valid(self, formset):
        images = formset.save(commit=False)

        # add this 2 lines, if you have can_delete=True
        # for obj in formset.deleted_objects:
        #     obj.delete()

        for obj in formset.deleted_objects:
            obj.delete()
        for img in images:
            img.property = self.object
            img.save()

    def formset_services_valid(self, formset):
        services = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for service in services:
            service.property = self.object
            service.save()

    def formset_nearby_valid(self, formset):
        buildings = formset.save(commit=False)

        # add this 2 lines, if you have can_delete=True
        # for obj in formset.deleted_objects:
        #     obj.delete()

        for building in buildings:
            building.property = self.object
            building.save()

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            messages.add_message(self.request, messages.ERROR, "Form or Formset was invalid.")
            return self.render_to_response(self.get_context_data(form=form))
        self.object = form.save()
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            print(formset_save_func)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        messages.add_message(self.request, messages.SUCCESS, "Property has been created")
        return redirect('property-list')


class PropertyListView(ListView):
    model = Property
    template_name = 'property/post_list.html'
    context_object_name = 'object_list'


class PropertyDetailView(DetailView):
    model = Property
