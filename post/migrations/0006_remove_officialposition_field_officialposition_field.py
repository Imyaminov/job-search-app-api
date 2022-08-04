# Generated by Django 4.0.6 on 2022-07-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_professionalfield_region_rename_category_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officialposition',
            name='field',
        ),
        migrations.AddField(
            model_name='officialposition',
            name='field',
            field=models.ManyToManyField(related_name='field_name', to='post.professionalfield'),
        ),
    ]
