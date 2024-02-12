from django.contrib import admin
from menu.models import Menu, Item


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    fieldsets = (
        ('Add new item', {
            'description': "Parent should be a menu or item",
            'fields': (('menu', 'parent'), 'title', 'slug')
            }),
            )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')