import random
from string import ascii_letters, digits

from django.db.models import F, Q
from django.http import JsonResponse, Http404
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect

from home.forms import UserForm
from social_distribution.common import setPassword, loginValid, send_email, set_page
from stream.models import *


# index
# @loginValid
def index(request):
    # last = Doctors.objects.count() - 1
    # user_id = request.session.get("user_id")
    page = request.GET.get("page", 0)
    # type_name = request.GET.get("type_name", "")
    data = Posts.objects.filter(is_public=1)
    page_list = []
    # if type_name:
    #     data = data.filter(office_type__type_name__icontains=type_name)
    if data:
        data, page_list = set_page(data, 40, page)
    return render(request, "common/index.html", {"data": data, "page_list": page_list})


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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        u = User.objects.filter(username=username, password=setPassword(setPassword(password)))
        if u.exists():
            response = HttpResponseRedirect("/")
            response.set_cookie("username", username)
            request.session["username"] = username
            request.session["user_id"] = u[0].id
            request.session["image"] = u[0].profileImage.url
            print(u[0].profileImage.url, u[0].profileImage)
            return response
    return render(request, "common/user/login.html")


# 退出
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
    user = User.objects.filter(id=user_id)
    if user.exists():
        user = user[0]
        return render(request, "common/user/user_info.html", locals())
    else:
        return render(request, "common/pages-404.html")


# change user info
@loginValid
def change_userinfo(request):
    user_id = request.session.get("user_id")
    user = User.objects.filter(id=user_id)

    if not user.exists():
        return render(request, "common/pages-404.html")

    if request.method == "POST":
        data = request.POST
        displayName = data.get("displayName")
        gender = data.get("gender")
        phone = data.get("phone")
        email = data.get("email")
        address = data.get("address")
        image = request.FILES.get("image")
        print(image)
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


# 忘记password
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
    return render(request, "common/forget_password.html", {"error": error})


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


# post详情
def doctors_detail(request):
    _id = request.GET.get("id")
    user_id = request.session.get("user_id")
    doctors = Doctors.objects.filter(id=_id)
    if not doctors or not user_id:
        raise Http404
    doctor = doctors[0]
    return render(request, "common/doctor_detail.html", {"doctor": doctor})


# my follows info
def type_messages(request):
    data = request.GET
    type_name = data.get("type_name", "")
    types = OfficeType.objects.all()
    print(type_name)
    if type_name:
        types = types.filter(type_name__icontains=type_name)
    return render(request, "common/types_message.html", {"types": types, "type_name": type_name})


# post info
def doctors_messages(request):
    data = request.GET
    doctor_name = data.get("doctor_name", "")
    desc = data.get("desc", "")
    doctors = Doctors.objects.all()
    if doctor_name:
        doctors = doctors.filter(doctor_name__icontains=doctor_name)
    if desc:
        doctors = doctors.filter(
            Q(goods_at__icontains=desc) | Q(office_type__type_name__icontains=desc) | Q(desc__icontains=desc) | Q(
                address__icontains=desc) | Q(rank_name__icontains=desc) | Q(office_type__desc__icontains=desc))
    return render(request, "common/doctors_message.html",
                  {"doctors": doctors, "doctor_name": doctor_name, "desc": desc})
