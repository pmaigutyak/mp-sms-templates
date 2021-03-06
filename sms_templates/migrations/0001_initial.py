# Generated by Django 2.0.6 on 2018-06-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMSTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Slug')),
                ('recipients', models.TextField(blank=True, help_text='One phone number for one line', max_length=1000, null=True, verbose_name='Recipients')),
                ('text', models.TextField(max_length=1024, verbose_name='Message')),
                ('placeholders', models.TextField(blank=True, max_length=4096, null=True, verbose_name='Placeholders')),
            ],
            options={
                'verbose_name_plural': 'SMS Templates',
                'verbose_name': 'SMS Template',
            },
        ),
    ]
