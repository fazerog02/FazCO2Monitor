from django.shortcuts import render
from api.models import NowPPM
from api.models import PPMData

import datetime
import matplotlib
from matplotlib import pyplot

# Create your views here.


def home(request):
    nowppm = NowPPM.objects.get(id=1)

    return render(request, 'home.html', {'nowppm': nowppm, })

