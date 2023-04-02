import random
from string import ascii_letters, digits

from django.db.models import F
from django.http import JsonResponse, Http404
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect

from home.forms import UserForm
from home.models import UserFollow, UserFriends
from social_distribution.common import setPassword, loginValid, send_email, set_page
from stream.models import *


# index
@loginValid
def index(request):
    # user_id = request.session.get("user_id")
    page = request.GET.get("page", 0)
    datas = Posts.objects.filter(is_public=1)
    page_list = []
    if datas:
        datas, page_list = set_page(datas, 40, page)
    return render(request, "common/index.html", {"datas": datas, "page_list": page_list})


# register页面
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
            error = "原password错误或两次password不一致！"
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
        error = "email或验证码不正确，请确认！"
    return render(request, "common/user/forget_password.html", {"error": error})


# ajax 发送验证码
def send_code(request):
    response = {"status": 0, "data": "email有误，请确认email"}
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
            response["data"] = "验证码已发送，请查收"
            request.session["code"] = str1
            request.session["email"] = email
    return JsonResponse(response)


@loginValid
def add_follow(request, id):
    user_id = request.session.get("user_id")
    username = request.session.get("username")
    user = User.objects.filter(id=id)
    if not user:
        raise Http404
    userfollow = UserFollow.objects.filter(create_user=id, follow_to=user_id)
    user_follow = UserFollow(
        create_user=user_id,
        create_user_name=username,
        follow_to=id,
        follow_to_username=user[0].username,
        is_followed=True if userfollow.exists() else False
    )
    user_follow.save()
    return render(request, "common/stream/doctor_detail.html", {"user_follow": user_follow})


def user_follows(request):
    user_id = request.session.get("user_id")
    page = request.GET.get("page", 0)
    datas = UserFollow.objects.filter(
        create_user=user_id
    )
    page_list = []
    if datas:
        datas, page_list = set_page(datas, 40, page)
    return render(request, "common/user/user_follows.html", {"datas": datas, "page_list": page_list})




# # my follows info
# def type_messages(request):
#     data = request.GET
#     type_name = data.get("type_name", "")
#     types = OfficeType.objects.all()
#     print(type_name)
#     if type_name:
#         types = types.filter(type_name__icontains=type_name)
#     return render(request, "common/stream/types_message.html", {"types": types, "type_name": type_name})
#
#
# # post info
# def doctors_messages(request):
#     data = request.GET
#     doctor_name = data.get("doctor_name", "")
#     desc = data.get("desc", "")
#     doctors = Doctors.objects.all()
#     if doctor_name:
#         doctors = doctors.filter(doctor_name__icontains=doctor_name)
#     if desc:
#         doctors = doctors.filter(
#             Q(goods_at__icontains=desc) | Q(office_type__type_name__icontains=desc) | Q(desc__icontains=desc) | Q(
#                 address__icontains=desc) | Q(rank_name__icontains=desc) | Q(office_type__desc__icontains=desc))
#     return render(request, "common/stream/posts_infos.html",
#                   {"doctors": doctors, "doctor_name": doctor_name, "desc": desc})
