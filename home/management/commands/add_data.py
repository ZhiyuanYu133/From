#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import random
import os
from django.core.management.base import BaseCommand

from home.models import *


class Command(BaseCommand):
    help = '初始化环境'

    def handle(self, *args, **options):
        self.create()

    def create(self):
        types = OfficeType.objects.all()
        doctors = Doctors.objects.all()
        for i in range(100):
            for doctor in doctors:
                _type = random.choice(types)
                d = Doctors()
                d.doctor_name = doctor.doctor_name+str("i")
                d.rank_name = doctor.rank_name
                d.office_type = _type
                d.doctor_pic = doctor.doctor_pic
                d.desc = doctor.desc
                d.address = doctor.address
                d.goods_at = doctor.goods_at
                d.hospital = doctor.hospital
                d.status = doctor.status
                d.save()