# Generated by Django 2.1.5 on 2019-04-02 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0003_auto_20190402_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Note.Food', verbose_name='食物'),
        ),
        migrations.AlterField(
            model_name='images',
            name='merchant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Note.MerchantInfo', verbose_name='商户'),
        ),
        migrations.AlterField(
            model_name='images',
            name='userinfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
