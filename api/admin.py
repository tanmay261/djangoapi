from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

# LEARN
# To display only specific columns for Companies
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')


# LEARN
# To display only specific columns for Employees
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','position','company')

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
