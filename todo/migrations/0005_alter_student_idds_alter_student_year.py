# Generated by Django 4.0.4 on 2022-05-05 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='idds',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.curriculum'),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, verbose_name='year'),
        ),
    ]
