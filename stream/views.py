from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render

from social_distribution.common import loginValid, set_page
from .models import *


@loginValid
def get_auth_posts(request):
    user_id = request.session["user_id"]
    title = request.GET.get("title", "")
    datas = Posts.objects.filter(author=user_id)
    if title:
        datas = datas.filter(title__icontains=title)
    page = request.GET.get("page", 0)
    page_list = []
    if datas:
        data, page_list = set_page(datas, 40, page)
    return render(request, "common/stream/posts_infos.html", {"datas": datas, "page_list": page_list, "title": title})


@loginValid
def add_auth_posts(request):
    user_id = request.session.get("user_id", "")
    post_id = request.GET.get("id", "")
    action = request.GET.get("action", "")
    post = None
    if post_id:
        posts = Posts.objects.filter(id=post_id)
        if posts.exists():
            post = posts[0]
            if action == "delete":
                posts.filter(author_id=user_id).delete()
                return HttpResponseRedirect("/stream/get_auth_posts")
        else:
            raise Http404
    if request.POST:
        post_id = request.GET.get("id", "")
        if post_id:
            posts = Posts.objects.filter(id=post_id)
            if posts.exists():
                post = posts[0]
            else:
                raise Http404
        user_id = request.session["user_id"]
        data = request.POST
        title = data.get("title", "")
        source = data.get("source", "")
        origin = data.get("origin", "")
        description = data.get("description", "")
        contentType = data.get("contentType", "")
        content = data.get("content", "")
        categories = data.get("categories", "")
        visibility = data.get("visibility", "")
        unlisted = data.get("unlisted", "")
        is_public = data.get("is_public", "")
        CommonMark = data.get("CommonMark", "")
        image = request.FILES.get("image", "")
        if post:
            post.title = title
            post.source = source
            post.origin = origin
            post.description = description
            post.contentType = contentType
            post.content = content
            post.categories = categories
            post.visibility = visibility
            post.unlisted = unlisted
            post.is_public = is_public
            post.CommonMark = CommonMark
            if image:
                post.image = image
        else:
            post = Posts(
                author_id=user_id,
                title=title,
                source=source,
                origin=origin,
                description=description,
                contentType=contentType,
                content=content,
                categories=categories,
                visibility=visibility,
                unlisted=unlisted,
                is_public=is_public,
                CommonMark=CommonMark,
                image=image,
                published=timezone.now()
            )
        post.save()
        return HttpResponseRedirect("/stream/get_auth_posts")

    return render(request, "common/stream/add_posts.html", {"post": post})


@loginValid
def get_post_detail(request, pk):
    posts = Posts.objects.filter(id=pk, is_public=True)
    if not posts.exists():
        raise Http404
    post = posts[0]
    post.view_count += 1
    post.save()
    comments = Comment.objects.filter(post=post)
    return render(request, "common/stream/post_detail.html", {"post": post, "comments": comments})


@loginValid
def add_comment(request):
    data = request.POST
    post_id = data.get("id")
    post = Posts.get_or_404(post_id)
    if not post:
        raise Http404
    comment = data.get("comment")
    auth = request.session.get("user_id")
    commen = Comment(
        author_id=auth,
        comment=comment,
        post_id=post_id
    )
    commen.save()
    post.comment_count += 1
    post.save()
    return HttpResponseRedirect("/stream/get_post_detail/{}".format(post_id))


@loginValid
def add_like_history(request):
    resp = {"state": 1, "data": {
        "count": 0
    }}
    post_id = request.GET.get("post_id")
    post = Posts.get_or_404(post_id)
    if not post:
        resp["state"] = 0
    else:
        user_id = request.session.get("user_id")
        like_historys = LikeHistory.objects.filter(
            author_id=user_id,
            post=post,
        )
        if like_historys.exists():
            resp["state"] = 0
        else:
            like_historys = LikeHistory(
                author_id=user_id,
                post=post,
            )
            like_historys.save()
            post.like_count+=1
            post.save()
        resp["data"]["count"] = post.like_count
    return JsonResponse(resp)
