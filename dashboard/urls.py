
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage,),
    path('pu_result', views.puPage, name='pu'),
    path('polling', views.pollingPage, name='polling'),
    path('result', views.resultPage, name='result'),
    path('new_polls', views.newpollPage, name='new_polls'),
]
