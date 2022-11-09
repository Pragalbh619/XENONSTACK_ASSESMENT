from django.contrib import admin
from django.urls import path, include
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login',views.login,name='login'),
    path('upload_category',views.upload_category,name='upload_category'),
    path('product_list',views.product_list,name='product_list'),
    path('save',views.save,name='save'),
    path('logout',views.logout,name='logout'),
    path('save_category',views.save_category,name='save_category'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('category_list',views.category_list,name='category_list'),
    path('delete_category',views.delete_category,name='delete_category'),
    path('upload_product',views.upload_product,name='upload_product'),
    path('product_upload',views.product_upload,name='product_upload'),
    #path('reset',views.reset,name='reset'),
    #path('verify',views.verify,name='verify'),
    #path('match',views.match,name='match'),
    #path('newpassword',views.newpassword,name='newpassword'),
    path('delete1',views.delete1,name='delete1'),
    path('delete',views.delete,name='delete'),
    path('ordertable',views.ordertable,name='ordertable')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
