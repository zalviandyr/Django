# Generated by Django 2.2.9 on 2020-01-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200114_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alamat',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='judul',
            field=models.CharField(max_length=20),
        ),
    ]
