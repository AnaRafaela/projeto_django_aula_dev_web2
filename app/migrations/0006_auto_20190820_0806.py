# Generated by Django 2.2.2 on 2019-08-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190815_1303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='resumo',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imagem',
            new_name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='auth',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]