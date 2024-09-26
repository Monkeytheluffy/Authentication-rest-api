from django.contrib import admin
from django.urls import path, include
from Book import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('data', views.Studentviewset, basename='student')

urlpatterns=[
    path('', include(router.urls)),
    path('sachin/', include('rest_framework.urls', namespace='sachin')),
]