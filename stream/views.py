from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse
from rest_framework import status
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
import json
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.forms import RadioSelect

# render(request, page to render, context)

@user_passes_test(lambda u: not u.is_authenticated, login_url='stream-home')
def welcome(request):
    return render(request, "stream/welcome.html")


@login_required
def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "stream/home.html", context)

# See if we can filter post here
class PostForm(forms.ModelForm):
    visibilityOptions = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    visibility = forms.ChoiceField(widget=forms.RadioSelect, choices=visibilityOptions)

    contentTypeOptions = (
        ('text/markdown -- common mark', 'text/markdown -- common mark'),
        ('text/plain -- UTF-8', 'text/plain -- UTF-8'),
        ('application/base64', 'application/base64'),
        (' image/png;base64', ' image/png;base64'),
        ('image/jpeg;base64', 'image/jpeg;base64'),
    )
    contentType = forms.ChoiceField(widget=forms.RadioSelect, choices=contentTypeOptions)

    class Meta:
        model = Post
        fields = ['title', 'description','contentType', 'content', 'image', 'categories','visibility', 'published']

@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "stream/home.html"
    context_object_name = "posts"
    ordering = ['-published']

    def get_queryset(self):
        # Get the value of the radio button from the GET request
        queryset = Post.objects.filter(visibility='public')
        # Order the queryset by published date
        queryset = queryset.order_by('-published')
        return queryset

@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    
@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    # Set post author to current login user
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
    # Check if user browsing the post is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author:
            return True
        return False


@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = "/"

    # Check if user browsing the post is the author
    def test_func(self):
        post = self.get_object()
        if self.request.user.profile == post.author:
            return True
        return False
    
@method_decorator(login_required(login_url=reverse_lazy('welcome')), name='dispatch')
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["comment"]

    # Set post author to current login user
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Set post author to current login user
        form.instance.author = self.request.user.profile
        # Save the comment object
        response = super().form_valid(form)
        # Add the comment to the post's comments field
        post.comments.add(self.object)
        post.count += 1
        post.save()
        return super().form_valid(form)
    
    
@login_required
def about(request):
    return render(request, "stream/about.html", {'title': 'About'})




def serialize_post(post):
    serialized = model_to_dict(post)
    serialized["type"] = str(post.type)
    serialized["title"] = str(post.title)
    serialized["id"] = str(post.id)
    #serialized["description"] = str(post.description)
    #serialized["contentType"] = str(post.contentType)
    #serialized["author"] = str(post.author)
    #serialized["categories"] = str(post.categories)
    serialized["content"] = str(post.content)
    return serialized

@api_view(['GET', 'POST'])
def posts(request):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        posts_data = Post.objects.all()
        posts_count = posts_data.count()
        page_size = int(request.GET.get("page_size", "10"))
        page_no = int(request.GET.get("page_no", "0"))
        orders_data = list(orders_data[page_no * page_size:page_no * page_size + page_size])
        orders_data = [serialize_post(post) for post in posts_data]
        return HttpResponse(json.dumps({"count": posts_count, "data": orders_data}), status=status.HTTP_200_OK)
    
    if request.method == "POST":
        post = Post()
        return save_post(request, post, status.HTTP_201_CREATED)

    return HttpResponse(json.dumps({"detail": "Wrong method"}), status=status.HTTP_501_NOT_IMPLEMENTED)



@api_view(['GET', 'PUT', 'DELETE'])
def post(request, post_id):
    if request.user.is_anonymous:
        return HttpResponse(json.dumps({"detail": "Not authorized"}), status=status.HTTP_401_UNAUTHORIZED)

    try:
        post = Post.objects.get(pk=post_id)
    except ObjectDoesNotExist:
        return HttpResponse(json.dumps({"detail": "Not found"}), status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return HttpResponse(json.dumps({"data": serialize_post(post)}), status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        return save_post(request, post, status.HTTP_200_OK)
    
    if request.method == "DELETE":
        post.delete()
        return HttpResponse(json.dumps({"detail": "deleted"}), status=status.HTTP_410_GONE)
    return HttpResponse(json.dumps({"detail": "Wrong method"}), status=status.HTTP_501_NOT_IMPLEMENTED)


def save_post(request, post, success_status):
    errors = []
    item = request.data.get("item", "")
    if item == "":
        errors.append({"item": "This field is required"})

    try:
        type = request.data.get("type", "")
        if type == "":
            errors.append({"type": "This field is required"})
        else:
            type = str(type)

    except ValueError:
        errors.append({"type": "Could not parse field"})

    try:
        title = request.data.get("title", "")
        if title == "":
            errors.append({"title": "This field is required"})
        else:
            title = str(title)

    except ValueError:
        errors.append({"title": "Could not parse field"})

    try:
        content = request.data.get("content", "")
        if title == "":
            errors.append({"content": "This field is required"})
        else:
            content = str(content)

    except ValueError:
        errors.append({"content": "Could not parse field"})

    try:
        id = request.data.get("id", "")
        if id == "":
            errors.append({"content": "This field is required"})
        else:
            id = str(id)

    except ValueError:
        errors.append({"content": "Could not parse field"})


    if len(errors) > 0:
        return HttpResponse(json.dumps(
            {
                "errors": errors
            }), status=status.HTTP_400_BAD_REQUEST)

    try:
        post.type = type
        post.title = title
        post.content = content
        post.id = id
        post.save()
    except Exception as e:
        return HttpResponse(json.dumps(
            {
                "errors": {"Post": str(e)}
            }), status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse(json.dumps({"data": serialize_post(post)}), status=success_status)


    