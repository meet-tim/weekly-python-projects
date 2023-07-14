from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models.query import Q
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from accounts.models import House
from accounts.filters import HouseFilter
from analytics.models import ObjectViewed, number_of_visits
from analytics.signals import object_viewed_signal
from analytics.utils import get_client_ip
from accounts.forms import ContactForm

def house_counter():
    all_count = House.objects.all()
    sale_count = House.objects.filter(property_type='Sale')
    rent_count = House.objects.filter(property_type='Rent')
    furnished_count = House.objects.exclude(furnishes='')

    return len(all_count),len(sale_count),len(rent_count),len(furnished_count)

def index(request):
    my_filter = HouseFilter()
    houses = House.objects.filter(exclusive=True)
    all_houses = House.objects.all()
    users = User.objects.all()
    visits = number_of_visits.objects.all().first()
    context = {
        'filter':my_filter,
        'exclusives':houses,
        'all':len(all_houses),
        'users':len(users),
        'visits':visits,
    }
    return render(request,'apartment/index.html',context)

def houses(request):
    houses = House.objects.all()
    my_filter = HouseFilter(request.GET, queryset=houses)
    houses = my_filter.qs 
    paginator = Paginator(houses, 6)
    page_var = 'page'
    page = request.GET.get(page_var)
    val = house_counter()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
        
    context = {
        'page_var':page_var,
        'houses':paginated_queryset,
        'filter':my_filter,
        'all':'active',
        'all_count':val[0],
        'sale_count':val[1],
        'rent_count':val[2],
        'furnished_count':val[3],
    }
    return render(request,'apartment/houses.html',context)

def for_sale(request):
    houses = House.objects.filter(property_type='Sale')
    paginator = Paginator(houses, 6)
    page_var = 'page'
    page = request.GET.get(page_var)
    val = house_counter()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
        
    context = {
        'page_var':page_var,
        'houses':paginated_queryset,
        'sale':'active',
        'all_count':val[0],
        'sale_count':val[1],
        'rent_count':val[2],
        'furnished_count':val[3],
    }
    return render(request,'apartment/houses.html',context)


def for_rent(request):
    houses = House.objects.filter(property_type='Rent')
    paginator = Paginator(houses, 6)
    page_var = 'page'
    page = request.GET.get(page_var)
    val = house_counter()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
        
    context = {
        'page_var':page_var,
        'houses':paginated_queryset,
        'rent':'active',
        'all_count':val[0],
        'sale_count':val[1],
        'rent_count':val[2],
        'furnished_count':val[3],
    }
    return render(request,'apartment/houses.html',context)


def furnished(request):
    houses = House.objects.exclude(furnishes='')
    paginator = Paginator(houses, 6)
    page_var = 'page'
    page = request.GET.get(page_var)
    val = house_counter()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
        
    context = {
        'page_var':page_var,
        'houses':paginated_queryset,
        'furnished':'active',
        'all_count':val[0],
        'sale_count':val[1],
        'rent_count':val[2],
        'furnished_count':val[3],
    }
    return render(request,'apartment/houses.html',context)


def house_detail(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    object_viewed_signal.send(house.__class__,instance=house,request=request)
    val = house_counter()
    houses = House.objects.filter(hitcount__gte=5)[0:3]
    context = {
        'house':house,
        'all_count':val[0],
        'sale_count':val[1],
        'rent_count':val[2],
        'furnished_count':val[3],
        'houses':houses,
    }
    return render(request,'apartment/house-detail.html',context)

    
def search(request):
    query = request.GET.get('q')
    queryset = ''
    if query:
        queryset = House.objects.filter(
        Q(description__icontains = query)|
        Q(price__icontains = query)|
        Q(furnishes__icontains = query)|
        Q(location__icontains = query)).distinct()

    paginator = Paginator(queryset, 6)
    page_var = 'page'
    page = request.GET.get(page_var)
    val = house_counter()
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    

    context = {
        'page_var':page_var,
        'houses':paginated_queryset,
        'all_count':val[0],
        'sale_count':val[1],
        'rent_count':val[2],
        'furnished_count':val[3],
    }
    return render(request,'apartment/houses.html',context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thank you for sending the message. We will get to it as soon as possible')
            return HttpResponseRedirect(request.path_info)

    context = {
        'form':form
    }
    return render(request,'apartment/contact.html',context)


def faq(request):
    
    return render(request,'apartment/faq.html',{})

def privacy(request):
    
    return render(request,'apartment/privacy.html',{})
