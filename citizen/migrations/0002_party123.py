# Generated by Django 3.0.3 on 2020-04-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party123',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Description', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('ShortName', models.CharField(max_length=200)),
                ('SignName', models.CharField(max_length=200)),
            ],
        ),
    ]
