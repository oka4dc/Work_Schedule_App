# Generated by Django 4.1.4 on 2022-12-18 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=100)),
                ('Basic_Salary', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Hours_work', models.PositiveIntegerField(default=0)),
                ('Gross_Salary', models.PositiveIntegerField(default=0)),
                ('Staff_Grade_Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkApp.staff_grade')),
            ],
        ),
    ]
