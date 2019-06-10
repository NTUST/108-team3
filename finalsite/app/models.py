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