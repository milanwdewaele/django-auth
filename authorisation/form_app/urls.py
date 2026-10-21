from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success_view, name='success'),
    path('contact/list/', views.contact_list_view, name='contact_list'),
]
