
from django.urls import path
from . import views
urlpatterns=[path('',views.index,name='index'),
             path('category/<slug:slug>.html',views.category_detail,name='category_detail'),
             path('game/<slug:slug>/',views.game_detail,name='game_detail'),
             path('game/<slug:slug>/rate/',views.rate_game,name='rate_game')]
