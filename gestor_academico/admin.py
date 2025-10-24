from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'promedio_display')
    search_fields = ('matricula', 'nombre')

    def promedio_display(self, obj):
        return obj.promedio()
    promedio_display.short_description = 'Promedio'
