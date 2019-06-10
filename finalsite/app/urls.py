from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    path('homepage', views.index),
    path('最新消息', views.the_news),
    path('關於我們', views.about_us),
    path('題庫', views.item_bank),
    path('模擬題', views.simulation_prob),
    path('quiz_BTS', views.quiz_BTS),
    path('quiz_GOT7', views.quiz_GOT7),
    path('quiz_seventeen', views.quiz_seventeen),
    path('quiz_TWICE', views.quiz_TWICE),
    path('quiz_SJ', views.quiz_SJ),
    path('quiz_EXO', views.quiz_EXO),
    path('itembank_BTS', views.itembank_BTS),
    path('itembank_EXO', views.itembank_EXO),
    path('itembank_TWICE', views.itembank_TWICE),
    path('itembank_seventeen', views.itembank_seventeen),
    path('itembank_SJ', views.itembank_SJ),
    path('itembank_GOT7', views.itembank_GOT7),
    ]