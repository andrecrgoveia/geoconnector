# GeoConnector API
Author: André Castelo

## Description

The GeoConnector API is a service that manages geospatial information, allowing the storage and interconnection of points, elements and resources associated with specific locations. The API requires PostgreSQL as the main database, with the PostGIS extension enabled to support advanced geospatial functionalities. I chose to use Docker Compose to quickly set up a PostgreSQL instance with PostGIS. Key features include:
- CRUD for locations.
- CRUD for elements.
- CRUD for geographic points.
- CRUD for elements that belong to a point.
- CRUD for a resource link.
- CRUD for resource link status between points.


## Technologies and tools used
- Python3.x
- Django
- Django REST Framework
- PostgreSQL
- PostGIS
- Docker
- Docker Compose

## Database relations
![Database relations](https://raw.githubusercontent.com/andrecrgoveia/geoconnecor-api/media/db_relations.png)


## How to run the project?
Soon!