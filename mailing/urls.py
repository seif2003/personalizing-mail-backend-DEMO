from django.urls import path
from .views import save_template, get_template

urlpatterns = [
    path('save-template/', save_template),
    path('get-template/', get_template),
]