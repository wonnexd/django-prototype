from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.startpage, name="startpage"),
    path("poll", views.poll, name="poll"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("blog", views.blog, name="blog"),
    path("<int:Blogpost_id>", views.blogdetail, name="blogdetail"),
    path("contactpage", views.contactpage, name="contactpage"),
    path("response_email", views.response_email, name="response_email"),
    path("bewerbung", views.bewerbung, name="bewerbung"),
]
