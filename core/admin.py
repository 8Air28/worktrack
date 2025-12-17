from django.contrib import admin
from .models import WorkCategory, Tag, WorkLog

admin.site.register(WorkCategory)
admin.site.register(Tag)
admin.site.register(WorkLog)
