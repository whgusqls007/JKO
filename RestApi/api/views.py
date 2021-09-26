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
from api.models import Clustering
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import django

# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def getPosts(body=None, className=None, flag="None"):
    first = body["first"]
    last = body["last"]

    if body["emotion"] != "All":
        if body["emotion"] == "neutral":
            Emotion = "중립"
        elif body["emotion"] == "positive":
            Emotion = "긍정"
        elif body["emotion"] == "negative":
            Emotion = "부정"
        elif body["emotion"] == "warm":
            Emotion = "따뜻한"
        elif body["emotion"] == "interesting":
            Emotion = "신기한"
        elif body["emotion"] == "shocking":
            Emotion = "충격적인"
        elif body["emotion"] == "sad":
            Emotion = "슬픈"

    posts = className.objects.order_by("-date")[first:last]

    if body["text"] == "" and body["category"] != "All":
        if body["emotion"] == "All":
            posts = (
                className.objects.filter(category=body["category"]).order_by("-date")[first:last],
            )
        else:
            posts = (
                className.objects.filter(category=body["category"], emotion=Emotion).order_by(
                    "-date"
                )[first:last],
            )

    elif body["text"] != "" and body["category"] == "All":
        posts = className.objects.filter(title__contains=body["text"]).order_by("-date")[first:last]

    elif body["text"] != "" and body["category"] != "All":
        if body["emotion"] == "All":
            posts = className.objects.filter(
                title__contains=body["text"], category=body["category"]
            ).order_by("-date")[first:last]
        else:
            posts = className.objects.filter(
                title__contains=body["text"], category=body["category"], emotion=Emotion
            ).order_by("-date")[first:last]

    if type(posts) == tuple:
        posts = posts[0]

    return posts


def getData(posts, flag="None"):
    data = []
    for post in posts:
        if post.articles:
            urls = []
            press = []
            for articles in post.articles:
                urls.append(articles["url"])
                press.append(articles["press"])
            data.append(
                {
                    "id": str(post._id),
                    "title": post.title,
                    "mainText": post.mainText,
                    "category": post.category,
                    "date": post.date,
                    "articles": post.articles,
                    "url": urls,
                    "press": press,
                    "mainPress": post.mainPress,
                    "reporter": post.reporter,
                    "img": post.img,
                    "emotion": post.emotion,
                    "visible": False,
                }
            )
        else:
            data.append(
                {
                    "id": str(post._id),
                    "title": post.title,
                    "mainText": post.mainText,
                    "category": post.category,
                    "date": post.date,
                    "url": post.url,
                    "reporter": post.reporter,
                    "press": post.press,
                    "img": post.img,
                    "emotion": post.emotion,
                    "visible": False,
                }
            )
    return data


def getData_all(body):
    first = body["first"] // 2
    last = body["last"] // 2

    if body["emotion"] != "All":
        if body["emotion"] == "neutral":
            Emotion = "중립"
        elif body["emotion"] == "positive":
            Emotion = "긍정"
        elif body["emotion"] == "negative":
            Emotion = "부정"
        elif body["emotion"] == "warm":
            Emotion = "따뜻한"
        elif body["emotion"] == "interesting":
            Emotion = "신기한"
        elif body["emotion"] == "shocking":
            Emotion = "충격적인"
        elif body["emotion"] == "sad":
            Emotion = "슬픈"

    classes = []
    press = []
    classes.append(busan)
    press.append("부산일보")
    classes.append(Donga)
    press.append("동아일보")
    classes.append(Hangook)
    press.append("한국일보")
    classes.append(Herald)
    press.append("헤럴드경제")
    classes.append(Joongang)
    press.append("중앙일보")
    classes.append(Joseon)
    press.append("조선일보")
    classes.append(Nocut)
    press.append("노컷뉴스")
    classes.append(Ohmynews)
    press.append("오마이뉴스")
    classes.append(Wikitree)
    press.append("위키트리")
    classes.append(Yeonhap)
    press.append("연합뉴스")

    data = []

    for i in range(len(classes)):
        posts = classes[i].objects.order_by("-date")[first:last]

        if body["text"] == "" and body["category"] != "All":
            if body["emotion"] == "All":
                posts = (
                    classes[i]
                    .objects.filter(category=body["category"])
                    .order_by("-date")[first:last],
                )
            else:
                posts = (
                    classes[i]
                    .objects.filter(category=body["category"], emotion=Emotion)
                    .order_by("-date")[first:last],
                )

        elif body["text"] != "" and body["category"] == "All":
            posts = (
                classes[i]
                .objects.filter(title__contains=body["text"])
                .order_by("-date")[first:last]
            )

        elif body["text"] != "" and body["category"] != "All":
            if body["emotion"] == "All":
                posts = (
                    classes[i]
                    .objects.filter(title__contains=body["text"], category=body["category"])
                    .order_by("-date")[first:last]
                )
            else:
                posts = (
                    classes[i]
                    .objects.filter(
                        title__contains=body["text"], category=body["category"], emotion=Emotion
                    )
                    .order_by("-date")[first:last]
                )

        if type(posts) == tuple:
            posts = posts[0]

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
                    "press": post.press,
                    "img": post.img,
                    "emotion": post.emotion,
                    "visible": False,
                }
            )

    data = sorted(data, reverse=True, key=lambda x: x["date"])

    return data


