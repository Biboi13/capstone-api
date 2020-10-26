from django.shortcuts import  get_object_or_404, render, redirect
from django.http import HttpResponse

from api.models import VCT,Respondance,Prob_occur

from django.contrib import messages
from datetime import datetime

from django.views.generic import CreateView
from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView
import datetime
import json
from django.db.models import Sum, Count

# Create your views here.
#routing
def index(request):
    return render(request, 'frontend/index.html')
