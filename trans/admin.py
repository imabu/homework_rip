from django.contrib import admin
from trans import models


# user:admin pass:mfu1mfumfu
class TransAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'comment', 'summ')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'name')

admin.site.register(models.TransactsModel, TransAdmin)
admin.site.register(models.TypeTransactModel, TypeAdmin)