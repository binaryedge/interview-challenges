# Generated by Django 2.0.1 on 2018-02-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.TextField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='domaindataleak',
            unique_together={('data_leak', 'domain')},
        ),
        migrations.AlterUniqueTogether(
            name='emaildataleak',
            unique_together={('data_leak', 'email')},
        ),
    ]