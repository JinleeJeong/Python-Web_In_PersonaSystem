import this

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from facebook.models import Article, Comment

# Create your views here.

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles':articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and  request.POST['password'] != '':
            new_comment =Comment.objects.all()(
                article=article,
                author=request.POST.get('author'),
                text=request.POST.get('text'),
                password=request.POST.get('password'),
            )
        return redirect(f'/feed/{article.pk}')
    return render(request, 'detail_feed.html', {'feed' : article})

# def page(request):
#     page = Page.objects.all()
#     return render(request, 'page.html', {'pages':page})

def new_feed(request):
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password'],
            )
        return redirect('/')
    return render(request, 'new_feed.html')

def new_comment_feed(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['author'] != '' and request.POST['text'] != '' and request.POST['password'] != '':
            new_comment = Comment.objects.create(
                article=article,
                author=request.POST['author'],
                text=request.POST['text'],
                password=request.POST['password'],
            )
        return redirect(f'/feed/{ article.pk }')
    return render(request, 'new_comment_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/')
        else:
            return redirect('/fail/')
    return render(request, 'remove_feed.html', {'feed':article})

def remove_comment_feed(request, pk):
    article = Article.objects.get(pk=pk)
    comment = Comment.objects.all()
    if request.method == 'POST':
        if(request.POST):
            comment.delete()
            return redirect('/')
        else:
            return redirect('/fail/')

    return render(request, 'remove_comment_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail/')
    return render(request, 'edit_feed.html', {'feed':article})

def fail(request):
    return render(request, 'fail.html')


# def play(request):
#     return render(request, 'play.html' )
# count = 0
# def play_two(request):
#     JinleeJeong = '진리'
#     global count
#     count = count + 1
#     diary = ['월요일', '화요일', '수요일']
#     return render(request, 'play_two.html',{ 'name' : JinleeJeong, 'cnt' : count, 'diary' : diary})
#
# def profile(request):
#     return render(request, 'Daniel/profile.html')
#
# def event(request):
#     JinleeJeong = '진리'
#     global count
#     count = count + 1
#     if count == 7:
#         lottery = '당첨!'
#     else:
#         lottery = '꽝...'
#     return render(request, 'event.html', { 'name' : JinleeJeong, 'cnt' : count, 'lottery' : lottery})

