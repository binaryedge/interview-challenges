# Generated by Django 2.0.1 on 2018-02-16 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataLeak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DomainDataLeak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_leak', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaks.DataLeak')),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaks.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmailDataLeak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_leak', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaks.DataLeak')),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='leaks.Email')),
            ],
        ),
    ]