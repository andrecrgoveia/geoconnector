from django.db import models
from django.contrib.gis.db import models


class Base(models.Model):
    """Base model with common fields."""

    created = models.DateField('Created', auto_now_add=True)  # Immutable after creation
    modified = models.DateTimeField('Modified', auto_now=True)  # Automatically updated whenever the record is modified
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Location(Base):
    """Model to represent location types."""

    type = models.CharField('Type', max_length=250, blank=False, null=False)
    location_name = models.CharField('Location Name', max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return f'Type: {self.type}, Name: {self.location_name}'


class Element(Base):
    """Model to represent an element associated with a point."""

    element_name = models.CharField('Element Name', max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Element'
        verbose_name_plural = 'Elements'

    def __str__(self):
        return self.element_name


class Point(Base):
    """Model to represent a point."""

    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False, related_name='points')
    point_type = models.CharField('Point Type', max_length=250, blank=False, null=False)
    point_name = models.CharField('Point Name', max_length=250, blank=True, null=True, unique=True)
    geolocation = models.PointField(blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Point'
        verbose_name_plural = 'Points'

    def __str__(self):
        return f'Name: {self.point_name} - Latitude: {self.geolocation.y}, Longitude: {self.geolocation.x}'


class PointElement(Base):
    """Model to represent point element status."""

    point = models.ForeignKey(Point, on_delete=models.CASCADE, blank=False, null=False, related_name='point_elements')
    element = models.ForeignKey(Element, on_delete=models.CASCADE, blank=False, null=False, related_name='point_elements')

    class Meta:
        verbose_name = 'Point Element'
        verbose_name_plural = 'Point Elements'

    def __str__(self):
        return f'Point: {self.point.point_name}, Element: {self.element.element_name}'


class ResourceLink(Base):
    """Model to represent resource links between points."""

    resource_link_name = models.CharField('Resource Link Name', max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'Resource Link'
        verbose_name_plural = 'Resource Links'

    def __str__(self):
        return self.resource_link_name


class PointResourceLinkStatus(Base):
    """Model to represent the status of resource links associated with points."""

    POINT_STATUS_CHOICES = [
        ('Completed', 'Completed'),
        ('Incomplete', 'Incomplete'),
    ]

    linked_points = models.ManyToManyField(Point, blank=False, related_name='points')
    linked_resources = models.ManyToManyField(ResourceLink, blank=False, related_name='resources')
    status = models.CharField(max_length=20, choices=POINT_STATUS_CHOICES, default='Incomplete')

    class Meta:
        verbose_name = 'Point Resource Link Status'
        verbose_name_plural = 'Point Resource Link Statuses'

    def __str__(self):
        return f"Points: {', '.join(str(link) for link in self.linked_points.all())} - Resource Links: {', '.join(str(link) for link in self.linked_resources.all())} - Status: {self.status}"
