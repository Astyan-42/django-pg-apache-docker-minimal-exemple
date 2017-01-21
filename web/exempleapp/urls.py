from django.conf.urls import url
from exempleapp.views import ExempleListView, ExempleCreateView

urlpatterns = [url(r'^$', ExempleListView.as_view(), name='exemplelist'),
               url(r'^create$', ExempleCreateView.as_view(), name='exemplecreate')]
