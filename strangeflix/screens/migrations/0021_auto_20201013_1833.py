# Generated by Django 3.1.2 on 2020-10-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0020_auto_20201013_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('Y', 'Yearly Plan'), ('N', 'No Active Plans'), ('H', '6 Months Plan'), ('M', 'Monthly Plan')], default='N', max_length=2, null=True),
        ),
    ]
