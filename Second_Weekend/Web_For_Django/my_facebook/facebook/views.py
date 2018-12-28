from django.shortcuts import render

# Create your views here.
def play(request):

    return render(request, 'play.html' )

def play_two(request):
    JinleeJeong = '진리'
    return render(request, 'play_two.html',{ 'name' : JinleeJeong })