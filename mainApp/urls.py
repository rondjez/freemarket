from django.conf.urls import url
from . import views
from .recaptcha import check_recaptcha

app_name = 'mainApp'

urlpatterns = [

    # maintenance page
    # url(r'^$', views.maintenance, name='maintenance'),

    # HOME PAGE
    url(r'^$', views.index, name='index'),

    # /register/
    url(r'^register/$', check_recaptcha(views.register), name='register'),

    # /my_info/
    url(r'^my_info/$', views.my_info, name='my_info'),

    # /login/
    url(r'^login/$', views.login_main, name='login'),

    # /login_user/
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /logout_user/
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /<item_id>/detail/
    url(r'^(?P<item_id>[0-9]+)/detail/$', views.detail, name='detail'),

    # /post/
    url(r'^post/$', views.add_item, name='add_item'),

    # /my_posts/
    url(r'^my_posts/$', views.my_items, name='my_items'),

    # /<item_id>/update_post/
    url(r'^(?P<item_id>[0-9]+)/update_post/$', views.update_item, name='update_item'),

    # /<item_id>/delete_post/
    url(r'^(?P<item_id>[0-9]+)/delete_post/$', views.delete_item, name='delete_item'),

    # /<item_id>/homeless_again/
    url(r'^(?P<item_id>[0-9]+)/homeless_again/$', views.item_available, name='item_available'),

    # /<item_id>/adopted/
    url(r'^(?P<item_id>[0-9]+)/adopted/$', views.item_unavailable, name='item_unavailable'),

    # /terms/
    url(r'^terms/$', views.terms, name='terms'),

    # /about/
    url(r'^about/$', views.about, name='about'),

]
