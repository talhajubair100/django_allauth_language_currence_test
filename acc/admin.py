from os import POSIX_FADV_DONTNEED
from django.contrib import admin
from .models import EmployeUser, CompanyUser, Post
# Register your models here.


admin.site.register(CompanyUser)
admin.site.register(EmployeUser)
admin.site.register(Post)

