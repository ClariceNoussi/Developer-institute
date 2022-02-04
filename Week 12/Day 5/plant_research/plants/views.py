from json import JSONDecodeError

from django.contrib import messages
from django.http import HttpResponse

from .forms import AddPlantForm
from .models import Plants, Family, EconomicComments
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
import requests
import json
from .models import Plants
import requests


# Create your views here.
# generic ListView : do a query all in the model specified
class PlantIndex(generic.ListView):
    template_name = 'plant.html'
    model = Plants  # it's like executing the command Animals.objects.all()


# generic CreateView : create a new instance of the model with data
# coming from the form and save it
class AddPlants(generic.CreateView):
    template_name = 'add_plant.html'  # the template to render
    form_class = AddPlantForm  # AddAnimalForm we created earlier in forms.py

    def form_valid(self, form):  # will check if our form is valid and save the data
        post_to_add = form.cleaned_data
        print(post_to_add)
        return super().form_valid(form)

    # Create your views here.


def plantes(request):
    all_plants = Plants.objects.all()  # query to get all the animals instances in my Animals table
    if request.method == 'POST':  # necessary to get data from the user
        # We are inside the post http method
        print('in_post')
        # we fetch the user search with the value of the input's attribute name (animal-search)
        search_result = request.POST.get('plant-search')
        print(search_result)
        # we filter animals instances that corresponds to the user search text
        plant_searched = Plants.objects.filter(name__contains=search_result.title())
        return render(request, 'plant.html', {'plants': plant_searched,
                                             'search': search_result})
    return render(request, 'plants.html', {'plants':
                                               all_plants})


def family(request, id):
    family_object = Family.objects.filter(id).first()  # method first() is used to get the first match in the queryset, since filter return a queryset (a list)
    print(family_object)
    plant_in_family = Plants.objects.filter(family_id=id)
    return render(request, 'home.html', {'plants': plant_in_family,
                                         'family': family_object})


def plant(request, plant_id):
    plant = get_object_or_404(Plants, pk=plant_id)
    context = {
        'plant': plant
    }
    return render(request, 'plant.html', context)


def add_plant(request):
    if request.method == 'POST':
        print('in post')
        add_form = AddPlantForm(request.POST, request.FILES)
        if add_form.is_valid():
            print('in valid')
            new_plant = add_form.save()  # we can use the save method directly on the form because it comes from modelForm and it creates a new animal instance
            messages.success(request, f'New plant {new_plant.name} saved')
            return redirect('home')
    else:
        add_form = AddPlantForm()
        return render(request, 'add_plant.html', {'form_a': add_form})


# SEARCH METHOD
def search(request):
    queryset_list = Plants.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # name
    if 'scientificName' in request.GET:
        name = request.GET['scienficName']
        if name:
            queryset_list = queryset_list.filter(city__iexact=name)

    # Synonyms
    if 'commonName' in request.GET:
        synonyms = request.GET['commonName']
        if synonyms:
            queryset_list = queryset_list.filter(synonyms__iexact=synonyms)

            # Bedroom
    if 'family' in request.GET:
        family = request.GET['family']
        if family:
            queryset_list = queryset_list.filter(family__lte=family)

            # Bedroom
    if 'molecules' in request.GET:
        molecules = request.GET['molecules']
        if molecules:
            queryset_list = queryset_list.filter(molecules__lte=molecules)

            #diseases
    if 'economicComments' in request.GET:
        diseases = request.GET['economicComments']
        if diseases:
            queryset_list = queryset_list.filter(diseases__lte=diseases)

    context = {
        'scentificName_choices': scientificName,
        'commonName_choices': commonName,
        'economicComments_choices': economicComments,
        'plants': plants,
        'values': request.GET
    }
    return render(request, 'search.html', context)


def api(request):
    i = 150016
    while i < 150100:
        try:
            d = requests.get(f'https://explorer.natureserve.org/api/data/taxon/ELEMENT_GLOBAL.2.{i}')
            print(i)
            data = d.json()
        except:
            print('oops error with this seqId')
            continue
        else:
            new_fam = Family.objects.create(name=data['speciesGlobal']['family'])
            print(data['scientificName'])
            if data['plantCharacteristics']['economicComments'] :
                new_economiccomments = EconomicComments.objects.create(name= data['plantCharacteristics']['economicComments'] )
            else:
                new_disease ='Unknown for the moment'
            if data['speciesCharacteristics']['generalDescription'] and data['primaryCommonName']:
                new_plant = Plants(name= data['scientificName'],
                               primarycommonname=data['primaryCommonName'],
                            generaldescription= data['speciesCharacteristics']['generalDescription'],
                               family=new_fam,
                               )
                new_plant.save()
                new_plant.economicComments.set(new_economicComments)
            print(data['formattedScientificName'])
            print('---------------------------------------------------------------')
        finally:
            i += 1

    print('done')
    return HttpResponse(request, 'plants added')