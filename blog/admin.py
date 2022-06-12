from django.contrib import admin

from .models import Question, Choice, Blogpost, Startpage_model, Comment


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Blogpost)
admin.site.register(Startpage_model)
admin.site.register(Comment)
