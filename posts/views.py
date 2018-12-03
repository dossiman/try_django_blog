from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Post
from .forms import PostForm


def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()
        messages.success(request, 'Successfully Created')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Not Successfully Created')

    context = {
        'form': form,
    }
    return render(request, 'posts/post_form.html', context)


def posts_detail(request, id=None):
    obj = get_object_or_404(Post, id=id)
    context = {
        'title': obj.title,
        'obj': obj,
    }
    return render(request, 'posts/post_detail.html', context)


def posts_list(request):
    queryset_list = Post.objects.all()  # .order_by('-timestamp')
    paginator = Paginator(queryset_list, 5)  # Show 25 posts per page

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    context = {
        'title': 'List',
        'object_list': queryset,
    }
    return render(request, 'posts/post_list.html', context)


def posts_update(request, id=None):
    obj = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('title'))
        instance.save()
        messages.success(request, '<a href="#">Item</a> Saved', extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': obj.title,
        'obj': obj,
        'form': form,
    }
    return render(request, 'posts/post_form.html', context)


def posts_delete(request, id=None):
    obj = get_object_or_404(Post, id=id)
    obj.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('posts:list')
