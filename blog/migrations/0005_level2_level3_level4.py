# Generated by Django 3.2.3 on 2021-05-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_level1_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='level1_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Level3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='level1_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Level4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='level1_pics')),
            ],
        ),
    ]
