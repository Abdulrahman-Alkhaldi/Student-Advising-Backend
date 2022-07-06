# Generated by Django 4.0.4 on 2022-07-06 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='apointment',
            name='studentID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.student'),
        ),
        migrations.AlterField(
            model_name='apointment',
            name='time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.courses'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='semister',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.semester'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='idds',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='todo.curriculum'),
        ),
    ]
