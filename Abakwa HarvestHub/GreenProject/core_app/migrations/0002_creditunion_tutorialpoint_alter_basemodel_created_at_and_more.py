# Generated by Django 4.2.9 on 2024-01-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditUnion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/')),
                ('location', models.CharField(max_length=65)),
                ('address', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='media/')),
                ('link', models.CharField(max_length=255)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='updates',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
