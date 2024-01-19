from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            #return HttpResponse(str(TFDO.cleaned_data['topic_name']))
            tn=TFDO.cleaned_data['topic_name']
            to=Topic.objects.get_or_create(topic_name=tn)[0]
            to.save()
            return HttpResponse('Topic is added')
            
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse('Webpage is added')

    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EAFO=Accessrecordform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=Accessrecordform(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(name=n)
            a=AFDO.cleaned_data['author']
            d=AFDO.cleaned_data['date']
            AO=Accessrecord.objects.get_or_create(name=WO,author=a,date=d)[0]
            AO.save()
            return HttpResponse('Webpage is added')

    return render(request,'insert_accessrecord.html',d)

# def select_multiple_webpage(request): 
#     QLTO=Topic.objects.all()        #by html page we are displying the form and inserting data
#     d={'topics':QLTO}
#     if request.method=='POST':
#         topiclist=request.POST.getlist('tn')
#         #print(topiclist)   #will show in cmd
#         QLWO=Webpage.objects.none()
#         for tn in topiclist:
#             QLWO=QLWO|Webpage.objects.filter(topic_name=tn)
#         d1={'webpage':QLWO}
#         return render(request,'display_webpage.html',d1)

#     return render(request,'select_multiple_webpage.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    return render(request,'checkbox.html',d)

def select_multiple_webpage(request):   #by django forms we are displying data
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        topiclist=request.POST.getlist('topic_name')
        #print(topiclist)   #will show in cmd
        QLWO=Webpage.objects.none()
        for tn in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=tn)
        d1={'webpage':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)

def select_multiple_accessrecord(request):
    EAFO=Accessrecordform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        wepagelist=request.POST.getlist('name')
        QLAO=Accessrecord.objects.none()
        for ao in wepagelist:
            QLAO=QLAO|Accessrecord.objects.filter(name=ao)
        d1={'access':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'select_multiple_accessrecord.html',d)
