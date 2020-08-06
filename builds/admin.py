from django.contrib import admin
from .models import Bb
from .models import Rubric

# Register your models here.


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'char1', 'items1', 'char2', 'items2', 'char3',
                    'items3', 'char4', 'items4', 'published')
    # list_display_links = ('title', 'char1', 'items1', )
    search_fields = ('title', 'rubric', 'char1', 'items1', 'char2', 'items2', 'char3',
                    'items3', 'char4', 'items4',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)