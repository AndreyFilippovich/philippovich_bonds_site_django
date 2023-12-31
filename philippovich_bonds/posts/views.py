from typing import Any, Dict
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.contrib.auth import logout, login

from .forms import *
from .models import *
from .utils import *


class PostsHome(DataMixin, ListView):
    model = Posts
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Posts.objects.filter(is_published=True).select_related('cat')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'posts/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Posts
    template_name = 'posts/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Posts.objects.filter(is_published=True).select_related('cat')


class SearchResultsView(DataMixin, ListView):
    model = Posts
    template_name = 'posts/search_results.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Posts.objects.filter(
            Q(title__icontains=query)
        )
        return object_list



class PostsCategory(DataMixin, ListView):
    model = Posts
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Posts.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title="Категория - " + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


def page_not_found(request, exception):
    return render(request, 'posts/404.html', {'path': request.path, 'title': 'Ошибка'}, status=404)








#def about(request):
#    contact_list = Posts.objects.all()
#    paginator = Paginator(contact_list, 3)
#
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#    return render(request, 'posts/about.html', {'page_obj': page_obj, 'menu': menu, 'title': "О сайте"})


#class ContactFormView(DataMixin, FormView):
#    form_class = ContactForm
#    template_name = 'posts/contact.html'
#    success_url = reverse_lazy('home')

#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Обратная связь")
#        return dict(list(context.items()) + list(c_def.items()))

#    def form_valid(self, form):
#        print(form.cleaned_data)
#        return redirect('home')


#class RegisterUser(DataMixin, CreateView):
#    form_class = RegisterUserForm
#    template_name = 'posts/register.html'
#    success_url = reverse_lazy('login')

#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Регистрация")
#        return dict(list(context.items()) + list(c_def.items()))

#    def form_valid(self, form):
#        user = form.save()
#        login(self.request, user)
#        return redirect('home')


#class LoginUser(DataMixin, LoginView):
#    form_class = LoginUserForm
#    template_name = 'posts/login.html'

#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title="Авторизация")
#        return dict(list(context.items()) + list(c_def.items()))

#    def get_success_url(self):
#        return reverse_lazy('home')


#def logout_user(request):
#    logout(request)
#    return redirect('login')
