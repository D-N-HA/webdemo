from django.shortcuts import render, get_object_or_404
from .models import Story

def story_list(request):
    stories = Story.objects.all()
    return render(request, 'stories/index.html', {'stories': stories})

def story_detail(request, slug):
    story = get_object_or_404(Story, slug=slug)
    story.views += 1
    story.save()
    return render(request, 'stories/detail.html', {'story': story})

