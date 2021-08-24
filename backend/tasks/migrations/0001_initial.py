# Generated by Django 3.2.6 on 2021-08-23 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tasks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2500)),
                ('text', models.TextField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', tasks.models.TaskManager()),
            ],
        ),
        migrations.CreateModel(
            name='TaskImageAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_set', to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerImageAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_set', to='tasks.answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
