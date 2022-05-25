from hashlib import new
from click import command
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.mail import send_mail

from .forms import ContactForm, CommentForm
from .models import Choice, Question, Startpage_model, Blogpost, Comment


def startpage(request):
    Startpage_query = Startpage_model.objects.all()
    context = {"Startpage_query": Startpage_query}
    return render(request, "blog/startpage.html", context)


def poll(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "blog/poll.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "blog/detail.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "blog/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("blog:results", args=(question.id,)))


def blog(request):
    all_blogs = Blogpost.objects.order_by("-pub_date")
    most_viewed_blogs = Blogpost.objects.order_by("-view_counter")[:2]
    paginator = Paginator(all_blogs, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "all_blogs": all_blogs,
        "most_viewed_blogs": most_viewed_blogs,
        "page_obj": page_obj,
    }
    return render(request, "blog/blog.html", context)


def blogdetail(request, Blogpost_id):
    chosen_Blogpost = get_object_or_404(Blogpost, pk=Blogpost_id)
    most_viewed_blogs = Blogpost.objects.order_by("-view_counter")[:2]
    all_comments = Comment.objects.filter(blogpost_id=Blogpost_id)
    new_comment = ""

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blogpost_id = Blogpost_id
            new_comment.save()

    blog_object = Blogpost.objects.get(id=Blogpost_id)
    blog_object.view_counter = blog_object.view_counter + 1
    blog_object.save()

    context = {
        "form": form,
        "all_comments": all_comments,
        "blog_object": blog_object,
        "chosen_Blogpost": chosen_Blogpost,
        "most_viewed_blogs": most_viewed_blogs,
        "new_comment": new_comment,
    }
    return render(request, "blog/blogdetail.html", context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    context = {
        "question": question,
    }
    return render(request, "blog/results.html", context)


def contactpage(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            from_email = request.POST.get("from_email")
            captcha1 = request.POST.get("captcha")
            captcha = int(captcha1)
            if subject and message and from_email and captcha == 1:
                send_mail(subject, message, from_email, ["lanweilig11@googlemail.com"])
                return HttpResponseRedirect("response_email")
            else:
                form = ContactForm()

    context = {"form": form}
    return render(request, "blog/contactpage.html", context)


def response_email(request):
    context = {}
    return render(request, "blog/response_email.html", context)
