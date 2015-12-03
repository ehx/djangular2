from django.contrib import admin
from .models import *

admin.site.register(Task)
admin.site.register(Organization)
admin.site.register(Client)
admin.site.register(UserClient)
admin.site.register(TaskComment)
admin.site.register(Todo)
admin.site.register(Module)
admin.site.register(Status)
admin.site.register(Urgency)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(UserProfile)