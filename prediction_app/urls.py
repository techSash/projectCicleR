from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('handle_image_upload', views.handle_image_upload, name='handle_image_upload')
]
