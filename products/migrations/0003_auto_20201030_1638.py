# Generated by Django 3.1.2 on 2020-10-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201027_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True, default='Ingredients', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='additionalImages',
            field=models.FileField(blank=True, upload_to='media/additional'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='media/product'),
        ),
    ]
