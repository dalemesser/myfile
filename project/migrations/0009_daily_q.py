# Generated by Django 3.1.3 on 2020-11-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_order_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_Q',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
    ]