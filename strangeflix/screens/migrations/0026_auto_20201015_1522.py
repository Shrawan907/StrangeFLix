# Generated by Django 3.1.2 on 2020-10-15 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('screens', '0025_auto_20201013_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('N', 'No Active Plans'), ('H', '6 Months Plan'), ('M', 'Monthly Plan'), ('Y', 'Yearly Plan')], default='N', max_length=2, null=True),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('tiimestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
