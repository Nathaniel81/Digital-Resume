from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('', views.Index.as_view(), name="Index"),
    path('contact/', views.Contact.as_view(), name="contact"),
]