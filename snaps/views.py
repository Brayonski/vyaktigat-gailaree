from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image,Location,Category

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def wholegallery(request):
    snaps = Image.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()
    return render(request, 'all-snaps/snaps.html',{"snaps":snaps, "location":location, "category":category})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image(search_term)
        message = f"{search_term}"
        return render(request, 'all-snaps/search.html', {"message":message, "image": searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-snaps/search.html',{"message":message},)

def location_image(request,location_id):
    image_location = Image.objects.filter(location__location=location_id)
    location = Location.objects.all()
    category = Category.objects.all()

    return render(request, 'all-snaps/snaps.html', {"snaps":image_location, "location":location, "category":category})

def category_image(request,category_id):
    image_category = Image.objects.filter(category__category=category_id)
    location = Location.objects.all()
    category = Category.objects.all()

    return render(request, 'all-snaps/snaps.html', {"snaps":image_category, "location":location, "category":category})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-snaps/snaps.html", {"image":image})
