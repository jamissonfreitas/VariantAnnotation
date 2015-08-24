from django.contrib import admin

# Register your models here.
from .models import VCF
from .models import Document

admin.site.register(VCF)
admin.site.register(Document)
