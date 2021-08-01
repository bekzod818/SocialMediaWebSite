from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from .models import Post
from .forms import PostForm, CommentForm


class PostListView(ListView, FormView):
    model = Post
    context_object_name = 'posts'
    template_name = 'social/post_list.html'
    ordering = ['-created_on']
    form_class = PostForm

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'posts': posts,
            'form': form
        }
        return render(request, 'social/post_list.html', context)


class PostDetailView(DetailView, FormView):
    model = Post
    template_name = 'social/post-detail.html'
    form_class = CommentForm