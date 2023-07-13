import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    BUS_STATIONS = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as f:
        for row in csv.DictReader(f):
            BUS_STATIONS.append(row)
        paginator = Paginator(BUS_STATIONS, 10)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            'bus_stations': page,
            'page': page,
    }
    return render(request, 'stations/index.html', context)
