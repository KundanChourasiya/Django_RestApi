from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^Product/$', views.ProductList.as_view()),
    url(r'^Product/(?P<pk>[0-9]+)', views.ProductDetails.as_view()),
]