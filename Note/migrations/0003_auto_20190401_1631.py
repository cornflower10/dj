# Generated by Django 2.1.5 on 2019-04-01 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0002_auto_20190401_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='images',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='end_vip_time',
            field=models.DateTimeField(auto_now=True, verbose_name='vip到期日'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='createTime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期'),
        ),
    ]