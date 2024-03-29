# Generated by Django 3.2 on 2024-03-11 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('TO_DO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], max_length=20)),
            ],
        ),
    ]
