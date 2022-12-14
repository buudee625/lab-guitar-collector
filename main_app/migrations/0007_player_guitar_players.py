# Generated by Django 4.1 on 2022-09-01 06:55

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_guitar_kind_alter_review_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('age', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='guitar',
            name='players',
            field=models.ManyToManyField(to='main_app.player'),
        ),
    ]
