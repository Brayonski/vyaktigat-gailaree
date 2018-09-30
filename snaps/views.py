from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def wholegallery(request):
    snaps = Image.objects.all()
    return render(request, 'all-snaps/snaps.html',{"snaps":snaps})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_image(search_term)
        message = f"{search_term}"
        return render(request, 'all-snaps/search.html', {"message":message, "categories": searched_categories})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-snaps/search.html',{"message":message},)

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-snaps/snaps.html", {"image":image})
