# Generated by Django 3.0.3 on 2020-02-10 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200210_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintainance',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Owner'),
        ),
    ]