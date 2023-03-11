
"""Afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from movie_app.views import *
from users.views import *

list_create = {
    'get':'list',
    'post': 'create'}
update_retrieve_destroy = {
    'get': 'retrieve',
    'put':'update',
    'delete':'destroy'
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', MovieModelViewSet.as_view(list_create)),
    path('api/v1/movies/<int:pk>/',MovieModelViewSet.as_view(update_retrieve_destroy)),
    path('api/v1/directors/', DirectorModelViewSet.as_view(list_create)),
    path('api/v1/directors/<int:pk>/', DirectorModelViewSet.as_view(update_retrieve_destroy)),
    path('api/v1/reviews/', ReviewModelViewSet.as_view(list_create)),
    path('api/v1/reviews/<int:pk>/', ReviewDetailModelsViewSet.as_view(update_retrieve_destroy)),
    path('api/v1/users/registration/', RegistrationAPIView.as_view()),
    path('api/v1/users/authorization/', AuthorizationAPIView.as_view()),
    path('api/v1/users/confirmation/', ConfirmationAPIView.as_view())
]
