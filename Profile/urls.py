from django.urls import path, include, re_path

from Profile.views import ProfileTable, ProfileTableDetail

urlpatterns = [
    re_path(r'^user/$',ProfileTable.as_view()),
    re_path(r'^user/(?P<pk>\d+)',ProfileTableDetail.as_view()),
] 