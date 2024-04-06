from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('event/<event_title>/', views.event_details, name='event_details'),
    path('add_event', views.add_event, name="add_event"),
    path('event/<int:event_id>/delete', views.delete_event, name="delete_event")
]
