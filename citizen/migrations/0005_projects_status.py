# Generated by Django 3.0.3 on 2020-05-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0004_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('A', 'Completed'), ('B', 'Progressing'), ('C', 'Sanctioned')], max_length=3, null=True),
        ),
    ]
