# Generated by Django 3.0.3 on 2020-05-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0006_auto_20200501_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeStructure123',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=200)),
                ('Numbers', models.IntegerField()),
            ],
        ),
    ]