# Generated by Django 4.0.6 on 2022-07-26 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_posted_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=128)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Status',
        ),
        migrations.RemoveField(
            model_name='post',
            name='job_title',
        ),
        migrations.AddField(
            model_name='post',
            name='job_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_status', to='post.status'),
        ),
        migrations.AddField(
            model_name='post',
            name='times_seen',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='OfficialPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='field_name', to='post.professionalfield')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='job_field',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='field_fromPost', to='post.professionalfield'),
        ),
        migrations.AddField(
            model_name='post',
            name='job_position',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_name', to='post.officialposition'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_location', to='post.region'),
        ),
    ]
