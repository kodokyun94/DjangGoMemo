from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger
from lunchMenu.models import LunchMenu


def main(request):
    # 단순 문자열 출력
    # return HttpResponse("Hello World!")

    # 화면 연결
    return render(request, 'main.html')

def main2(request):
    return render(request, 'main2.html')

# burgers = Burger.objects.filter(name__endswith="버거")

def burger_list(request):
    burgers = Burger.objects.all()
    # print(f"전체 햄버거 목록 : {burgers}")
    context = {'burgers': burgers}
    return render(request, 'burger_list.html',context)


def lunchMenu_list(request):

    lunchMenus = LunchMenu.objects.all()
    context = {'lunchMenus': lunchMenus}
    return render(request, 'lunchMenu_list.html',context)