from django.contrib import admin

from ads.models import Category, Ad, User, Location#, Media

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(User)
admin.site.register(Location)
# admin.site.register(Media)