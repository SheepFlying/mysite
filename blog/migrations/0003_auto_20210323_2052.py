# Generated by Django 3.1.7 on 2021-03-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210323_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签')),
            ],
        ),
        migrations.AlterModelOptions(
            name='friendlink',
            options={'ordering': ['-create_date'], 'verbose_name': '友链', 'verbose_name_plural': '友链'},
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
    ]
