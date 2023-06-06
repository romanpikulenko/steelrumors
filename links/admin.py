from django.contrib import admin

from links.models import Link, Vote

# Register your models here.
admin.site.register(Link)
admin.site.register(Vote)
