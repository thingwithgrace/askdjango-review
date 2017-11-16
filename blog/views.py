from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html')


def temp_study(request):
    return render(request, 'blog/temp_study.html')