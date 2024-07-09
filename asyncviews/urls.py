from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api, name='api'),
    path('api2/', views.async_view, name='async-view'),
    path('api3/', views.sync_view, name='sync-view')
]
