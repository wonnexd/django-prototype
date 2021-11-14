from typing import ContextManager
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.mail import BadHeaderError, send_mail

from .forms import ContactForm 
from .models import Blogeintrag, Choice, Question, Startseite

def home(request):
    startseite_query = Startseite.objects.all()
    context = {
        'startseite_query': startseite_query
    }
    return render(request, 'blog/home.html', context)

def umfrage(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'blog/umfrage.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'blog/results.html', {'question': question})

def blog(request):
    latest_blog = Blogeintrag.objects.order_by('-pub_date')
    paginator = Paginator(latest_blog, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'latest_blog': latest_blog,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blog.html', context)

def blogdetail(request, blogeintrag_id):
    latest_blog = Blogeintrag.objects.order_by('-pub_date')
    blogeintrag = get_object_or_404(Blogeintrag, pk=blogeintrag_id)
    context = {
        'blogeintrag': blogeintrag,
        'latest_blog': latest_blog,      
    }
    return render(request, 'blog/blogdetail.html', context)

def contactpage(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            from_email = request.POST.get('from_email')
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['lanweilig11@googlemail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/polls/contactpage')
            else:
                form = ContactForm()
                return HttpResponse('Make sure all fields are entered and valid.')

    context = {'form': form}
    return render(request, 'blog/contactpage.html', context)


