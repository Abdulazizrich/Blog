
from django.contrib import admin
from django.urls import path
from mainApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('blog/',Blog.as_view(),name='blog'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
