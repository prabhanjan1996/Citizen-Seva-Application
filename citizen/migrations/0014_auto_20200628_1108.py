# Generated by Django 3.0.3 on 2020-06-28 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0013_auto_20200626_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partyworkers',
            name='Party123',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='citizen.Party123'),
        ),
    ]
