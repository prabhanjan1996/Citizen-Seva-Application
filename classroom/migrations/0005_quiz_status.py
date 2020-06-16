# Generated by Django 3.0.3 on 2020-05-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20200508_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='Status',
            field=models.CharField(choices=[('Not Solved', 'Not Solved'), ('Progressing', 'Progressing'), ('Completed', 'Completed'), ('Technical Issues', 'Technical Issues')], max_length=40, null=True),
        ),
    ]
