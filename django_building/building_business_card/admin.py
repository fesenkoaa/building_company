from django.contrib import admin
from .models import Contact, Project, OldProject, Vacancy, NewEmployee


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone', 'email', 'date')
    list_display_links = ('id',)


class ProjectsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'start', 'end', 'project_link')
    list_display_links = ('title',)
    search_fields = ('title',)


class OldProjectsAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'start', 'end')
    list_display_links = ('title',)
    search_fields = ('title',)


class VacancyAdmin(admin.ModelAdmin):

    list_display = ('id', 'position',)


class NewEmployeeAdmin(admin.ModelAdmin):

    list_display = ('id', 'position', 'first_name', 'last_name', 'phone')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(OldProject, OldProjectsAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(NewEmployee, NewEmployeeAdmin)
