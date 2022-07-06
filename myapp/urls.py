from django.urls import path
from myapp import views


urlpatterns=[
    path('hello/', views.hello),
    path('show/', views.show),
    path('', views.upload_file),
    path('info/', views.methodinfo),
    path('get/',views.getpdf),
]