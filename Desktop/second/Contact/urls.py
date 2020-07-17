from django.urls import path
from . import views

urlpatterns = [
    path('Contacts/', views.Contact, name = "Contacts"),
    path('Contact_upload', views.Contact_upload, name="Contact_upload"),
]