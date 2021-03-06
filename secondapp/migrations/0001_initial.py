# Generated by Django 3.2.5 on 2021-08-14 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('password', models.CharField(default='None', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companyid', models.IntegerField(primary_key=True, serialize=False)),
                ('companyname', models.CharField(max_length=50)),
                ('companyjob', models.CharField(max_length=50)),
                ('companydetail', models.CharField(max_length=50)),
                ('companywork', models.CharField(max_length=50)),
                ('companylocation', models.CharField(max_length=50)),
                ('companydeadline', models.CharField(max_length=50)),
                ('companyregister', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Studyroom',
            fields=[
                ('studynum', models.IntegerField(primary_key=True, serialize=False)),
                ('studytitle', models.TextField()),
                ('studycontent', models.TextField()),
                ('studywriter', models.CharField(max_length=10)),
                ('studylink', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='secondapp.board')),
            ],
        ),
    ]
