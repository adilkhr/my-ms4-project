# Generated by Django 3.2.8 on 2021-10-26 12:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('comments', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]