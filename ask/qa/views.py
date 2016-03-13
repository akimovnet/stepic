from django.http import HttpResponse 
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from qa.models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def main(request):
    qs = Question.objects.all()
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

def question(request):
    return render_to_response('qa/', {})
