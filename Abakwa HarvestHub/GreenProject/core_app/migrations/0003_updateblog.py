# Generated by Django 4.2.9 on 2024-01-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_creditunion_tutorialpoint_alter_basemodel_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
