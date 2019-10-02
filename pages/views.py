from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'hello.html'

class Page2PageView(TemplateView):
    template_name = 'page2.html'

# def homePageView(request):
#     x = "hi everyone out there".split()
#     print(x)
#     return HttpResponse(x[0].title())
