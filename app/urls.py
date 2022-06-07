from django.urls import path
from . import views

urlpatterns = [
    path('list',views.jinrongspider),
    path('list1',views.yuyanspider),
    path('list2',views.jisuanjispider),
    path('list3',views.guanlispider),
    path('list4',views.values),
    path('computer',views.computer),
    path('english',views.English),
    path('manage',views.manages),
    path('economys',views.economys),
    path('test',views.test)
]


