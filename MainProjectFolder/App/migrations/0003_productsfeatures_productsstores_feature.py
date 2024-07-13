# Generated by Django 4.2.6 on 2024-06-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_productscart_productscategories_productsorder_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeatureName', models.CharField(max_length=200, verbose_name='Feature')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Products Categories',
            },
        ),
        migrations.AddField(
            model_name='productsstores',
            name='Feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.productsfeatures', verbose_name='Feature'),
        ),
    ]
