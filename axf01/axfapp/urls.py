from django.conf.urls import url

from axfapp import views

urlpatterns = [
    url(r'^home/',views.excel_export, name='home'),
    # url(r'^mine/',views.mine, name='mine'),
    # url(r'^market/$', views.market, name='market'),
    # url(r'^market/(\d+)/(\d+)/(\d+)/', views.user_market, name='user_market'),
    # url(r'^addcart/', views.addcart, name='addcart'),
    # url(r'^subcart/', views.subcart, name='subcart'),
    # url(r'^cart/', views.cart, name='cart'),
    # url(r'^change_select_status/', views.change_select_status, name='change_select_status'),
    # url(r'^generateorder/', views.generate_order, name='generateorder'),
    # url(r'^changepaystatus/', views.changepaystatus, name='changepaystatus'),
    # url(r'^waitpay/', views.wait_pay, name='waitpay')

]