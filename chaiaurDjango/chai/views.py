from django.shortcuts import render
from .models import chaiVariety
# Create your views here.


def allchai(request):
    chais = chaiVariety.objects.all(),
    # yeh ab saare objects laakar de dega of chai
    # as all liya hai so saare objects would come in array
    return render(request, 'chai/all_chai.html', {'chais': chais})
