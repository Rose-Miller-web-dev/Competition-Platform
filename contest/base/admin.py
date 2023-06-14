from django.contrib import admin
from .models import Competition, Topic, Award
# Register your models here.

admin.site.register(Topic)
admin.site.register(Award)
admin.site.register(Competition)
