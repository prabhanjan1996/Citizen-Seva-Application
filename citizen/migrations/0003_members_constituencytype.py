# Generated by Django 3.0.3 on 2020-04-24 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0002_party123'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='ConstituencyType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='citizen.ConstituencyType'),
        ),
    ]
