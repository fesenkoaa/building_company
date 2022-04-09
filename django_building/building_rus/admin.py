from django.contrib import admin
from .models import RuContact, RuProject, RuOldProject, RuVacancy, RuNewEmployee


class RuContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone', 'email', 'date')
    list_display_links = ('id',)


class RuProjectsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'start', 'end', 'project_link')
    list_display_links = ('title',)
    search_fields = ('title',)


class RuOldProjectsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'start', 'end')
    list_display_links = ('title',)
    search_fields = ('title',)


class RuVacancyAdmin(admin.ModelAdmin):

    list_display = ('id', 'position',)


class RuNewEmployeeAdmin(admin.ModelAdmin):

    list_display = ('id', 'position', 'first_name', 'last_name', 'phone')


# admin.site.register(RuContact, RuContactAdmin)
admin.site.register(RuProject, RuProjectsAdmin)
admin.site.register(RuOldProject, RuOldProjectsAdmin)
admin.site.register(RuVacancy, RuVacancyAdmin)
# admin.site.register(RuNewEmployee, RuNewEmployeeAdmin)
