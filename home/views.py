import random
from string import ascii_letters, digits

from django.db.models import F
from django.db.models import Q
from django.http import JsonResponse, Http404
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect

from home.forms import UserForm
from home.models import UserFollow, UserFriends, UserInbux
from social_distribution.common import setPassword, loginValid, send_email, set_page
from stream.models import *


# index
@loginValid
def index(request):
    # user_id = request.session.get("user_id")
    page = request.GET.get("page", 0)
    datas = Posts.objects.filter(is_public=1, is_friends_public=1)
    page_list = []
    if datas:
        datas, page_list = set_page(datas, 40, page)
    return render(request, "common/index.html", {"datas": datas, "page_list": page_list})


# register page
def register(request):
    errors = ""
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data.get("username")
            password = userform.cleaned_data.get("password")
            password_confirm = request.POST.get("password_confirm")
            github = request.POST.get("github", "")
            email = request.POST.get("email", "")
            displayName = request.POST.get("displayName", "")
            if password == password_confirm:
                user = User()
                user.username = username
                user.github = "https://github.com/" + github
                user.email = email
                user.displayName = displayName
                user.password = setPassword(setPassword(password))
                user.save()
            return HttpResponseRedirect("/login/")
        else:
            errors = userform.errors
    return render(request, "common/user/register.html", {"errors": errors})


