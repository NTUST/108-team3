from __future__ import unicode_literals
from .models import Photo,Group,Quiz
from django.contrib import admin

class PhotoAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp"]

	class Meta:
		model = Photo

class GroupAdmin(admin.ModelAdmin):
	list_display = ('vid', 'name', 'description', 'quizlink', 'descriptionlink')

	class Meta:
		model = Group

class QuizAdmin(admin.ModelAdmin):
	list_display = ('question', 'ansA', 'ansB', 'ansC', 'real_ans')

	class Meta:
		model = Quiz

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Group)
admin.site.register(Quiz)
from django.contrib import admin