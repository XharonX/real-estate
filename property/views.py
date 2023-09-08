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
                'services': ServiceInlineFormset(prefix='services'),
                'nearby': NearbyInlineFormset(prefix='nearby'),
                'images': ImageInlineFormset(prefix='images'),
            }
            print(named.keys())
            return named
        else:
            return {
                'services': ServiceInlineFormset(self.request.POST, self.request.FILES, prefix='services'),
                'nearby': NearbyInlineFormset(self.request.POST, self.request.FILES, prefix='nearby'),
                'images': ImageInlineFormset(self.request.POST, self.request.FILES or None, prefix='images'),
            }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['named_formsets'] = self.get_named_formsets()
        # context['img_formset'] = ImageInlineFormset()
        # context['service_formset'] = ServiceInlineFormset()
        # context['nearby_formset'] = NearbyInlineFormset()
        return context

    def formset_images_valid(self, formset):
        images = formset.save(commit=False)

        # add this 2 lines, if you have can_delete=True
        # for obj in formset.deleted_objects:
        #     obj.delete()

        for img in images:
            img.property = self.object
            img.save()

    def formset_services_valid(self, formset):
        services = formset.save(commit=False)

        for service in services:
            print(service)
            service.property = self.object
            service.save()

    def formset_nearby_valid(self, formset):
        buildings = formset.save(commit=False)

        print('formset_nearby_valid is valid')

        # add this 2 lines, if you have can_delete=True
        # for obj in formset.deleted_objects:
        #     obj.delete()

        for nearby in buildings:
            print(nearby)
            nearby.property = self.object
            nearby.save()
            print('YES saved')

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            messages.add_message(self.request, messages.ERROR, "Form or Formset was invalid.")
            return self.render_to_response(self.get_context_data(form=form))
        self.object = form.save()

        for name, formset in named_formsets.items():
            print(f"{name}: {formset}")
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            print(formset_save_func)
            import os
            if os.path.exists("pretest.html"):
                os.remove("pretest.html")
            with open("pretest.html", "w") as f:
                f.write(str(formset))
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
    template_name = 'property/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        images = self.object.image_set.all()
        feature_services = ['lift', 'water_supply', 'garden', 'play_ground', 'power_backup', 'security_guard']
        near_buildings = ['school', 'hospital', 'market', 'mall', 'gym', 'parking']
        print(self.object.service.__dict__)

        context['services'] = self.get_feature_dict('service', feature_services)
        context['nearby_buildings'] = self.get_feature_dict('nearby', near_buildings)
        context['images'] = images
        return context

    def get_feature_dict(self, feature_property: str, features: list):
        f = list()
        obj = getattr(self.object, feature_property)
        for feature in features:
            f.append({
                'label': feature.replace('_', ' '),
                'is_active': getattr(obj, feature),
            })
        return f
