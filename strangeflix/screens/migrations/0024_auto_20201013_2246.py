# Generated by Django 3.1.2 on 2020-10-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0023_auto_20201013_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('M', 'Monthly Plan'), ('Y', 'Yearly Plan'), ('H', '6 Months Plan'), ('N', 'No Active Plans')], default='N', max_length=2, null=True),
        ),
    ]
