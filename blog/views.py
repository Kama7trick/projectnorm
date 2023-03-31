from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from django.shortcuts import render
from django.views.generic.edit import CreateView


class Bloglist(ListView):
    paginate_by = 5
    model = Post
    template_name = 'home.html'


class ViewCategory(ListView):
    class SearchResultsView(ListView):
        model = Post
        template_name = 'category.html'

        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            context['q'] = self.request.GET.get('q')
            return context


def post_list_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'category.html', {'posts': posts})


class BlogBirds(ListView):
    paginate_by = 1
    model = BirdPost
    template_name = 'birds.html'


class BlogMammals(ListView):
    paginate_by = 1
    model = MammalsPost
    template_name = 'mammals.html'


class BlogFish(ListView):
    paginate_by = 1
    model = FishPost
    template_name = 'fish.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BirdsDetailView(DetailView):
    model = BirdPost
    template_name = 'birds_detail.html'


class FishDetailView(DetailView):
    model = FishPost
    template_name = 'fish_detail.html'


class MammalsDetailView(DetailView):
    model = MammalsPost
    template_name = 'mammals_detail.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class Search(ListView):
    template_name = 'home.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('q')) or BirdPost.objects.filter(
            title__icontains=self.request.GET.get('q')) or MammalsPost.objects.filter(
            title__icontains=self.request.GET.get('q')) or FishPost.objects.filter(
            title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class ShuePageView(TemplateView):  # Форум
    template_name = 'shue.html'


class ContactPageView(TemplateView):  # Контактная информация
    template_name = 'contact.html'


class GalleryPageView(TemplateView):  # Галерея
    template_name = 'gallery.html'


@login_required
def profile_view(request):
    return render(request, 'profile.html')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
