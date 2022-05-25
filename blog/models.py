from operator import mod
from pyexpat import model
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from ckeditor.fields import RichTextField


class Blogpost(models.Model):
    title = models.CharField(max_length=200, default="")
    maintext = RichTextField(null=True)
    previewtext = RichTextField(max_length=1000, null=True)
    sidetext = RichTextField(max_length=400, null=True)
    pub_date = models.DateField("date published")
    view_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blogpost = models.ForeignKey("Blogpost", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    pub_date = models.DateField("date published", null=True, auto_now_add=True)
    captcha = models.IntegerField()


class Startpage_model(models.Model):
    inhalt = RichTextField(null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