@csrf_exempt
def function(className=None, request=None):
    print("IP :", get_client_ip(request))

    body = json.loads(request.body)

    if "#" in body["text"] or "||" in body["text"]:
        return json.dumps([])

    if body["isCluster"]:
        posts = getPosts(body, className)
        data = getData(posts, flag="Main")
        return json.dumps(data)
    else:
        if className == Clustering:
            data = getData_all(body)
        else:
            posts = getPosts(body, className)
            data = getData(posts, flag="None")

        return json.dumps(data)


@csrf_exempt
def read_busan(request):
    return HttpResponse(function(className=busan, request=request))


@csrf_exempt
def read_ohmynews(request):
    return HttpResponse(function(className=Ohmynews, request=request))


@csrf_exempt
def read_wikitree(request):
    return HttpResponse(function(className=Wikitree, request=request))


@csrf_exempt
def read_herald(request):
    return HttpResponse(function(className=Herald, request=request))


@csrf_exempt
def read_nocut(request):
    return HttpResponse(function(className=Nocut, request=request))


@csrf_exempt
def read_donga(request):
    return HttpResponse(function(className=Donga, request=request))


@csrf_exempt
def read_yeonhap(request):
    return HttpResponse(function(className=Yeonhap, request=request))


@csrf_exempt
def read_hangook(request):
    return HttpResponse(function(className=Hangook, request=request))


@csrf_exempt
def read_joongang(request):
    return HttpResponse(function(className=Joongang, request=request))


@csrf_exempt
def read_joseon(request):
    return HttpResponse(function(className=Joseon, request=request))


@csrf_exempt
def read_subs(request):
    return HttpResponse(function2(request=request))


@csrf_exempt
def read_main(request):
    return HttpResponse(function(className=Clustering, request=request))


def function2(request):
    body = json.loads(request.body)

    if "#" in body["text"] or "||" in body["text"]:
        return json.dumps([])

    first = body["first"]
    last = body["last"]
    classNames = body["classNames"]
    if body["emotion"] != "All":
        if body["emotion"] == "neutral":
            Emotion = "중립"
        elif body["emotion"] == "positive":
            Emotion = "긍정"
        elif body["emotion"] == "negative":
            Emotion = "부정"
        elif body["emotion"] == "warm":
            Emotion = "따뜻한"
        elif body["emotion"] == "interesting":
            Emotion = "신기한"
        elif body["emotion"] == "shocking":
            Emotion = "충격적인"
        elif body["emotion"] == "sad":
            Emotion = "슬픈"
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

        if body["text"] == "" and body["category"] != "All":
            if body["emotion"] == "All":
                posts = (
                    classes[i]
                    .objects.filter(category=body["category"])
                    .order_by("-date")[first:last],
                )
            else:
                posts = (
                    classes[i]
                    .objects.filter(category=body["category"], emotion=Emotion)
                    .order_by("-date")[first:last],
                )

        elif body["text"] != "" and body["category"] == "All":
            posts = (
                classes[i]
                .objects.filter(title__contains=body["text"])
                .order_by("-date")[first:last]
            )

        elif body["text"] != "" and body["category"] != "All":
            if body["emotion"] == "All":
                posts = (
                    classes[i]
                    .objects.filter(title__contains=body["text"], category=body["category"])
                    .order_by("-date")[first:last]
                )
            else:
                posts = (
                    classes[i]
                    .objects.filter(
                        title__contains=body["text"], category=body["category"], emotion=Emotion
                    )
                    .order_by("-date")[first:last]
                )

        if type(posts) == tuple:
            posts = posts[0]

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
                    "img": post.img,
                    "emotion": post.emotion,
                    "visible": False,
                }
            )

    data = sorted(data, reverse=True, key=lambda x: x["date"])

    return json.dumps(data)
