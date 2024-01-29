# Generated by Django 5.0.1 on 2024-01-29 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField()),
                ('created_at', models.DateField()),
                ('modified_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.basemodel')),
                ('name', models.CharField(max_length=50)),
            ],
            bases=('core_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.basemodel')),
                ('title', models.CharField(max_length=50)),
            ],
            bases=('core_app.basemodel',),
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.basemodel')),
                ('image', models.ImageField(upload_to=None)),
                ('text', models.TextField()),
                ('tuto_url', models.URLField(max_length=500)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_app.area')),
            ],
            bases=('core_app.basemodel',),
        ),
    ]
