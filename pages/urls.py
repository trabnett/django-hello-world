from django.urls import path

from .views import HomePageView, Page2PageView

urlpatterns = [
    path('', HomePageView.as_view(), name='hello'),
    path('page2/', Page2PageView.as_view(), name='page2'),
]
