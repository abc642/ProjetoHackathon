# Generated by Django 3.0.8 on 2020-08-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_auto_20200723_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
                ('titulo', models.CharField(max_length=30)),
                ('descricao', models.TextField(max_length=240)),
                ('cidade', models.CharField(max_length=30)),
                ('numero', models.IntegerField()),
                ('imagem', models.CharField(max_length=240)),
            ],
        ),
        migrations.AlterField(
            model_name='element',
            name='atomicMass',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='atomicNumber',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='electrons',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='neutrons',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='protons',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]