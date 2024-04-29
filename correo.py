
def create_email(nombre, apellido):
   
    '''La función recibirá el nombre y apellido de cada alumno/a y
       devolverá una dirección de correo en el dominio de Educación Navarra.
        Parámetros:
            - tendremos dos str con el nombre y el apellido de cada alumno/a.
        Salida:
            -la función devolveremos un str con el email resultante.
    '''
    dominio = '@educacion.navarra.es'
    nombre = nombre[0]
    apellido=apellido[:5]
    correo = nombre.lower() + apellido.lower() + dominio
    return correo 
create_email("Miguel","Martillo")