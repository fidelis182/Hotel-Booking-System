"""
URL configuration for hotel_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

"""
URL configuration for hotel_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

"""
URL configuration for hotel_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index"),
    path('about/', views.about,name="about"),
    path('notfound/', views.notfound,name="notfound"),
    path('amenities/', views.amenities,name="amenities"),
    path('booking/', views.booking,name="booking"),
    path('contact/', views.contact,name="contact"),
    path('events/', views.events,name="events"),
   path('gallery/', views.gallery,name="gallery"),
   path('loaction/', views.location,name="location"),
   path('offers/', views.offers,name="offers"),
   path('privacy/', views.privacy,name="privacy"),
   path('restaurant/', views.restaurant,name="restaurant"),
   path('room_details/', views.room_details,name="room_details"),
   path('rooms/', views.rooms,name="rooms"),
   
   path('terms/', views.terms,name="terms"),


]


