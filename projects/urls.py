"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import path
from projects.views import HomePage, EditProj, AddProj, ViewProj

urlpatterns = [
    path('', HomePage.as_view(),name= "home"),
    path('<slug>=slug', ViewProj.as_view(), name = 'detail'),
    path('<slug>=slug/edit', EditProj.as_view(), name="edit"),
    path('<slug>=slug/new', AddProj.as_view(), name="new"),
]
