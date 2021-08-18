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

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def function(className, request, press):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("IP :", ip)

    body = json.loads(request.body)
    
    if "#" in body["text"] or "||" in body["text"]:
        return json.dumps([])

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
    return HttpResponse(function(busan, request, "부산일보"))


@csrf_exempt
def read_ohmynews(request):
    return HttpResponse(function(Ohmynews, request, "오마이뉴스"))


@csrf_exempt
def read_wikitree(request):
    return HttpResponse(function(Wikitree, request, "위키트리"))


@csrf_exempt
def read_herald(request):
    return HttpResponse(function(Herald, request, "헤럴드경제"))


@csrf_exempt
def read_nocut(request):
    return HttpResponse(function(Nocut, request, "노컷뉴스"))


@csrf_exempt
def read_donga(request):
    return HttpResponse(function(Donga, request, "동아일보"))


@csrf_exempt
def read_yeonhap(request):
    return HttpResponse(function(Yeonhap, request, "연합뉴스"))


@csrf_exempt
def read_hangook(request):
    return HttpResponse(function(Hangook, request, "한국일보"))


@csrf_exempt
def read_joongang(request):
    return HttpResponse(function(Joongang, request, "중앙일보"))


@csrf_exempt
def read_joseon(request):
    return HttpResponse(function(Joseon, request, "조선일보"))

@csrf_exempt
def read_subs(request):
    return HttpResponse(function2(request))

def function2(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print("IP :", ip)

    body = json.loads(request.body)

    if "#" in body["text"] or "||" in body["text"]:
        return json.dumps([])

    first = body["first"]
    last = body["last"]
    classNames = body["classNames"]
    classes = []
    press = []
    for className in classNames:
        if className == "read_busan/":
            classes.append(busan)
            press.append("부산일보")
        elif className == "read_donga/":
            classes.append(Donga)
            press.append("동아일보")
        elif className == "read_hangook/":
            classes.append(Hangook)
            press.append("한국일보")
        elif className == "read_herald/":
            classes.append(Herald)
            press.append("헤럴드경제")
        elif className == "read_joongang/":
            classes.append(Joongang)
            press.append("중앙일보")
        elif className == "read_joseon/":
            classes.append(Joseon)
            press.append("조선일보")
        elif className == "read_nocut/":
            classes.append(Nocut)
            press.append("노컷뉴스")
        elif className == "read_ohmynews/":
            classes.append(Ohmynews)
            press.append("오마이뉴스")
        elif className == "read_wikitree/":
            classes.append(Wikitree)
            press.append("위키트리")
        else:
            classes.append(Yeonhap)
            press.append("연합뉴스")
    
    data = []

    for i in range(len(classes)):
        posts = classes[i].objects.order_by("-date")[first:last]
        if body["text"] != "":
            posts = classes[i].objects.filter(title__contains=body["text"]).order_by(
                "-date"
            )[first:last]
        if body["category"] != "All":
            posts = classes[i].objects.filter(category=body["category"]).order_by("-date")[
                first:last
            ]
        if body["category"] != "All" and body["text"] != "":
            posts = classes[i].objects.filter(
                title__contains=body["text"], category=body["category"]
            ).order_by("-date")[first:last]

        
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
                    "press": press[i],
                    "visible": False,
                }
            )
    
    data = sorted(data, reverse=True, key=lambda x : x["date"])

    return json.dumps(data)

    
