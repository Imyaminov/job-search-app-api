# Generated by Django 4.0.6 on 2022-07-26 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_job_field_alter_post_job_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='job_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_fromPost', to='post.professionalfield'),
        ),
        migrations.AlterField(
            model_name='post',
            name='job_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_status', to='post.status'),
        ),
    ]
