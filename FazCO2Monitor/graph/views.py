from django.shortcuts import render
from api.models import PPMData
from api.models import NowPPM
import datetime

import matplotlib
from matplotlib import pyplot
import tkinter
import numpy

def today(request):
    nowYear = datetime.datetime.now().year
    nowMonth = datetime.datetime.now().month
    nowDate = datetime.datetime.now().day
    nowppm = NowPPM.objects.get(id=1)
    ppmdataList = PPMData.objects.filter(date__year=nowYear, date__month=nowMonth, date__day=nowDate)

    left = []
    height = []
    for i in range(24):
        left.append(str(i))
        height.append(0)
        counter = 0
    for i in range(ppmdataList[0].date.hour, len(ppmdataList) + ppmdataList[0].date.hour):
        height[i] = ppmdataList[counter].value
        counter += 1
    pyplot.plot(left, height, marker="o", color='black')
    pyplot.savefig('statics/img/plot.png')
    pyplot.clf()

    return render(request, 'graph/graphToday.html', {})

def date(request):
    if 'chosenDate' in request.POST:
        chosenDate = request.POST['chosenDate']
    else:
        chosenDate = None

    ppmdataList = None
    lenPpmdataList = None
    if chosenDate != None and chosenDate != '':
        chosenDate_datetime = datetime.datetime.strptime(chosenDate, "%Y-%m-%d")
        ppmdataList = PPMData.objects.filter(date__year=chosenDate_datetime.year, date__month=chosenDate_datetime.month, date__day=chosenDate_datetime.day)
        ppmdataList = sorted(ppmdataList, key=lambda x: x.date)
        lenPpmdataList = len(ppmdataList)
        left = []
        height = []
        if len(ppmdataList) > 0:
            for i in range(24):
                left.append(str(i))
                height.append(0)
            counter = 0
            for i in range(ppmdataList[0].date.hour, len(ppmdataList)+ppmdataList[0].date.hour):
                height[i] = ppmdataList[counter].value
                counter += 1
            pyplot.plot(left, height, marker="o", color='black')
            pyplot.savefig('statics/img/plot.png')
            pyplot.clf()
    return render(request, 'graph/graphDate.html', {'ppmdataList': ppmdataList, 'lenPpmdataList': lenPpmdataList, 'chosenDate': chosenDate})

def month(request):
    if 'chosenMonth' in request.POST:
        chosenMonth = request.POST['chosenMonth']
    else:
        chosenMonth = None
    ppmdataList = None
    lenPpmdataList = None
    ppmdataListEachDay = []
    if chosenMonth != None and chosenMonth != '':
        chosenMonth_datetime = datetime.datetime.strptime(chosenMonth, "%Y-%m")
        ppmdataList = PPMData.objects.filter(date__year=chosenMonth_datetime.year, date__month=chosenMonth_datetime.month)
        ppmdataList = sorted(ppmdataList, key=lambda x: x.date)
        lenPpmdataList = len(ppmdataList)
        left = []
        height = []
        if len(ppmdataList) > 0:
            for i in range(1, 32) if chosenMonth_datetime.month == 1 or chosenMonth_datetime.month == 3 or chosenMonth_datetime.month == 5 or chosenMonth_datetime.month == 7 or chosenMonth_datetime.month == 8 or chosenMonth_datetime.month == 10 or chosenMonth_datetime.month == 12 else range(1, 31):
                left.append(i)
                height.append(0)
            counter = 0
            ppmdataListEachDay = []
            ppmdataListEachDaySum = 0
            beforeElementDate = 404
            ppmdataListEachDaySize = 0
            for ppmdata in ppmdataList:
                if ppmdata.date.day != beforeElementDate and beforeElementDate != 404:
                    ppmdataListEachDayValue = round(ppmdataListEachDaySum / ppmdataListEachDaySize)
                    ppmdataListEachDay.append(ppmdataListEachDayValue)
                    ppmdataListEachDaySum = 0
                    ppmdataListEachDaySize = 0
                beforeElementDate = ppmdata.date.day
                ppmdataListEachDaySum += ppmdata.value
                ppmdataListEachDaySize += 1
            ppmdataListEachDayValue = round(ppmdataListEachDaySum / ppmdataListEachDaySize)
            ppmdataListEachDay.append(ppmdataListEachDayValue)
            for i in range(ppmdataList[0].date.day-1, len(ppmdataListEachDay)+ppmdataList[0].date.day-1):
                height[i] = ppmdataListEachDay[counter]
                counter += 1
            pyplot.plot(left, height, marker="o", color='black')
            pyplot.savefig('statics/img/plot.png')
            pyplot.clf()
    return render(request, 'graph/graphMonth.html', {'ppmdataList': ppmdataList, 'lenPpmdataList': lenPpmdataList, 'chosenMonth': chosenMonth})

def year(request):
    if 'chosenYear' in request.POST:
        chosenYear = request.POST['chosenYear']
    else:
        chosenYear = None
    ppmdataList = None
    lenPpmdataList = None
    ppmdataListEachDay = []
    if chosenYear != None and chosenYear != '' and 2000 <= int(chosenYear) <= 2300:
        ppmdataList = PPMData.objects.filter(date__year=chosenYear)
        ppmdataList = sorted(ppmdataList, key=lambda x: x.date)
        lenPpmdataList = len(ppmdataList)
        left = []
        height = []
        if len(ppmdataList) > 0:
            for i in range(1, 13):
                left.append(i)
                height.append(0)
            counter = 0
            ppmdataListEachDay = []
            ppmdataListEachDaySum = 0
            beforeElementDate = 404
            ppmdataListEachDaySize = 0
            for ppmdata in ppmdataList:
                if ppmdata.date.month != beforeElementDate and beforeElementDate != 404:
                    ppmdataListEachDayValue = round(ppmdataListEachDaySum / ppmdataListEachDaySize)
                    ppmdataListEachDay.append(ppmdataListEachDayValue)
                    ppmdataListEachDaySum = 0
                    ppmdataListEachDaySize = 0
                beforeElementDate = ppmdata.date.month
                ppmdataListEachDaySum += ppmdata.value
                ppmdataListEachDaySize += 1
            ppmdataListEachDayValue = round(ppmdataListEachDaySum / ppmdataListEachDaySize)
            ppmdataListEachDay.append(ppmdataListEachDayValue)
            for i in range(ppmdataList[0].date.month-1, len(ppmdataListEachDay)+ppmdataList[0].date.month-1):
                height[i] = ppmdataListEachDay[counter]
                counter += 1
            pyplot.plot(left, height, marker="o", color='black')
            pyplot.savefig('statics/img/plot.png')
            pyplot.clf()
    return render(request, 'graph/graphYear.html', {'ppmdataList': ppmdataList, 'lenPpmdataList': lenPpmdataList, 'chosenYear': chosenYear})

def archive(request):
    return render(request, 'graph/graphArchive.html', {})