# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import *
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import transaction
from member.models import User
from member.decorators import login_required
from member.forms import SignUpForm


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        return super(SignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
