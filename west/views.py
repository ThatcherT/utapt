
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from west.forms import SearchForm
# Create your views here.
from django.template import loader
from .models import Apartment, Review
from django.db.models import Q
from.filters import ApartmentFilter
class IndexView(generic.ListView):
    template_name = 'west/index.html'
    context_object_name = 'apartment_list'
    print(context_object_name)

    #We’re using two generic views here: ListView and DetailView. Respectively, those two views abstract the concepts of
    # “display a list of objects” and “display a detail page for a particular type of object.”
    def get_queryset(self):
        """Return list of apartments"""
        # apartment_list = Apartment.objects.filter(author=)
        # # object_list = City.objects.filter(Q()

        return Apartment.objects.all()
class DetailView(generic.DetailView):
    model = Apartment
    template_name = 'west/detail.html'

def search(request):
    apartment_list = Apartment.objects.all()
    # myFilter = ApartmentFilter(request.GET, queryset=apartment_list)
    # apartment_list = myFilter.qs


    # if request.method == "POST":
    #     searchform = SearchForm(request.POST)
    #     if searchform.is_valid():
    #         area = SearchForm.cleaned_data['area']
    #         print(area)
    West = request.GET.get('west')
    North = request.GET.get('north')
    Riverside = request.GET.get('riverside')
    Name = request.GET.get('name')

    if Name != None:

        apartment_list = apartment_list.filter(name__icontains=Name)
    if West or North or Riverside != None:
        if West == None:

            apartment_list = apartment_list.exclude(area='W')


        if North == None:

            apartment_list = apartment_list.exclude(area='N')

        if Riverside == None:

            apartment_list = apartment_list.exclude(area='R')
    sortprice = request.GET.get('sortprice')
    if sortprice == 'LOW':
        apartment_list = apartment_list.order_by('price')
    if sortprice == 'HIGH':
        apartment_list = apartment_list.order_by('-price')
    quantityl = request.GET.get('quantitylow')
    quantityh = request.GET.get('quantityhigh')


    if  quantityh != "":
            if  quantityl == "":
                quantityl = 0
                quantityh = int(quantityh)
                quantityh += 1
                print('yay')
                apartment_list = apartment_list.filter(price__lt=quantityh, price__gt=quantityl)


    context = {'apartment_list': apartment_list
        # , 'myFilter': myFilter
               }

    return render(request,'west/search.html', context)

# class DetailView(generic.DetailView):


class ReviewsView(generic.DetailView):
    model = Apartment
    template_name = 'west/reviews.html'

# def index(request):
#     apartment_list = Apartment.objects.order_by('-price')
#     context = {
#         'apartment_list': apartment_list,
#     }
#     #The context is a dictionary mapping template variable names to Python objects.
#     return  render(request, 'west/index.html', context)
#
#     #The render() function takes the request object as its first argument, a template name as its second argument and a
#     # dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with
#     # the given context.
#
# # def roomates(request)
# #     roomate_list = Roomate.objects.order_by('major')
# #     context = {
# #         'roomate_list': roomate_list
# #     }
# #     return render(request, 'west/roomates.html', context)
# def detail(request, apartment_id):
#     apartment = get_object_or_404(Apartment, pk=apartment_id)
#     return render(request, 'west/detail.html', {'apartment': apartment})
#
# def reviews(request, apartment_id):
#     apartment = get_object_or_404(Apartment, pk=apartment_id)
#     return  render(request, 'west/reviews.html', {'apartment': apartment})

def reviewit(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    try:
        reviewer = request.POST['fname']
        review = request.POST['review']
    except (KeyError, review.DoesNotExist):
        return render(request, 'west/detail.html', {
            'error_message': "TYPE!!!",
        })
    else:
        r = Review(apartment = apartment, name = reviewer,review = review)
        r.save()

    return HttpResponseRedirect(reverse('west:reviews', args=[apartment.id]))
