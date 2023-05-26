
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Song, Comment

def song_detail(request, post_id):
    post = get_object_or_404(Song, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

def add_comment(request, post_id):
    post = get_object_or_404(Song, pk=post_id)
    if request.method == 'POST':
        content = request.Song['content']
        user = request.user
        comment = Comment.objects.create(post=post, user=user, content=content)
        # Дополнительные действия, если необходимо
    return redirect('post_detail', post_id=post_id)


