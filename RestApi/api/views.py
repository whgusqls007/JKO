from api.models import busan
from api.models import Ohmynews
from api.models import Wikitree
from api.models import Nocut
from api.models import Herald
from api.models import Donga
from api.models import Joongang
from api.models import Joseon
from api.models import Yeonhap
from api.models import Hangook
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json

# Create your views here.


@csrf_exempt
def function(className, request):
    body = json.loads(request.body)
    first = body["first"]
    last = body["last"]
    posts = className.objects.order_by("-date")[first:last]
    if body["text"] != "":
        posts = className.objects.filter(title__contains=body["text"]).order_by(
            "-date"
        )[first:last]
    if body["category"] != "All":
        posts = className.objects.filter(category=body["category"]).order_by("-date")[
            first:last
        ]
    if body["category"] != "All" and body["text"] != "":
        posts = className.objects.filter(
            title__contains=body["text"], category=body["category"]
        ).order_by("-date")[first:last]

    data = []
    press = ""
    if className == busan:
        press = "부산일보"
    elif className == Ohmynews:
        press = "오마이뉴스"
    elif className == Wikitree:
        press = "위키트리"
    elif className == Herald:
        press = "헤럴드경졔"
    elif className == Nocut:
        press = "노컷뉴스"
    elif className == Joongang:
        press = "중앙일보"
    elif className == Joseon:
        press = "조선일보"
    elif className == Yeonhap:
        press = "연합뉴스"
    elif className == Donga:
        press = "동아일보"
    else:
        press = "한국일보"

    for post in posts:
        data.append(
            {
                "id": str(post._id),
                "title": post.title,
                "mainText": post.mainText,
                "category": post.category,
                "date": post.date,
                "url": post.url,
                "reporter": post.reporter,
                "press": press,
                "visible": False,
            }
        )
    return json.dumps(data)


@csrf_exempt
def read_busan(request):
    return HttpResponse(function(busan, request))


@csrf_exempt
def read_ohmynews(request):
    return HttpResponse(function(Ohmynews, request))


@csrf_exempt
def read_wikitree(request):
    return HttpResponse(function(Wikitree, request))


@csrf_exempt
def read_herald(request):
    return HttpResponse(function(Herald, request))


@csrf_exempt
def read_nocut(request):
    return HttpResponse(function(Nocut, request))


@csrf_exempt
def read_donga(request):
    return HttpResponse(function(Donga, request))


@csrf_exempt
def read_yeonhap(request):
    return HttpResponse(function(Yeonhap, request))


@csrf_exempt
def read_hangook(request):
    return HttpResponse(function(Hangook, request))


@csrf_exempt
def read_joongang(request):
    return HttpResponse(function(Joongang, request))


@csrf_exempt
def read_joseon(request):
    return HttpResponse(function(Joseon, request))
