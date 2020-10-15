# Generated by Django 3.1.2 on 2020-10-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0027_auto_20201015_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='tiimestamp',
            new_name='timestamp',
        ),
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('Y', 'Yearly Plan'), ('M', 'Monthly Plan'), ('N', 'No Active Plans'), ('H', '6 Months Plan')], default='N', max_length=2, null=True),
        ),
    ]
