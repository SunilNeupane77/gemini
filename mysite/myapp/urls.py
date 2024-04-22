from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('aboutus/',views.aboutus,name='aboutuspage'),
    path('home/<id>',views.dynamicHome,name="dynamic")
]
