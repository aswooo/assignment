# Generated by Django 4.1 on 2023-02-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('history_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('is_spend', models.BooleanField()),
                ('cost', models.BigIntegerField()),
                ('balance', models.BigIntegerField()),
                ('memo', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'history',
            },
        ),
    ]
