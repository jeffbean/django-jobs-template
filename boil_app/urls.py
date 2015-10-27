from django.conf.urls import url

from boil_app.views import NodeListView, NodeDetailView


urlpatterns = [
    url(r'^nodes/$', NodeListView.as_view(), name='node-list'),
    url(r'^nodes/(?P<slug>[\w\-]+)/$', NodeDetailView.as_view(), name="node-detail"),
]