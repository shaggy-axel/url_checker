# Generated by Django 3.2.5 on 2021-07-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_url_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='status_text',
            field=models.CharField(blank=True, default='Not checked', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='url',
            name='status_code',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
    ]