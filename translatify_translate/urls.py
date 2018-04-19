from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from translatify_translate import views

urlpatterns = [
    url(r'^phrases/$', views.PhraseList.as_view()),
    url(r'^phrases/(?P<pk>[0-9]+)/$', views.PhraseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
