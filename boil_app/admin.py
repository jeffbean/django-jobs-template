from django.contrib import admin

from boil_app.models import Node


class PodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'owner', 'ip_address')
    search_fields = ('name', 'ip_address',)


class NodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'uuid', 'hostname',)
    search_fields = ('uuid', 'ip_address', 'hostname',)


admin.site.register(Node, NodeAdmin)
