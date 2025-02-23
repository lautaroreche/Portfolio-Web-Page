from django.contrib import admin
from .models import Project, Technology, WorkExperience


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tags', 'image', 'repo_url')
    search_fields = ('id', 'title', 'tags', 'image', 'repo_url')


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fields = ('id', 'name', 'image')


class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'location', 'start_date', 'end_date', 'image', 'description')
    search_fields = ('id', 'title', 'company', 'location', 'start_date', 'end_date', 'image', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
