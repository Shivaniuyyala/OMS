# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-06 16:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('created_on', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('order_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, b'Submitted'), (2, b'In-progress'), (3, b'Complete'), (4, b'Cancelled')], default=1)),
                ('user_comment', models.TextField(blank=True, null=True)),
                ('admin_comment', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=1)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitem_created_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitem_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, editable=False, to='order.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
