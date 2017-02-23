from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    model = Post
    context_object_name = 'latest_posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-date_published')[:20]

def add_item(request, submitted_text):
    try:
        obtained_text = request.POST.get('submitted_text', False)
        if len(obtained_text) == 0:
            raise ValueError
        p = Post(post_text=obtained_text, date_published=timezone.now())
        p.save()
        #return HttpResponse("You've submitted this text: %s" % obtained_text)
        return HttpResponseRedirect(reverse('posts:index'))
    except ValueError:
        return HttpResponseRedirect(reverse('posts:index'))

def remove_item(request, post_id):
    item = Post.objects.get(id=post_id)
    item.delete()
    return HttpResponseRedirect(reverse('posts:index'))

