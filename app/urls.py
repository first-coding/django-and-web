from django.urls import path
from . import views

urlpatterns = [
    path('list',views.jinrongspider),
    path('list1',views.yuyanspider),
    path('list2',views.jisuanjispider),
    path('list3',views.guanlispider),
    path('login', views.Login_view),
    path('register', views.register),
    path("computer",views.computer),
    path("economys",views.economys),
    path("english",views.English),
    path("manage",views.manages),
    # path("ana",views.ana),
    path("test",views.pagenumber),
    path("usemain",views.usemain),
    path('getimg',views.imgg)
]

