from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('houses/', views.houses, name='apartments'),

    path('houses/for_sale/', views.for_sale, name='for_sale'),

    path('houses/for_rent/', views.for_rent, name='for_rent'),

    path('houses/furnished/', views.furnished, name='furnished'),

    path('houses/<int:house_id>', views.house_detail, name='house-detail'),

    path('search/', views.search, name='search'),

    path('contact/' ,views.contact, name='contact'),

    path('faq/' ,views.faq, name='faq'),

    path('privacy/' ,views.privacy, name='privacy'),
]

