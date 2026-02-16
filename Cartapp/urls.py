
from django.contrib import admin
from django.urls import path
from Cartapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index),
    path('gallery/', views.gallery),
]
