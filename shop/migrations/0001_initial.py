# Generated by Django 3.1.7 on 2021-06-04 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
