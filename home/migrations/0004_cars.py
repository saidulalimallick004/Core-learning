# Generated by Django 5.1.6 on 2025-02-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_students_creationdate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Color', models.TextField()),
            ],
        ),
    ]
