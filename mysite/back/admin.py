from django.contrib import admin

# Register your models here.

from back.models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ('name','id_num')

admin.site.register(Form,FormAdmin)
