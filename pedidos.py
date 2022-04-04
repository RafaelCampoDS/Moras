#Project Moras
#This scrip is goona initializate the class orders thath represents the 
#online order of blueberryes and other products online in the website moras

from datetime import datetime


class pedido:
    def __init__(self,nombre_usuario,codigo_pedido,ubicacion,restaurante,lista_compra) -> None:
        self.nombre_usuario = nombre_usuario 
        self.codigo_pedido = codigo_pedido 
        self.ubicacion = ubicacion
        self.restaurante = restaurante
        self.lista_compra = lista_compra
        self.hora_orden = datetime.now('''tzinfo=pytz.utc''')

#Se inicializa la clase pedido seteando la fecha en la que se recibio el pedido

    def hora_preparacion(self):
        self.hora_preparacion = datetime.now('''tzinfo=pytz.utc''')

#Una vez se llame a la funcion hora recojida se creara el atributo

    def hora_recojida(self):
        self.hora_preparacion = datetime.now('''tzinfo=pytz.utc''')

#Una vez se llame a la funcion hora recojida se creara el atributo

    def hora_entrega(self):
        self.hora_preparacion = datetime.now('''tzinfo=pytz.utc''')

#Una vez se llame a la funcion hora recojida se creara el atributo
    def llamada_json(self):
        pass 
