# Generated by Django 4.0.4 on 2022-05-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=211)),
                ('doubt', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]