from django.contrib import admin
from MyApp.models import Emp

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=['id','empno','empname','empsal','empadd']
admin.site.register(Emp,EmpAdmin)