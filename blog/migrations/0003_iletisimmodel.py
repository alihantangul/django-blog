# Generated by Django 3.1.5 on 2024-01-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240129_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('isim_soyisim', models.CharField(max_length=150)),
                ('mesaj', models.TextField()),
                ('olusturulma_tarihi', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'İletişim',
                'db_table': 'iletisim',
            },
        ),
    ]
