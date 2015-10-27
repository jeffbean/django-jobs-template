from rest_framework import routers
from boil_app.views import PodAPIViewSet, JobsAPIViewSet, AutomationAPIViewSet
from boil_app.views import NodeAPIViewSet

router = routers.DefaultRouter()

router.register(r'pods', PodAPIViewSet, base_name='pod')
router.register(r'nodes', NodeAPIViewSet, base_name='node')
router.register(r'jobs', JobsAPIViewSet, base_name='job')
router.register(r'auto', AutomationAPIViewSet, base_name='auto')
