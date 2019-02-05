from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from member.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', ]

    @transaction.atomic
    def save(self):
        user = super(SignUpForm, self).save(commit=False)
        user.is_member = True
        user.save()
        return user
