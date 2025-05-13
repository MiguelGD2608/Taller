import uuid
from django.db import models
from accounts.models import Usuario
from pos_project.choices import EstadoEntidades,EstadoOrden

# Create your models here.
class TipoIdentificacion(models.Model):
    tipo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_tipo = models.CharField(max_length=150, null=False)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO)

    def __str__(self):
        return self.nombre_tipo

    class Meta:
        db_table = "tipos_identificacion"
        ordering = ['nombre_tipo']

# Create your models here.
class GrupoArticulo(models.Model):
    grupo_id=models.UUIDField(primary_key=True)
    codigo_grupo=models.CharField(max_length=5, null=False)
    nombre_grupo=models.CharField(max_length=150,null=False)
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO)


class Meta:
    db_table="grupos_articulos"
    ordering = ["codigo_grupo"]

class LineaArticulo(models.Model):
    linea_id=models.UUIDField(primary_key=True)
    codigo_linea=models.CharField(max_length=10, null=False)
    grupo = models.ForeignKey(GrupoArticulo,on_delete=models.RESTRICT,null=False,related_name='grupo_linea')
    nombre_linea=models.CharField(max_length=150,null=False)
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO)


class Meta:
    db_table="lineas_articulos"
    ordering = ["codigo_linea"]


class Articulo(models.Model):
    articulo_id=models.UUIDField(primary_key=True)
    codigo_articulo=models.CharField(max_length=25, null=False)
    codigo_barras=models.CharField(max_length=25, null=False)
    descripcion=models.CharField(max_length=150, null=False)
    presentacion=models.CharField(max_length=10, null=False)
    grupo = models.ForeignKey(GrupoArticulo,on_delete=models.RESTRICT,null=False,related_name='grupos_lineas')
    linea = models.ForeignKey(LineaArticulo,on_delete=models.RESTRICT,null=False,related_name='linea_articulo')
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO)
    stock = models.DecimalField(max_digits=12, decimal_places=2)
    imagen = models.CharField(max_length=255, null=False)


class Meta:
    db_table="articulos"
    ordering = ["codigo_articulo"]


class ListaPrecio(models.Model):
    articulo = models.ForeignKey(Articulo,on_delete=models.RESTRICT,null=False,related_name='lista_articulo')
    precio_1 = models.DecimalField(max_digits=12, decimal_places=2)
    precio_2 = models.DecimalField(max_digits=12, decimal_places=2)
    precio_3 = models.DecimalField(max_digits=12, decimal_places=2)
    precio_4 = models.DecimalField(max_digits=12, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=12, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=12, decimal_places=2)


class Meta:
    db_table="lista_precios"
    ordering = ["articulo"]

class CanalCliente(models.Model):
    canal_id=models.CharField(max_length=3, null=False)
    nombre_canal=models.CharField(max_length=100, null=False)

class Meta:
    db_table="canal_clientes"
    ordering = ["canal_id"]

class Cliente(models.Model):
    cliente_id=models.UUIDField(primary_key=True)
    tipo_identificacion=models.CharField(max_length=1, null=False)
    nro_identificacion=models.CharField(max_length=11, null=False)
    nombres=models.CharField(max_length=150, null=False)
    direccion=models.CharField(max_length=150, null=False)
    correo_electronico=models.CharField(max_length=255, null=False)
    nro_movil=models.CharField(max_length=15, null=False)
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO)
    canal_id = models.ForeignKey(CanalCliente,on_delete=models.RESTRICT,null=False,related_name='canal_cliente')

class Meta:
    db_table="clientes"
    ordering = ["cliente_id"]


class Pedido(models.Model):
    pedido_id=models.UUIDField(primary_key=True)
    nro_pedido = models.IntegerField()
    fecha_pedido = models.DateTimeField()
    cliente_id = models.ForeignKey(Cliente,on_delete=models.RESTRICT,null=False,related_name='cliente_pedido')
    importe = models.DecimalField(max_digits=12, decimal_places=2)


class Meta:
    db_table="lista_precios"
    ordering = ["pedido_id"]


class ItemPedido(models.Model):
    item_id=models.UUIDField(primary_key=True)
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT,null=False,related_name='pedido_item')
    nro_item = models.IntegerField()
    articulo_id = models.ForeignKey(Articulo,on_delete=models.RESTRICT,null=False,related_name='articulo_item')
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2)
    total_item = models.DecimalField(max_digits=12, decimal_places=2)
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO)


class Meta:
    db_table="item_pedidos"
    ordering = ["item_id"]


def __str__(self):
    return self.nombre_grupo

class Meta:
    db_table="grupos_articulos"
    ordering=["codigo_grupo"]

class Vendedor(models.Model):
    vendedor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombres = models.CharField(max_length=150, null=False)
    correo = models.EmailField(max_length=255, null=False)
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO)

    class Meta:
        db_table = "vendedores"
        ordering = ["nombres"]

class OrdenCompraCliente(models.Model): 
    pedido_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    nro_pedido = models.CharField(max_length=50, unique=True)  
    fecha_pedido = models.DateField(auto_now_add=True, null=False) 
    cliente = models.ForeignKey('Cliente', on_delete=models.RESTRICT, null=False) 
    vendedor = models.ForeignKey('Vendedor', on_delete=models.RESTRICT, null=False) 
    importe = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    estado = models.IntegerField(choices=EstadoOrden, 
    default=EstadoOrden.PENDIENTE) 
    notas = models.TextField(blank=True, null=True) 
    creado_por = models.ForeignKey(Usuario, on_delete=models.RESTRICT, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False) 

def actualizar_total(self): 
    # """Actualiza el total de la orden basado en los items""" 
    total = sum(item.total_item for item in self.items_orden_compra.all()) 
    self.importe = total 
    self.save() 
    
def __str__(self): 
    return f"Orden #{self.nro_pedido} - {self.cliente}" 

class Meta: 
    db_table = "ordenes_compra_cliente" 
    ordering = ["-fecha_creacion"] 

class ItemOrdenCompraCliente(models.Model): 
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    pedido = models.ForeignKey(OrdenCompraCliente, on_delete=models.CASCADE, 
    null=False, related_name='items_orden_compra') 
    nro_item = models.PositiveIntegerField(default=1, null=False) 
    articulo = models.ForeignKey('Articulo', on_delete=models.RESTRICT, null=False, related_name='articulo_item_orden_compra') 
    cantidad = models.PositiveIntegerField(null=False, default=1) 
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0) 
    total_item = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0) 
    estado = models.IntegerField(choices=EstadoEntidades, default=EstadoEntidades.ACTIVO) 
    creado_por = models.ForeignKey(Usuario, on_delete=models.RESTRICT, null=False) 
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False) 

def save(self, *args, **kwargs): 
    # Calcular el total del item 
    self.total_item = self.cantidad * self.precio_unitario 
    # Si no se ha establecido el precio unitario, tomarlo del artículo 
    if self.precio_unitario == 0: 
        try: 
            lista_precio = self.articulo.listaprecio 
            self.precio_unitario = lista_precio.precio_1 
            self.total_item = self.cantidad * self.precio_unitario
        except: 
            pass 
        super().save(*args, **kwargs) 
        # Actualizar el total de la orden 
        # self.pedido.actualizar_total() 

def __str__(self): 
    return f"{self.cantidad} x {self.articulo.descripcion}" 

class Meta: 
    db_table = "items_ordenes_compra_cliente" 