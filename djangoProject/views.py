from django.http import HttpResponse
from django.shortcuts import render
def main(request):
    # 단순 문자열 출력
    # return HttpResponse("Hello World!")
    # 화면 연결
    return render(request, 'main.html')
def main2(request):
    return render(request, 'main2.html')