from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

   

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']

admin.site.register(Choice) 
admin.site.register(Poll, PollAdmin)

