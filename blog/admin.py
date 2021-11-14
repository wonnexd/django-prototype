from django.contrib import admin

from .models import Question, Choice, Blogeintrag, Startseite


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Blogeintrag)
admin.site.register(Startseite)