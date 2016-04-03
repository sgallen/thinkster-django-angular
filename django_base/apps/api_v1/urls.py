from django.conf.urls import include, url

from rest_framework import routers

from .views import AccountViewSet


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
]
