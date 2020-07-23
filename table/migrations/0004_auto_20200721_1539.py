# Generated by Django 3.0.8 on 2020-07-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_auto_20200721_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='atomicMass',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='atomicNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='electrons',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='element',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='neutrons',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='phase',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='protons',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='symbol',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='type',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
