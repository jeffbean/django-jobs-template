from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework import serializers, viewsets

from boil_project.api_urls import router


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router.register(r'users', UserViewSet)

admin.autodiscover()


class GrinderIndexView(TemplateView):
    template_name = 'index.html'


urlpatterns = [
    url(r'^$', GrinderIndexView.as_view(), name='index'),
    url(r'^lab/', include('boil_app.urls', namespace='lab')),
    url(r'^api/', include(router.urls, namespace='api')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),

    # adds the auth urls all nice and simple
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
