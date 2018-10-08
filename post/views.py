



from django.shortcuts import render, redirect

from post.models import Post


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        return render(request, 'post/create_post.html')


def edit_post(request):
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(pk=post_id)

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(pk=post_id)
        return render(request, 'post/edit_post.html', {'post': post})


def read_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(pk=post_id)
    return render(request, 'post/read_post.html', {'post': post})


def delete_post(request):
    post_id = int(request.GET.get('post_id'))
    Post.objects.get(pk=post_id).delete()
    return redirect('/')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})


def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'post/search.html', {'posts': posts})