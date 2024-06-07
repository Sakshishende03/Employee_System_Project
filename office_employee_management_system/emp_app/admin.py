from django.contrib import admin
from emp_app.models import Employee,Department,Role

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','dept','salary','bonus','role','phone','hire_date']
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department)
admin.site.register(Role)
