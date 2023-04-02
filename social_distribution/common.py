# -*-coding:utf-8 -*-

import hashlib


def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


from home.models import User
from django.http import HttpResponseRedirect


# loginvalid
def loginValid(func):
    def inner(request, *args, **kwargs):
        username = request.COOKIES.get("username")
        user_id = request.session.get("user_id")
        if username and user_id:
            user = User.objects.filter(id=user_id).first()
            if user and user.username == username:
                return func(request, *args, **kwargs)
        return HttpResponseRedirect("/login/")
    return inner



from django.core.mail import send_mail
from social_distribution import settings


def send_email(message, receiver, html_message=None):
    """
    """
    try:
        if html_message:
            result = send_mail("", message, settings.EMAIL_HOST_USER, [receiver], html_message=html_message)
        else:
            result = send_mail("", message, settings.EMAIL_HOST_USER, [receiver])
    except:
        result = 0
    return result


from django.core.paginator import Paginator


def set_page(data, num, page):
    """
    """
    p = Paginator(data, num)
    number = p.num_pages
    page_range = p.page_range
    try:
        page = int(page)
        data = p.page(page)
    except:
        data = p.page(1)
    if page < 5:
        page_list = page_range[:5]
    elif page + 4 > number:
        page_list = page_range[-5:]
    else:
        page_list = page_range[page - 3:page + 2]
    return data, page_list
