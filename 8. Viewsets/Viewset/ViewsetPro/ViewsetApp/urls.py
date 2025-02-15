from django.conf.urls import url
from django.conf.urls import include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', views.ViewSet_Feedback, base_name='viewset')

urlpatterns=[
    url(r'^', include(router.urls))
]