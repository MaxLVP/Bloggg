# Generated by Django 3.2.3 on 2021-05-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateTimeField(),
        ),
    ]
