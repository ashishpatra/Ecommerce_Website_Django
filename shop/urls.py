from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("search/", views.search, name="Search"),
]
