from django.shortcuts import render
from markdown import serializers

from .models import User
from .models import Station
from django.db.models import Q
from .models import News
from .models import SiteRoute
from .models import Route
import json
from collections import Counter


# Create your views here.
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        news = News.objects.all()
        news_obj = toDicts(news)
        news_json = json.dumps(news_obj, ensure_ascii=False)
        return HttpResponse(news_json)
    else:
        return HttpResponse("Please send the request in POST.")

def busnum(request):
    if request.method == "POST":
        data_json = json.loads(request.body)
        try:
            data = {}
            route = SiteRoute.objects.filter(busid = data_json["busid"])
            if route.count() == 0:
                return HttpResponse("Did not find the corresponding information.")
            else:
                te = []
                for temp in route.values("stationname"):
                    te.append(temp["stationname"])
                data[data_json["busid"]] = list(te)
                data = json.dumps(data)
                return HttpResponse(data)
        except(KeyError,SiteRoute.DoesNotExist):
            return HttpResponse("Did not find the corresponding information.")
    else:
        return HttpResponse("Please send the request in POST.")

def SearchRoute(request):
    if request.method == "POST":
        data_json = json.loads(request.body)
        try:
            startid = data_json["startid"]
            endid = data_json["endid"]
            temp1,temp2 = isDirect(startid,endid)  #直达
            if temp1 == -1:
                t1,r1,t2,r2 = Transfer(startid,endid)
                if t1 == -1:
                    tmp1,rou1,tmp2,rou2,tmp3,rou3 = Trans2(startid,endid)
                    if tmp1 == -1:
                        return HttpResponse("请检查站点是否输入错误！")
                    else:
                        data = {}
                        data["transferTimes"] = 2
                        data[tmp1] = list(rou1)
                        data[tmp2] = list(rou2)
                        data[tmp3] = list(rou3)
                        data = json.dumps(data)
                        return HttpResponse(data)
                else:
                    data = {}
                    data["transferTimes"] = 1
                    data[t1] = list(r1)
                    data[t2] = list(r2)
                    data = json.dumps(data)
                    return HttpResponse(data)
            else:
                data = {}
                data["transferTimes"] = 0
                data[temp1] = list(temp2)
                data = json.dumps(data)
                return HttpResponse(data)
        except(KeyError):
            return HttpResponse("Did not find the corresponding information.")
    else:
        return HttpResponse("Please send the request in POST.")

def SearchBus(request):
    if request.method == "POST":
        data_json = json.loads(request.body)
    try:
        staname = data_json["stationname"]
        result = SiteRoute.objects.filter(stationname=staname).values("busid")
        if result.count() == 0:
            return HttpResponse("站点不存在")
        else:
            temp = []
            for i in result:
                temp.append(i.get("busid"))
            data = {}
            data["passid"] = list(temp)
            data = json.dumps(data)
            return HttpResponse(data)
    except(KeyError):
        return HttpResponse("error")




def toDicts(objs):
        obj_arr=[]
        for o in objs:
            obj_arr.append(o.toDict())
        return obj_arr

def isDirect(id1,id2):
    route = []
    tmp1 = Route.objects.all()
    for i in tmp1:
        tmp2 = i.route.split("/")
        if (id1 in tmp2) and (id2 in tmp2):
            b1 = SiteRoute.objects.filter(stationname=id1,busid=i.busid).values("siteinbus")
            b2 = SiteRoute.objects.filter(stationname=id2,busid=i.busid).values("siteinbus")
            n1 = b1[0].get("siteinbus")
            n2 = b2[0].get("siteinbus")
            if n1 > n2:
                for j in range(n1, n2 - 1, -1):
                    route.append(tmp2[j - 1])
            else:
                for j in range(n1, n2 + 1):
                    route.append(tmp2[j - 1])
            return i.busid,route
        else:
            continue
    return -1,-1

def Transfer(id1, id2):
    route1 = []
    route2 = []
    b1 = SiteRoute.objects.filter(stationname=id1)
    b2 = SiteRoute.objects.filter(stationname=id2)
    for i in b1:
        r1 = Route.objects.filter(busid=i.busid).values("route")[0]
        t1 = str(r1.get("route")).split("/")
        for j in b2:
            r2 = Route.objects.filter(busid=j.busid).values("route")[0]
            t2 = str(r2.get("route")).split("/")
            for k in t1:
                if k in t2:
                    if t1.index(k) > t1.index(id1):
                        for m in range(t1.index(id1),t1.index(k)+1):
                            route1.append(t1[m])
                    else:
                        for m in range(t1.index(id1),t1.index(k)-1,-1):
                            route1.append(t1[m])

                    if t2.index(k) > t2.index(id2):
                        for m in range(t2.index(k),t2.index(id2)-1,-1):
                            route2.append(t2[m])
                    else:
                        for m in range(t2.index(k),t2.index(id2)+1):
                            route2.append(t2[m])
                    return i.busid,route1,j.busid,route2
    return -1,-1,-1,-1

def Trans2(id1,id2):
    route1 = []
    route2 = []
    route3 = []
    b1 = SiteRoute.objects.filter(stationname=id1).values("busid")
    b2 = SiteRoute.objects.filter(stationname=id2).values("busid")
    for i in b1:
        for j in b2:
            tmp = Route.objects.filter(~Q(busid=i.get("busid")),~Q(busid=j.get("busid")))
            r1 = Route.objects.filter(busid=i.get("busid"))[0].route.split("/")
            r2 = Route.objects.filter(busid=j.get("busid"))[0].route.split("/")
            for k in tmp:
                t1 = str(k.route).split("/")
                for m1 in t1:
                    if m1 in r1:
                        for m2 in t1:
                            if (m2 in r2) and (m1 != m2):
                                if r1.index(id1) > r1.index(m1):
                                    for l in range(r1.index(id1), r1.index(m1)-1,-1):
                                        route1.append(r1[l])
                                else:
                                    for l in range(r1.index(id1), r1.index(m1)+1):
                                        route1.append(r1[l])

                                if t1.index(m1) > t1.index(m2):
                                    for l in range(t1.index(m1), t1.index(m2)-1, -1):
                                        route2.append(t1[l])
                                else:
                                    for l in range(t1.index(m1), t1.index(m2) + 1):
                                        route2.append(t1[l])

                                if r2.index(m2) > r2.index(id2):
                                    for l in range(r2.index(m2), r2.index(id2)-1,-1):
                                        route3.append(r2[l])
                                else:
                                    for l in range(r2.index(m2), r2.index(id2)+1):
                                        route3.append(r2[l])
                                return i.get("busid"),route1,k.busid,route2,j.get("busid"),route3
    return -1,-1,-1,-1,-1,-1

def Judge(obj1,obj2):
    for i in obj1:
        for j in obj2:
            if i == j:
                return i
            else:
                continue
    return -1












