# Adding Endpoints

## Procedure

### Add urls for the app

Import `include` from `django.urls` and add the paths for my-app to `urlpatterns`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
```

### Add test code

### Add endpoint

## References

1. [Let’s build an API with Django REST Framework — Part 1](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-32fcf40231e5)
2. [Let’s build an API with Django REST Framework — Part 2](https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-part-2-cfb87e2c8a6c)
