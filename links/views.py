from django.shortcuts import render

from django.contrib.auth.models import User

from .models import Link, AdLink, Profile


def show_all(request):
    links = Link.objects.all()
    ad = AdLink.objects.get()
    return render(request, 'links/links.html', {'links': links, 'ad': ad})


def links_by_user(request, username):
    user = User.objects.get(username=username)
    links = Link.objects.filter(author=user)
    ad = AdLink.objects.get()
    user_info = Profile.objects.get(user=user)

    return render(request, 'links/links.html', {'links': links, 'ad': ad, 'user_info': user_info})
