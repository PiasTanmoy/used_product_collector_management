# Generated by Django 3.1 on 2020-09-21 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0001_initial'),
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Buyer',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Buyer.buyer'),
        ),
    ]