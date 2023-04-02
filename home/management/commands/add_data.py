#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import random
import os
from django.core.management.base import BaseCommand

from home.models import *


class Command(BaseCommand):
    help = 'init env'

    def handle(self, *args, **options):
        self.create()

    def create(self):
        pass