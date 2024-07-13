# Generated by Django 5.0.7 on 2024-07-13 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0003_hodimlar_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio/')),
            ],
        ),
    ]
