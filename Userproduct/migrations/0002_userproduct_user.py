# Generated by Django 3.1 on 2020-09-21 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usermanagement', '0001_initial'),
        ('Userproduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='User',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usermanagement.user'),
        ),
    ]
