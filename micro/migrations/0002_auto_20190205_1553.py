# Generated by Django 2.1.5 on 2019-02-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Micro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_id', models.CharField(max_length=20)),
                ('link_link', models.URLField()),
                ('link_description', models.TextField()),
                ('link_author', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'micro',
            },
        ),
        migrations.DeleteModel(
            name='BlogComments',
        ),
    ]
