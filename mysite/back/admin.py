from django.contrib import admin

# Register your models here.

from back.models import Form,Posts

class FormAdmin(admin.ModelAdmin):
    list_display = ('name','id_num')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id_var', 'title_var', 'desc_var')



admin.site.register(Form,FormAdmin)
admin.site.register(Posts,PostAdmin)
