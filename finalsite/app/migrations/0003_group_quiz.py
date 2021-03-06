# Generated by Django 2.2.2 on 2019-06-11 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_photo_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('quizlink', models.CharField(max_length=200)),
                ('descriptionlink', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('ans1', models.CharField(max_length=200)),
                ('ans2', models.CharField(max_length=200)),
                ('ans3', models.CharField(max_length=200)),
                ('real_ans', models.CharField(max_length=200)),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Group')),
            ],
        ),
    ]