# login
def login(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        u = User.objects.filter(username=username, password=setPassword(setPassword(password)), is_active=1,
                                is_delete=0)
        if u.exists():
            response = HttpResponseRedirect("/")
            response.set_cookie("username", username)
            request.session["username"] = username
            request.session["user_id"] = u[0].id
            request.session["image"] = u[0].profileImage.url
            print(u[0].profileImage.url, u[0].profileImage)
            return response
        else:
            error = "user not find"
    return render(request, "common/user/login.html", {"error": error})


# logout
def logout(request):
    response = HttpResponseRedirect("/login/")
    try:
        response.delete_cookie("username")
        del request.session["username"]
        del request.session["user_id"]
        del request.session["image"]
    except:
        pass
    return response


# user info
@loginValid
def user_info(request):
    user_id = request.session.get("user_id")
    view_user_id = request.GET.get("user_id")
    add_friend = False
    add_follow = False
    if view_user_id:
        user = User.objects.filter(id=view_user_id)
        if not UserFriends.is_friends(user_id, view_user_id):
            add_friend = True
        if not UserFollow.is_follows(user_id, view_user_id):
            add_follow = True
    else:
        user = User.objects.filter(id=user_id)
    if user.exists():
        user = user[0]
        return render(request, "common/user/user_info.html", locals())
    else:
        return render(request, "common/stream/pages-404.html")


# change user info
@loginValid
def change_userinfo(request):
    user_id = request.session.get("user_id")
    user = User.objects.filter(id=user_id)

    if not user.exists():
        return render(request, "common/stream/pages-404.html")

    if request.method == "POST":
        data = request.POST
        displayName = data.get("displayName")
        gender = data.get("gender")
        phone = data.get("phone")
        email = data.get("email")
        address = data.get("address")
        image = request.FILES.get("image")

        user.update(
            displayName=displayName if displayName else F("displayName"),
            gender=gender if gender else F("gender"),
            phone=phone if phone else F("phone"),
            email=email if email else F("email"),
            address=address if address else F("address")
        )
        if image:
            user = user[0]
            user.profileImage = image
            user.save()
        return redirect("home:user_info")

    return render(request, "common/user/change_userinfo.html", {"user": user[0]})


# change password
@loginValid
def change_password(request):
    user_id = request.session.get("user_id")
    error = ""
    if request.method == "POST":
        data = request.POST
        old_password = data.get("old_password")
        new_password = data.get("new_password")
        password_sure = data.get("password_sure")
        user = User.objects.filter(id=user_id, password=setPassword(setPassword(old_password)))
        if new_password == password_sure and user.exists():
            user.update(password=setPassword(setPassword(new_password)))
            return redirect("home:logout")
        else:
            error = "last password error or password is diffrient！"
    return render(request, "common/user/change_password.html", {"error": error})


# forget password
def forget_password(request):
    error = ""
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        code = data.get("code")
        password = data.get("password")
        alternative_code = request.session.get("code")
        alternative_email1 = request.session.get("email")
        if email == alternative_email1 and code == alternative_code:
            User.objects.filter(email=email).update(password=setPassword(setPassword(password)))
            return redirect("home:login")
        error = "email or codeerror，please sure！"
    return render(request, "common/user/forget_password.html", {"error": error})


# ajax send code
def send_code(request):
    response = {"status": 0, "data": "email error，please user email"}
    email = request.GET.get("email")
    u = User.objects.filter(email=email)
    if u.exists():
        alternate_string = ascii_letters + digits
        str1 = ""
        for _ in range(6):
            str1 += random.choice(alternate_string)
        print(str1)
        result = send_email(str1, email)
        if result:
            response["status"] = 1
            response["data"] = "code sened"
            request.session["code"] = str1
            request.session["email"] = email
    return JsonResponse(response)


@loginValid
def add_follow(request, id):
    user_id = request.session.get("user_id")
    username = request.session.get("username")
    action = request.GET.get("action", "")
    print(action)
    user = User.objects.filter(id=id)
    # find this user follow
    userfollow = UserFollow.objects.filter(
        create_user=user_id, follow_to=id,
    )
    if not user:
        raise Http404
    if action == "delete":
        userfollow.delete()
    else:
        if not userfollow.exists():
            other_follow = UserFollow.objects.filter(
                create_user=id, follow_to=user_id,
            )

            user_follow = UserFollow(
                create_user=user_id,
                create_user_name=username,
                follow_to=id,
                follow_to_username=user[0].username,
                is_followed=1 if other_follow.exists() else 0
            )
            user_follow.save()
            other_follow.update(is_followed=1)
            UserInbux.add_inbux(
                user_id, username, id, user[0].username, "add follow", "", "{} follow you".format(username),
                user_follow.id,
                "UserFollow",
            )
    return HttpResponseRedirect("/user_follows/")


@loginValid
def get_user_follows(request):
    user_id = request.session.get("user_id")
    page = request.GET.get("page", 0)
    datas = UserFollow.objects.filter(
        create_user=user_id
    )
    page_list = []
    if datas:
        datas, page_list = set_page(datas, 40, page)
    return render(request, "common/user/user_follows.html", {"datas": datas, "page_list": page_list})


@loginValid
def add_friends(request, id):
    user_id = request.session.get("user_id")
    username = request.session.get("username")
    user = User.objects.filter(id=id)
    if not user:
        # TODO search other user
        raise Http404
    user_friend = UserFriends(
        create_user=user_id,
        create_user_name=username,
        friend_to=id,
        friend_to_username=user[0].username,
    )
    user_friend.save()
    UserInbux.add_inbux(
        user_id, username, id, user[0].username, "friend application", "url", "you hava a friend application",
        user_friend.id
    )
    return HttpResponseRedirect("/get_user_friends/")


@loginValid
def get_user_friends(request):
    user_id = request.session.get("user_id")
    page = request.GET.get("page", 0)
    datas = UserFriends.objects.filter(
        create_user=user_id,
        is_agreed=1
    )
    page_list = []
    if datas:
        datas, page_list = set_page(datas, 40, page)
    return render(request, "common/user/user_friend.html", {"datas": datas, "page_list": page_list})


@loginValid
def get_user_inbox(request):
    user_id = request.session.get("user_id")

    page = request.GET.get("page", 0)
    action = request.GET.get("action", "")
    is_read = request.GET.get("is_read", 0)
    datas = UserInbux.objects.filter(operator=user_id)
    if action:
        datas = datas.filter(action__icontains=action)
    print(is_read)
    if is_read:
        datas = datas.filter(is_read=is_read)
    page_list = []
    if datas:
        datas, page_list = set_page(datas, 40, page)
    return render(request, "common/user/user_inbux.html", {"datas": datas, "page_list": page_list, "is_read": is_read})


@loginValid
def update_inbux_state(request, id):
    user_id = request.session["user_id"]
    UserInbux.update_state(user_id, id)
    return redirect("/get_user_inbox")


@loginValid
def delete_friends(request, id):
    user_id = request.session["user_id"]
    print(user_id)
    UserFriends.objects.filter(
        Q(create_user=user_id) | Q(friend_to=user_id),
        id=id).delete()
    return HttpResponseRedirect("/get_user_friends")


@loginValid
def get_all_users(request):
    user_id = request.session["user_id"]
    page = request.GET.get("page", 0)
    username = request.GET.get("username", "")
    print(user_id)
    datas = UserFriends.objects.filter(
        Q(create_user=user_id) | Q(friend_to=user_id),
        is_agreed=1
    )
    friends = []
    for data in datas:
        if data.friend_to != user_id:
            friends.append(data.friend_to)
        elif data.create_user != user_id:
            friends.append(data.create_user)
    datas = User.objects.filter(is_active=1, is_delete=0).exclude(
        id=user_id
    ).exclude(id__in=friends)
    print(datas.count())
    if username:
        datas = datas.filter(username__icontains=username)
    page_list = []
    if datas:
        datas, page_list = set_page(datas, 40, page)
    ret = []
    # TODO:search other user
    return render(request, "common/user/user_list.html", {"datas": datas, "page_list": page_list, "username": username})


@loginValid
def read(request, id):
    UserInbux.objects.filter(id=id).update(
        is_read=1
    )
    return HttpResponseRedirect("/get_user_inbox")
