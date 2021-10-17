
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage,),
    path('pu_results.html', views.puPage, name='pu'),
    path('polling', views.pollingPage, name='polling'),
    path('results.html', views.resultPage, name='result'),
    path('new_polls.html', views.newpollPage, name='new_polls'),
]
