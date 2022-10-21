# django-redis-init

Just a simple django app with planes

## Requirements

1. python 3.9
2. poetry - install poetry using ```pip install poetry```
3. Docker installed

## How To

1. Navigate to django-redis-init directory
2. Install requirements: ```poetry install```
3. Start redis using docker using this command ```bash run_redis.sh```
4. Start django app: ```python manage.py runserver```

##### NOTE: no need to run migrations for these example


## Endpoint:

This app just have two endpoints:
1. admin/ - default admin page and
2. planes/ - that accepts GET, PUT and POST methods (for now)


#### Get all planes
``` commandline
curl \
    --header "Content-Type: application/json" \
    --request GET \
    http://localhost:8000/planes/

```


#### Create plane

``` commandline
curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data '{"model_key":"xyz","plane_name":"Plane xyz","plane_active": true}' \
    http://localhost:8000/planes/

```


#### Edit Plane
``` commandline
curl \
    --header "Content-Type: application/json" \
    --request PUT \
    --data '{"model_key":"xyz","plane_name":"PLANE XYZ"}' \
    http://localhost:8000/planes/

```
###### NOTE: PUT request must include ```model_key``` in data

#### NOTE: Don't forget to kill/stop docker container when finished
