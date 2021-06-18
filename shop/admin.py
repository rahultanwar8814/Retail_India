from django.contrib import admin
from .models import item, order, item2 ,help

admin.site.register(item)
admin.site.register(item2)
admin.site.register(order)
admin.site.register(help)
# Register your models here.
