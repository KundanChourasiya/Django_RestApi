from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import Empviewset

router =DefaultRouter()

router.register('emp_viewset',Empviewset,base_name='emp-viewset')

urlpatterns=[
    url(r'',include(router.urls))
]