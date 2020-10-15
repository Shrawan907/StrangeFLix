# Generated by Django 3.1.2 on 2020-10-15 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0026_auto_20201015_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='screens.payment'),
        ),
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('Y', 'Yearly Plan'), ('N', 'No Active Plans'), ('M', 'Monthly Plan'), ('H', '6 Months Plan')], default='N', max_length=2, null=True),
        ),
    ]
