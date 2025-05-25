from collections import deque

class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora  
        self.app = app
        self.mensaje = mensaje

    def __str__(self):
        return f"[{self.hora}] {self.app}: {self.mensaje}"

def eliminar_facebook(cola):
    """Elimina todas las notificaciones de Facebook de la cola."""
    nueva_cola = deque()
    while cola:
        notif = cola.popleft()
        if notif.app.lower() != 'facebook':
            nueva_cola.append(notif)
    return nueva_cola

def mostrar_twitter_python(cola):
    """Muestra notificaciones de Twitter cuyo mensaje incluye 'Python', sin perder datos."""
    temp = deque()
    for notif in cola:
        if notif.app.lower() == 'twitter' and 'python' in notif.mensaje.lower():
            print(notif)
        temp.append(notif)
    

def contar_notificaciones_horario(cola, hora_inicio, hora_fin):
    """Usa una pila para almacenar notificaciones entre dos horas y retorna la cantidad."""
    pila = []
    for notif in cola:
        if hora_inicio <= notif.hora <= hora_fin:
            pila.append(notif)
    return len(pila)


if __name__ == "__main__":
    
    cola = deque([
        Notificacion('11:30', 'Facebook', 'Nuevo mensaje'),
        Notificacion('11:45', 'Twitter', 'Aprende Python ahora'),
        Notificacion('12:00', 'Instagram', 'Nueva foto'),
        Notificacion('13:15', 'Twitter', 'Python es genial'),
        Notificacion('16:00', 'Facebook', 'Evento hoy'),
    ])

    
    cola = eliminar_facebook(cola)

   
    print("Notificaciones de Twitter con 'Python':")
    mostrar_twitter_python(cola)

    
    cantidad = contar_notificaciones_horario(cola, '11:43', '15:57')
    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {cantidad}")