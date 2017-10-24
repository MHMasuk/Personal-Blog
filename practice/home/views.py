from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView,ListView, CreateView, UpdateView, DeleteView
from . import models
from home.models import Post
from home.forms import PostFrom
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'home/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContractView(TemplateView):
    template_name = 'home/contract.html'


class CreatePostView(CreateView):
    # redirect_field_name = 'home/post_list'
    form_class = PostFrom
    model = Post


class UpdatePostView(UpdateView):
    form_class = PostFrom
    model = Post

class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')