from django.conf.urls import url
from . import views

urlpatterns=[
    url('$',views.welcome,name='welcome'),
    url('^###/$',views.wholegallery,name='allsnaps'),
    url('^search/',views.search_results, name='search_results')
]