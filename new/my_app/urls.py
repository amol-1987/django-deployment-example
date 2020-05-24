from django.conf.urls import url
from my_app import views

urlpatterns=[
    # url(r'^amol/', views.help, name='help'),
    url(r'^$', views.help, name='help')
]
