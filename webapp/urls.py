from django.urls import path, include
from . import views
urlpatterns = [
path('', views.about_me),
path('portfolio/', views.portfolio),
path('contact/', views.contact)
]