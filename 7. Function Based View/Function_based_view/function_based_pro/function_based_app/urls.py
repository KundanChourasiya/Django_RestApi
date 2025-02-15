from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^Product/$', views.ProductList),
    url(r'^Product/(?P<pk>[0-9]+)', views.ProductDetails),
]
