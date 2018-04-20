from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from translatify_translate import views

urlpatterns = [
    url(r'^phrases/$', views.TranslatedPhraseList.as_view()),
    url(r'^phrases/(?P<pk>[0-9]+)/$', views.TranslatedPhraseDetail.as_view()),
    url(r'^translate/$', views.PhraseRequestList.as_view()),
    url(r'^translate/(?P<pk>[0-9]+)/$', views.PhraseRequestDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
