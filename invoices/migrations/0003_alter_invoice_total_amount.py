# Generated by Django 5.1.7 on 2025-03-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_rename_roles_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]
