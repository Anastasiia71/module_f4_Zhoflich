# Generated by Django 4.2.3 on 2023-07-24 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipySite', '0002_alter_recipy_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('recepies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipySite.recipy')),
            ],
        ),
    ]
