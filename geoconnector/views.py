from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Location, Element, Point, PointElement, ResourceLink, PointResourceLinkStatus

from .serializer import LocationSerializer, ElementSerializer, PointSerializer, PointElementSerializer, ResourceLinkSerializer, PointResourceLinkStatusSerializer


class LocationsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing location instances.
    Uses authentication to ensure only authenticated users can access the method.
    Filters are provided to refine search results based on location attributes.
    """
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'type', 'location_name',]


class ElementsViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling requests for element data.
    This viewset supports authenticated users only and includes basic filtering capabilities.
    """
    permission_classes = [IsAuthenticated]
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'element_name',]


class PointsViewSet(viewsets.ModelViewSet):
    """
    Manages creating, reading, updating, and deleting points.
    Includes a related field optimization using `select_related` to improve performance.
    """
    permission_classes = [IsAuthenticated]
    queryset = Point.objects.select_related('location').all()
    serializer_class = PointSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'location', 'point_type', 'point_name',]


class PointElementsViewSet(viewsets.ModelViewSet):
    """
    Provides a mechanism for clients to interact with point-element data.
    Optimized to prefetch related data for efficiency.
    """
    permission_classes = [IsAuthenticated]
    queryset = PointElement.objects.select_related('point', 'element').all()
    serializer_class = PointElementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'point', 'element',]


class ResourceLinksViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides access to resource link data.
    Filters allow for narrowing down results based on resource link characteristics.
    """
    permission_classes = [IsAuthenticated]
    queryset = ResourceLink.objects.all()
    serializer_class = ResourceLinkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'resource_link_name',]
    

class PointResourceLinkStatusesViewSet(viewsets.ModelViewSet):
    """
    Handles API requests related to the status of resource links to points.
    Includes custom methods to enhance default list actions with additional geographical data.
    """
    permission_classes = [IsAuthenticated]
    queryset = PointResourceLinkStatus.objects.prefetch_related('linked_points', 'linked_resources').all()
    serializer_class = PointResourceLinkStatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'linked_points', 'linked_resources', 'status',]

    def list(self, request):
        """
        Overridden method to provide custom data structure in the response that includes
        latitude and longitude details for linked points.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        data = []
        for item in serializer.data:
            linked_points_data = []
            for point_id in item['linked_points']:
                try:
                    point = Point.objects.get(id=point_id)
                    latitude = point.geolocation.y
                    longitude = point.geolocation.x
                    linked_points_data.append({'latitude': latitude, 'longitude': longitude})
                except Point.DoesNotExist:
                    pass  # If a point does not exist, it is simply ignored in the response.

            # Append the overall data for each item including linked points coordinates.
            data.append({
                'id': item['id'],
                'created': item['created'],
                'modified': item['modified'],
                'active': item['active'],
                'status': item['status'],
                'linked_points': linked_points_data,
                'linked_resources': item['linked_resources'],
            })

        return Response(data)
