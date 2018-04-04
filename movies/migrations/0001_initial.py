# Generated by Django 2.0.3 on 2018-04-04 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('duration', models.DurationField()),
                ('preview', models.ImageField(upload_to='')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Director')),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField()),
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=16)),
                ('plan_to_watch', models.ManyToManyField(related_name='users_plan_to_watch', to='movies.Movie')),
                ('watched', models.ManyToManyField(related_name='users_watched', to='movies.Movie')),
                ('watching', models.ManyToManyField(related_name='users_watching', to='movies.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.User'),
        ),
    ]
