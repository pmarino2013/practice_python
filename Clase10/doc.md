### 1. `filtro_gris`

Es la imagen donde vamos a buscar.

- **Por qué es importante:** La detección de rostros (Haar Cascades) se basa en la intensidad de la luz (contraste). No necesita colores para saber dónde hay una nariz o un ojo. Al pasar la imagen a gris, eliminamos información innecesaria y hacemos que el proceso sea mucho más rápido.

### 2. `scaleFactor=1.1` (El zoom invertido)

Este es el parámetro de **escala**. El algoritmo tiene una "ventana" de tamaño fijo para buscar caras. Pero en una foto, las caras pueden estar cerca (grandes) o lejos (pequeñas).

- **Cómo funciona:** OpenCV reduce el tamaño de la imagen original un poco en cada paso (un 10% si usamos 1.1) y vuelve a pasar la ventana de búsqueda.
- **Ejemplo:** Si pones `1.1`, la imagen se achica un poco cada vez hasta que el rostro "encaja" en la ventana de búsqueda. Si pones `1.5`, se achica de forma muy brusca y podrías "saltarte" rostros.

### 3. `minNeighbors=8` (El filtro de consenso)

Este es el parámetro de **calidad**. Cuando el algoritmo cree ver un rostro, suele encontrar varias detecciones positivas muy cerca una de la otra.

- **Cómo funciona:** Le dice a OpenCV: "No me digas que hay un rostro a menos que hayas encontrado al menos 8 detecciones en esa misma zona".
- **Ejemplo:**
- Un valor bajo (**3**): Detectará todo, pero podrías tener "falsos positivos" (confunde una sombra o un pliegue de ropa con una cara).
- Un valor alto (**10** o más): Es mucho más seguro. Solo marcará el rostro si la detección es muy clara, aunque podrías ignorar rostros que estén un poco borrosos.

### 4. `minSize=(50, 50)` (El filtro de distancia)

Este es el parámetro de **tamaño mínimo**.

- **Cómo funciona:** Le dice al código que ignore cualquier objeto detectado que sea más pequeño que un cuadrado de 50x50 píxeles.
- **Ejemplo Práctico:** Si estás haciendo un sistema de asistencia para alumnos que están sentados frente a la computadora, sus rostros siempre serán grandes (ej. 200x200). Al poner un `minSize`, evitas que el programa pierda tiempo o se equivoque analizando "manchitas" pequeñas que hay en el fondo del aula.

---

### 💡 Analogía para tus alumnos

Imaginen que están buscando a una persona en una multitud usando binoculares:

1. **`filtro_gris`**: Se ponen lentes que solo ven sombras para no distraerse con los colores de la ropa.
2. **`scaleFactor`**: Van ajustando el zoom de los binoculares para ver a la gente que está cerca y a la que está lejos.
3. **`minNeighbors`**: No gritan "¡Ahí está!" hasta que no están 8 veces seguros de que lo que ven es una cara y no un arbusto.
4. **`minSize`**: Si ven algo que parece una cara pero es del tamaño de una hormiga, lo ignoran porque saben que su objetivo no puede ser tan pequeño.
