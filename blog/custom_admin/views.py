from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from post.models import Post


def is_superuser(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_superuser, login_url='/users/login/')
def admin_dashboard(request):
    users = User.objects.filter(is_superuser=False).order_by('-date_joined')
    posts = Post.objects.select_related('author', 'cata').order_by('-created_at')
    context = {
        'users': users,
        'posts': posts,
        'total_users': users.count(),
        'total_posts': posts.count(),
        'blocked_users': users.filter(is_active=False).count(),
    }
    return render(request, 'custom_admin/dashboard.html', context)


@user_passes_test(is_superuser, login_url='/users/login/')
def admin_delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('admin_dashboard')


@user_passes_test(is_superuser, login_url='/users/login/')
def admin_block_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = not user.is_active   # toggle block/unblock
    user.save()
    return redirect('admin_dashboard')


@user_passes_test(is_superuser, login_url='/users/login/')
def admin_delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.delete()
    return redirect('admin_dashboard')
