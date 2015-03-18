# Simple Property Manager

This is a simple property manager with create and edit functionality.

Simple Property Manager uses [Stylish Portfolio](http://startbootstrap.com/template-overviews/stylish-portfolio/), a stylish, responsive page [Bootstrap](http://getbootstrap.com/) portfolio theme with off canvas navigation and smooth scrolling through content sections. 

## Requirements

* Python 2.7
* [GeoDjango](https://docs.djangoproject.com/en/1.7/ref/contrib/gis/)
* Libraries in requirements.txt 


This project uses PostgreSQL with PostGIS, PostGIS adds geographic object support to PostgreSQL, turning it into a spatial database. GEOS, PROJ.4 and GDAL should be installed prior to building PostGIS. [Oficial Documentation](https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/postgis/).


## Installation
We recomend using a virtual envorinment:

	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt

	
### Tipical Steps

	python manage.py migrate
	python manage.py collectstatic
	python manage.py createsuperuser
	
	python manage.py loaddata example_data.json
	
	python manage.py runserver

