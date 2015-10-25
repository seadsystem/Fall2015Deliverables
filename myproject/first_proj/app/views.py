from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.core import serializers
from django.shortcuts import render
import json


from .models import Table

# Create your views here.

def graph(request):
    return render(request, 'app/graph.html')

def index(request):
    query_results = Table.objects.all()
    return HttpResponse(query_results)


def make_json(request):
    data = serializers.serialize("json", Table.objects.all())
    return HttpResponse(data, content_type='json')

