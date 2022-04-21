from django.contrib import admin

# Register your models here.
from song import models
# Register your models here.
admin.site.register(models.Songs)
