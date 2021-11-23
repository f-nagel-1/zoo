# Generated by Django 3.2.9 on 2021-11-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('legs', models.PositiveIntegerField()),
                ('height', models.PositiveIntegerField()),
                ('speed', models.PositiveIntegerField()),
            ],
        ),
    ]
