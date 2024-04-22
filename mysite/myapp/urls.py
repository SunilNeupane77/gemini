from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.home),
    path('aboutus/',views.aboutus),
    path('home/<id>',views.dynamicHome)
]
