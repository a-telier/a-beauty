# Generated by Django 3.1.2 on 2021-01-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210129_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog_category',
            options={'verbose_name_plural': 'blog Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='additionalImages',
            field=models.FileField(blank=True, default='', null=True, upload_to='articles/additional'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to='articles/img'),
        ),
    ]
