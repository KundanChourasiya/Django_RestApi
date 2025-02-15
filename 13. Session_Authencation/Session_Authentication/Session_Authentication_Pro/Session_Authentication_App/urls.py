from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import Empviewset2

router = DefaultRouter()

router.register('emp-viewset', Empviewset2, base_name='emp-viewset2')

urlpatterns=[
    url(r'',include(router.urls))
]