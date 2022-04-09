from django.contrib import admin
from .models import EnContact, EnProject, EnOldProject, EnVacancy, EnNewEmployee


class EnContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone', 'email', 'date')
    list_display_links = ('id',)


class EnProjectsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'start', 'end', 'project_link')
    list_display_links = ('title',)
    search_fields = ('title',)


class EnOldProjectsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'start', 'end')
    list_display_links = ('title',)
    search_fields = ('title',)


class EnVacancyAdmin(admin.ModelAdmin):

    list_display = ('id', 'position',)


class EnNewEmployeeAdmin(admin.ModelAdmin):

    list_display = ('id', 'position', 'first_name', 'last_name', 'phone')


# admin.site.register(EnContact, EnContactAdmin)
admin.site.register(EnProject, EnProjectsAdmin)
admin.site.register(EnOldProject, EnOldProjectsAdmin)
admin.site.register(EnVacancy, EnVacancyAdmin)
# admin.site.register(EnNewEmployee, EnNewEmployeeAdmin)
