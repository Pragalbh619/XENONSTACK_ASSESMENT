from django.contrib import admin
from django.urls import path, include
from.import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('query',views.query,name='query'),
    path('query_table',views.query_table,name='query_table'),
    path('product_details',views.product_details,name='product_details'),
    path('pd',views.pd,name="pd"),
    path('shop',views.shop,name="shop"),
    path('checkout',views.checkout,name='checkout'),
    path('purchase1',views.purchase1,name='purchase1'),
    path('faq',views.faq,name="faq")
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
