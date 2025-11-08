from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .form import Post_form
from django.contrib.auth.decorators import login_required

def all_Post(request,cid=None,uid=None):
    if cid:
        posts = Post.objects.filter(cata_id = cid)
        return render(request,"cata_post.html",{"posts":posts})
    elif uid:
        posts = Post.objects.filter(author_id = uid)
        return render(request,"my_post.html" ,{"posts":posts})
    else:
        posts = Post.objects.all()
        return render(request,"index.html",{"posts":posts})

def post_details(request,id):
    match_post = get_object_or_404(Post,pk=id)
    return render(request,"post_details.html",{"match_post":match_post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('all_Post')
    else:
        form = Post_form()
        return render(request,'addpost.html',{'form':form})
    

def update_post(request, id):
    post = get_object_or_404(Post,pk=id)
    if request.method == 'POST':
        form = Post_form(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('all_Post')
    else:
        form = Post_form(instance=post)
        return render(request,'updatepost.html',{'form':form, 'post':post})


def delete_post(request,id):
    post = get_object_or_404(Post,pk=id)
    post.delete()

    return redirect('all_Post')
    