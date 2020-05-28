
from django.contrib import admin
#from django.conf.urls import url,include
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('Laundry/', include('Laundry.urls')), # new
    path('Laundry/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='cart.html'), name='cart'), 
   # url(r'^',include('Laundry.urls')),
]

