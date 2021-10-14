from django.db import models
from ckeditor.fields import RichTextField


class Blogeintrag(models.Model):
    title = models.CharField(max_length=200, default="")
    maintext  = RichTextField(null=True)
    previewtext = models.CharField(max_length=500, default="")
    sidetext = models.CharField(max_length=500, default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
            return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    
    def __str__(self):
        return self.choice_text
