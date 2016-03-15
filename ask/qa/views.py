from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def main(request):
    qs = Question.objects.order_by('-id')
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render_to_response('qa/list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def popular(request):
    qs = Question.objects.order_by('-rating')
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, 10)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render_to_response('qa/list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def question(request, id):
    try:
        question = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form._user_id = request.user_id
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(answer.question.get_url())
    else:
        form = AnswerForm()
    return render(request, 'qa/question.html', {
        'question': question,
        'form': form,
    })

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user_id = request.user_id
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {
        'form': form,
    })

# @require_POST
# def answer(request):
#     form = AnswerForm(request.POST)
#     if form.is_valid():
#         answer = form.save()
#         return HttpResponseRedirect(answer.question.get_url())
#     return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #request.session.create()
            request.session['user'] = user.id
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {
        'form': form,
    })

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user != None:
                request.session['user'] = user.id
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {
        'form': form,
    })
