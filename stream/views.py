import random
from string import ascii_letters, digits

from django.db.models import F, Q
from django.http import JsonResponse, Http404
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render, redirect

from social_distribution.common import setPassword, loginValid, send_email, set_page
from home.forms import UserForm
from .models import *


