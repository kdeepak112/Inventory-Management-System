
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', views.home, name="home"),
    path('main/<str:function>/', views.main, name="main"),
    path('operation/<str:oper>/<str:section>/', views.operation, name="operation"),
    path('balance',views.balance,name="balance"),
    path('locBalance/<int:loc_id>/',views.locBalance,name='locBalance')

]
