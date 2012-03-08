# process of https://docs.djangoproject.com/en/1.3/intro/tutorial02/
# commented out lines were original lines of code from the tutorial,
# then have added and edited as the tutorial went on
from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

# admin.site.register(Poll)

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question']
	#fieldsets = [
	#(None, {'fields': ['question']}),
	#('Date information', {'fields': ['pub_date']})
	#]
	fieldsets = [
	(None, {'fields': ['question']}),
	('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

# admin.site.register(Choice)


admin.site.register(Poll, PollAdmin)