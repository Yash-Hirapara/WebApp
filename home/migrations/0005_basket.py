# Generated by Django 4.0.5 on 2022-08-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_manuitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=30)),
                ('itemprice', models.IntegerField()),
            ],
        ),
    ]
