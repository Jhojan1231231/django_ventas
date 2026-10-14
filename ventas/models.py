from django.db import models

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    ciudad = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
class pedido(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, related_name='pedidos')
    producto = models.CharField(max_length=100)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=12, decimal_places=0)
    estado = models.CharField(max_length=50, default='Pendiente')
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.producto}"   