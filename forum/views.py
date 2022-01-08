from django.shortcuts import render

def forum(request):
    posts = [
        {"title": "THis is the TItle", "body": "This is the body", "date": "this is the date"},
        {"title": "THis is the TItle", "body": "This is the body", "date": "this is the date"},
        {"title": "THis is the TItle", "body": "This is the body", "date": "this is the date"}
        ]

    context = {'posts': posts}
    return render(request, 'forum/forum.html', context)