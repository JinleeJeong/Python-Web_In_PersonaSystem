# Generated by Django 2.1.4 on 2019-01-02 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AlterField(
            model_name='comment',
            name='password',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
