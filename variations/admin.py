from django.contrib import admin
from .models import Variations, VariationsCategory

# Register your models here.


admin.site.register(VariationsCategory)
admin.site.register(Variations)


