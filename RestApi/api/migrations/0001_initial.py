# Generated by Django 3.2.6 on 2021-09-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='busan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Clustering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('date', models.TextField()),
                ('category', models.TextField()),
                ('articles', models.TextField()),
                ('urls', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('mainPress', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Donga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Hangook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Herald',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Joongang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Joseon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Nocut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Ohmynews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Wikitree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Yeonhap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.BigIntegerField()),
                ('title', models.TextField()),
                ('mainText', models.TextField()),
                ('category', models.TextField()),
                ('date', models.TextField()),
                ('url', models.TextField()),
                ('reporter', models.TextField()),
                ('press', models.TextField()),
                ('img', models.TextField()),
                ('emotion', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
