from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User 
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from .models import Post


class PostList(ListView):
    model = Post 
    template_name = 'blog_app/all_posts.html'
    context_object_name = 'list_of_posts'


class PostsByUser(PostList):
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetails(DetailView):
    model = Post 
    template_name = 'blog_app/post_details.html'
    context_object_name = 'post'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content']
    template_name = 'blog_app/create_post.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('blog:all_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Added new post: {form.instance.title}')
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']
    template_name = 'blog_app/edit_post.html'
    login_url = reverse_lazy('users:login')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        post = self.get_object()
        return reverse('blog:post_details', kwargs={'pk': post.pk})

    def form_valid(self, form):
        form.instance.date_last_edited = timezone.now()
        messages.success(self.request, f'Edited post: {form.instance.title}')
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    template_name = 'blog_app/delete_post.html'
    success_url = reverse_lazy('blog:all_posts')
    login_url = reverse_lazy('users:login')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
