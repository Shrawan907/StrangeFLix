# Generated by Django 3.1.2 on 2020-10-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0012_auto_20201013_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('M', 'Monthly'), ('N', 'No Active Plans'), ('Y', 'Yearly')], default='N', max_length=2, null=True),
        ),
    ]
