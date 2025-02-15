from django.conf.urls import url,include
from Pagination_App import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('emp-viewset', views.EmpViewSet)

urlpatterns=[
    url(r'',include(router.urls))
]