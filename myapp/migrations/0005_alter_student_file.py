# Generated by Django 4.0.6 on 2022-07-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_student_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]