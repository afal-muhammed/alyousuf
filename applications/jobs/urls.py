from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views
# from applications.accounts.views import handler500, handler404

urlpatterns = [
    path('importer/', views.ImporterView.as_view(), name="importer"),
    path('', views.LandingView.as_view(), name="landing")
    ]