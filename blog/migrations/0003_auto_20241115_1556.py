# Generated by Django 2.2.28 on 2024-11-15 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20241115_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='lieu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Equipement'),
        ),
    ]