# Generated by Django 2.2.17 on 2022-03-25 10:28

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('coverages', '0010_polarisation_channels_expand'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_index', models.PositiveSmallIntegerField(default=1)),
                ('mean', models.FloatField(blank=True, null=True)),
                ('minimum', models.FloatField(blank=True, null=True)),
                ('maximum', models.FloatField(blank=True, null=True)),
                ('stddev', models.FloatField(blank=True, null=True)),
                ('valid_percent', models.FloatField(blank=True, null=True)),
                ('histogram', jsonfield.fields.JSONField(blank=True, null=True)),
                ('arraydata_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='array_statistics', to='coverages.ArrayDataItem')),
            ],
            options={
                'unique_together': {('arraydata_item', 'band_index')},
            },
        ),
    ]
