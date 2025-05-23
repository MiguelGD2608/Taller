# Generated by Django 5.2 on 2025-04-22 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanalCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canal_id', models.CharField(max_length=3)),
                ('nombre_canal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.UUIDField(primary_key=True, serialize=False)),
                ('tipo_identificacion', models.CharField(max_length=1)),
                ('nro_identificacion', models.CharField(max_length=11)),
                ('nombres', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('correo_electronico', models.CharField(max_length=255)),
                ('nro_movil', models.CharField(max_length=15)),
                ('estado', models.IntegerField(choices=[(1, 'Activo'), (9, 'De baja')], default=1)),
                ('canal_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='canal_cliente', to='core.canalcliente')),
            ],
        ),
        migrations.CreateModel(
            name='ListaPrecio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_1', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_2', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_3', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_4', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='lista_articulo', to='core.articulo')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.UUIDField(primary_key=True, serialize=False)),
                ('nro_pedido', models.IntegerField()),
                ('fecha_pedido', models.DateTimeField()),
                ('importe', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cliente_pedido', to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('item_id', models.UUIDField(primary_key=True, serialize=False)),
                ('nro_item', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('total_item', models.DecimalField(decimal_places=2, max_digits=12)),
                ('estado', models.IntegerField(choices=[(1, 'Activo'), (9, 'De baja')], default=1)),
                ('articulo_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='articulo_item', to='core.articulo')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='pedido_item', to='core.pedido')),
            ],
        ),
    ]
