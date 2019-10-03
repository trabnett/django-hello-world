from django.urls import path
from django.conf.urls import include

from .views import HomePageView, Page2PageView

urlpatterns = [
    path('', HomePageView.as_view(), name='hello'),
    path('page2/', Page2PageView.as_view(), name='page2'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
