from django.shortcuts import render
import datetime
now = datetime.datetime.now()

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.day==1 and now.month==1
    })