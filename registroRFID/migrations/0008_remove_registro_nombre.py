# Generated by Django 2.2.6 on 2019-11-05 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registroRFID', '0007_auto_20191104_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='nombre',
        ),
    ]
