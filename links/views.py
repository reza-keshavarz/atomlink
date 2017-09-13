from django.shortcuts import render
from .models import Link, AdLink


def show_all(request):
    links = Link.objects.all()
    ad = AdLink.objects.get()
    return render(request, 'links/links.html', {'links': links, 'ad': ad})
