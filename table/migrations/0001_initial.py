# Generated by Django 3.0.8 on 2020-07-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element', models.CharField(max_length=15)),
                ('symbol', models.CharField(max_length=3)),
                ('atomicNumber', models.IntegerField()),
                ('atomicMass', models.FloatField()),
                ('neutrons', models.IntegerField()),
                ('protons', models.IntegerField()),
                ('electrons', models.IntegerField()),
                ('phase', models.CharField(max_length=35)),
                ('radioactive', models.BooleanField(default=False)),
                ('type', models.CharField(max_length=35)),
            ],
        ),
    ]