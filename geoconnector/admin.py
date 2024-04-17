from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Location, Element, Point, PointElement, ResourceLink, PointResourceLinkStatus


# Registering points and rendering in backoffice
@admin.register(Point)
class PointAdmin(LeafletGeoAdmin):
    pass


# Standard administration records
admin.site.register(Location)
admin.site.register(Element)
admin.site.register(PointElement)
admin.site.register(ResourceLink)
admin.site.register(PointResourceLinkStatus)
