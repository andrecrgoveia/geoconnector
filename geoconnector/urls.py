from django.urls import include, path

from rest_framework import routers

from . import views

from .views import LocationsViewSet, ElementsViewSet, PointsViewSet, PointElementsViewSet, ResourceLinksViewSet, PointResourceLinkStatusesViewSet


# Create a router object which will handle all the URL routing for our API.
router = routers.DefaultRouter()

# Register several viewsets with the router.
router.register(str('locations'), views.LocationsViewSet, basename='locations')
router.register(str('elements'), views.ElementsViewSet, basename='elements')
router.register(str('points'), views.PointsViewSet, basename='points')
router.register(str('pointelements'), views.PointElementsViewSet, basename='pointelements')
router.register(str('resourcelinks'), views.ResourceLinksViewSet, basename='resourcelinks')
router.register(str('pointresourcelinkstatuses'), views.PointResourceLinkStatusesViewSet, basename='pointresourcelinkstatuses')


urlpatterns = [
    path('', include(router.urls)), # Include all URLs from the router in the urlpatterns list.
]
