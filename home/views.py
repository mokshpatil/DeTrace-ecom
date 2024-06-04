from django.shortcuts import render, HttpResponse

# Create your views here.

listings = [
    {
        'title':'prod 1',
        'seller':'seller1',
        'price':'p1',
        'date_Listed':'date1'
    },
    {
        'title':'prod 2',
        'seller':'seller2',
        'price':'p2',
        'date_Listed':'date2'
    },
]

def index(request):
    context = {
        'listings': listings
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("about page")