import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


# def bus_stations(request):
#     # получите текущую страницу и передайте ее в контекст
#     # также передайте в контекст список станций на странице
#     page_num = int(request.GET.get('page', 1))
#     stations = list()
#     with open(BUS_STATION_CSV,  newline='') as stations_csv:
#         reader = csv.DictReader(stations_csv)
#         for row in reader:
#             if (page_num - 1) * 10 + 2 <= reader.line_num <= page_num * 10 + 1:
#                 stations.append(row)
#                 print(row)
#     with open(BUS_STATION_CSV, newline='') as stations_csv2:
#         reader2 = csv.DictReader(stations_csv2)
#         paginator = Paginator(list(reader2), 10)
#         page = paginator.get_page(page_num)
#
#     context = {
#         'bus_stations': stations,
#         'page': page,
#     }
#     return render(request, 'stations/index.html', context)

# Easier way
def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = int(request.GET.get('page', 1))
    with open(BUS_STATION_CSV,  newline='') as stations_csv:
        reader = csv.DictReader(stations_csv)
        stations = list(reader)
        paginator = Paginator(list(stations), 10)
        page = paginator.get_page(page_num)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
