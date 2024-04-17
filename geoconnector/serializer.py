from rest_framework import serializers

from .models import Location, Element, Point, PointElement, ResourceLink, PointResourceLinkStatus


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Location model.
    """
    class Meta:
        model = Location
        fields = '__all__'


class ElementSerializer(serializers.ModelSerializer):
    """
    Serializer for the Element model.
    """
    class Meta:
        model = Element
        fields = '__all__'


class PointSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.location_name', read_only=True)
    """
    Serializer for the Point model with additional read-only field 'location_name'.
    This field is included to enhance API usability by providing related location name directly.
    """
    class Meta:
        model = Point
        fields = '__all__'


class PointElementSerializer(serializers.ModelSerializer):
    point_name = serializers.CharField(source='point.point_name', read_only=True)
    element_name = serializers.CharField(source='element.element_name', read_only=True)
    """
    Serializer for the PointElement model. This serializer enhances object representation by including
    the names of associated Point and Element directly using read-only fields.
    """
    class Meta:
        model = PointElement
        fields = '__all__'


class ResourceLinkSerializer(serializers.ModelSerializer):
    """
    Serializer for the ResourceLink model.
    """
    class Meta:
        model = ResourceLink
        fields = '__all__'


class PointResourceLinkStatusSerializer(serializers.ModelSerializer):
    linked_resources = serializers.SerializerMethodField()
    """
    Serializer for the PointResourceLinkStatus model. It includes custom methods to retrieve linked
    points and resources, providing a richer API response that includes relevant associated data.
    """
    class Meta:
        model = PointResourceLinkStatus
        fields = ['id', 'created', 'modified', 'active', 'status', 'linked_points', 'linked_resources']

    def get_linked_points(self, obj):
        """
        Custom method to retrieve names of linked points. Returns a list of names, which
        are easier to use in client applications than raw IDs.
        """
        points = obj.linked_points.all()
        return [point.point_name for point in points]

    def get_linked_resources(self, obj):
        """
        Custom method to retrieve names of linked resources. Similar to get_linked_points, this method
        enhances usability by providing resource names.
        """
        resources = obj.linked_resources.all()
        return [resource.resource_link_name for resource in resources]
