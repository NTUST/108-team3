# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Photo(models.Model):
	title = models.CharField(max_length=200)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	image = models.ImageField(null=False, blank=False, width_field="width", height_field="height")
	context = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	link = models.CharField(max_length=3000)

	def __str__(self):
		return self.context
	def __str__(self):
		return self.title
	def __str__(self):
		return self.link

	class Meta:
		ordering = ["-timestamp"]

class Group(models.Model):
	vid = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	description = models.TextField()
	quizlink = models.CharField(max_length=200)
	descriptionlink = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Quiz(models.Model):
	question = models.CharField(max_length=1000)
	ansA = models.CharField(max_length=200)
	ansB = models.CharField(max_length=200)
	ansC = models.CharField(max_length=200)
	real_ans = models.CharField(max_length=200)
	vid = models.ForeignKey('Group',on_delete=models.CASCADE)

	def __str__(self):
		return self.question


