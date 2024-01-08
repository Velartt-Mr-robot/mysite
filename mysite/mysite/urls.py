from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('hello/', include('hello.urls')),    
    path('polls/', include('polls.urls')),
    path('autos/', include('autos.urls')),
    path('ads/', include('ads.urls')),
    path('myarts/', include('myarts.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home/main.html')),
]