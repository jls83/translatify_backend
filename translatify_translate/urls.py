from django.conf.urls import url
from translatify_translate import views

urlpatterns = [
    url(r'^phrases/$', views.phrase_list),
    url(r'^phrases/(?P<pk>[0-9]+)/$', views.phrase_detail),
]
