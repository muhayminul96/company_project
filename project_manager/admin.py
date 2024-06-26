from django.contrib import admin
from .models import User, Project, ProjectMember, Task, Comment

# Register your models here.


admin.site.register(User)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Task)
admin.site.register(Comment)
