from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactMe"),
    path('tracker/',views.tracker,name="Tracker"),
    path('productview/', views.prodview, name="ProductView"),
    path('search/', views.search, name="Search"),
    path('checkout/', views.chkout, name="CheckOut"),
]