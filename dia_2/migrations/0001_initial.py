# Generated by Django 4.2 on 2023-04-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peopleinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('preg', models.FloatField()),
                ('glu', models.FloatField()),
                ('bp', models.FloatField()),
                ('insulin', models.FloatField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('dpf', models.FloatField()),
                ('age', models.FloatField()),
                ('gender', models.FloatField()),
            ],
        ),
    ]