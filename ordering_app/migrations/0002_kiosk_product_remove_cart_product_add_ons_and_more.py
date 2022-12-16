# Generated by Django 4.1.4 on 2022-12-16 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordering_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kiosk_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('add_ons', models.ManyToManyField(to='ordering_app.addon')),
                ('kiosk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ordering_app.kiosk')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordering_app.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='cart_product',
            name='add_ons',
        ),
        migrations.RemoveField(
            model_name='cart_product',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cart_product',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cart_Product',
        ),
    ]
