# Generated by Django 3.0.7 on 2020-06-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_maker', '0002_auto_20200619_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_record',
            name='Code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='subject_information',
            name='Code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teachers_record',
            name='Code',
            field=models.CharField(max_length=20),
        ),
    ]
