from django.conf.urls import url
from showusers.views import UserListView

urlpatterns = [url(r'^$', UserListView.as_view(), name='userlist')]
