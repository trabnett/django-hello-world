from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from pages import models

import random

# import pdb; pdb.set_trace()


class HomePageView(TemplateView):
    # person = models.Person.objects.create(name='tim', password='AAAAAA1!')
    # person = models.Person.objects.filter(name='tim')
    person = models.Person.objects.get(name='tim')
    print(person.name, "=======", person.password)
    template_name = 'hello.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hello'] = "hello"
        context['goodbye'] = 'goodbye'
        return context

class Page2PageView(TemplateView):
    template_name = 'page2.html'

    def get_context_data(self, **kwargs):
        context = super(Page2PageView, self).get_context_data(**kwargs)
        array = [
            "The greatest glory in living lies not in never falling, but in rising every time we fall.",
            "The way to get started is to quit talking and begin doing.",
            "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
            "If life were predictable it would cease to be life, and be without flavor.",
            "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
            "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
            "Life is what happens when you're busy making other plans.",
            "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
            "When you reach the end of your rope, tie a knot in it and hang on.",
            "Always remember that you are absolutely unique. Just like everyone else.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Tell me and I forget. Teach me and I remember. Involve me and I learn."
        ]
        num = random.randint(0,11)
        print("------------>", num)
        context['quote'] = array[num]
        return context

# def homePageView(request):
#     x = "hi everyone out there".split()
#     print(x)
#     return HttpResponse(x[0].title())
