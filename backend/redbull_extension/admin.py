from django.contrib import admin
from .models import Club, Person

# do all the models need to be registered? or is there ever a case where there is a model that wouldn't need to be registered?
admin.site.register(Club)
admin.site.register(Person)