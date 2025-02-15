from django.conf.urls import url,include
from TokenAuthenticaton_App import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('emp-viewset', views.EmpViewset)

urlpatterns= [
    url(r'',include(router.urls)),
]