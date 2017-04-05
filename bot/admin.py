# from django.contrib import admin
#
# from .models import Command, Response, Unit, Session, Activity
#
# admin.site.register(Command)
# admin.site.register(Response)
# admin.site.register(Unit)
# admin.site.register(Session)
# admin.site.register(Activity)


from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import Node

admin.site.register(Node, DraggableMPTTAdmin, MPTTModelAdmin)