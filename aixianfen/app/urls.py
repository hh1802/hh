from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    # url(r'^exl/', views.excel_export, name='home'),
    url(r'^market/$',views.market, name='market'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$',views.user_market, name='market_parmas'),

]