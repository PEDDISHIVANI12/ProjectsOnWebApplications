"""MyFirstDjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup/', views.SignUp.as_view(), name='signup'),
 # path('signup/', views.SignUp.as_view(), name='signup'),
    #url(r'^signup/$',views.SignUp.as_view(),name="signup"),
   # url(r'^login/$',views.login,name="login"),
    path('cart/',views.cart,name="cart"),
    path('add_service/',views.AddService,name="add_service"),
   # url(r'^address/$',views.Address,name="address"),
    path('track/',views.track,name="track"),
    #path('again/',views.index,name="track"),
  #  url(r'^again/$',views.again,name="again"),
    #url(r'^logout/$',views.logout,name="logout"),
    path('add_service_submit/',views.AddService_submit,name="add_service_submit"),
]
