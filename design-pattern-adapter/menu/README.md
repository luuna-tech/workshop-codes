# Adaptador de Menú

Otro problema que enfrentamos al implementar el nuevo backend (ZeCore) en el web-client existente, fue que la estructura de menú cambió, originalmente teníamos un menú que definía tres niveles distintos:

1. Categoría
2. Subcategoría (subcategory)
3. Productos (subcategorySubChildren)

Es decir:


En el nuevo esquema tenemos un menú que puede tener cualquier número de niveles, y los productos son una propiedad del 


## Ejercicio

Crear un adaptador que tome un objeto `treeMenu` y lo transforme para que implemente la interfaz `threeLevelMenu`.

Se proveen los ejemplos como JSON, puedes implementarlo en el lenguaje que prefieras.

### Notas:

* En el menú de tres niveles la segunda categoría puede estar vacía y una categoría puede tener 
* En el menú de árbol el sitio es la categoría raíz, pero en el de tres niveles hay que ignorarlo para empezar desde el segundo nivel