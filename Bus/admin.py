from django.contrib import admin
from .models import User
from .models import Station
from .models import News
from .models import SiteRoute
from .models import Route

# Register your models here.

admin.site.register(User)
admin.site.register(SiteRoute)
admin.site.register(Station)
admin.site.register(News)
admin.site.register(Route)