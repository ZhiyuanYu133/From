#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib


def set_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result
