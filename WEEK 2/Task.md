
# 💡 Ejercicios

## 1. Pseudocódigo para calcular descuento de producto

**Descripción:** Se pide un `precio de producto` al usuario, calcula su descuento y muestra el precio final.  
- Si el precio es menor a 100, el descuento es del 2%.  
- Si el precio es mayor o igual a 100, el descuento es del 10%.

**Ejemplos:**  
- 120 → 108  
- 40 → 39.2

**Respuesta en pseudocódigo:**

```
Inicio

1. Definir descuento = 0
2. Definir precio_de_producto
3. Mostrar “Ingrese el precio del producto”
4. Pedir precio_de_producto
5. Si (precio_de_producto < 100), entonces
    1. descuento = precio_de_producto * 0.02
   Sino
    1. descuento = precio_de_producto * 0.10
FinSi
6. Definir total = precio_de_producto - descuento
7. Mostrar “Su precio a pagar es de ”
8. Mostrar total
9. Mostrar “Con un descuento de ”
10. Mostrar descuento

Fin
```

## 2. Pseudocódigo para evaluar tiempo en segundos

**Descripción:** Se pide un `tiempo en segundos` al usuario y calcula si es menor, mayor o igual a 10 minutos.  
- Si es menor, muestra cuántos segundos faltan para 10 minutos.  
- Si es mayor, muestra "Mayor".  
- Si es igual, muestra "Igual".

**Ejemplos:**  
- 1040 → Mayor  
- 140 → 460  
- 600 → Igual  
- 599 → 1

**Respuesta en pseudocódigo:**

```
Inicio

1. Definir diez_minutos = 600
2. Definir tiempo_en_segundos
3. Mostrar “Ingrese el tiempo en segundos”
4. Pedir tiempo_en_segundos
5. Si (tiempo_en_segundos > diez_minutos), entonces
       Mostrar “Mayor”
   Sino, Si (tiempo_en_segundos == diez_minutos) entonces
       Mostrar “Igual”
   Sino
       Mostrar diez_minutos - tiempo_en_segundos
FinSi

Fin
```

## 3. Suma de números del 1 hasta N

**Descripción:** Se pide un número al usuario y se realiza la suma de todos los números desde 1 hasta el número ingresado.

**Ejemplos:**  
- 5 → 15 (1 + 2 + 3 + 4 + 5)  
- 3 → 6 (1 + 2 + 3)  
- 12 → 78 (1 + 2 + ... + 12)

**Respuesta en pseudocódigo:**

```
Inicio

1. Definir numero
2. Definir contador = 1
3. Definir acumulador = 0
4. Mostrar “Ingrese el numero: ”
5. Pedir numero
6. Mientras (contador ≤ numero):
    1. acumulador = acumulador + contador
    2. contador = contador + 1
FinMientras
7. Mostrar acumulador

Fin
```

# 💡 Ejercicios Extra

## 1. Ordenar dos números

**Descripción:** Se pide 2 números al usuario (`primero` y `segundo`) y se ordenan de menor a mayor.

**Ejemplos:**  
- A: 56, B: 32 → A: 32, B: 56  
- A: 24, B: 76 → A: 24, B: 76  
- A: 45, B: 12 → A: 12, B: 45

**Respuesta en pseudocódigo:**

```
Inicio

1. Definir primero
2. Definir segundo
3. Definir A
4. Definir B
5. Mostrar “Ingrese el primer numero: ”
6. Pedir primero
7. Mostrar “Ingrese el segundo numero: ”
8. Pedir segundo
9. Si (segundo < primero):
    1. A = segundo
    2. B = primero
   Sino:
    1. A = primero
    2. B = segundo
FinSi
10. Mostrar A
11. Mostrar B

Fin
```

## 2. Convertir velocidad km/h a m/s

**Descripción:** Se pide una velocidad en km/h y la convierte a m/s.  
**Nota:** `1 km = 1000 m`, `1 hora = 3600 s`

**Ejemplos:**  
- 73 → 20.27  
- 50 → 13.88  
- 120 → 33.33

**Respuesta en pseudocódigo:**

```
Inicio

1. Definir velocidad_km_h
2. Comentar “1 km/h equivale a 1000/(60*60) m/s”
3. Definir metros_por_segundo = 1000/(60*60)
4. Mostrar “Ingrese la velocidad en km/h: ”
5. Pedir velocidad_km_h
6. Definir resultado = velocidad_km_h * metros_por_segundo 
7. Mostrar resultado

Fin
```

## 3. Porcentaje de mujeres y hombres

**Descripción:** Se pide el sexo de 6 personas (1 = mujer, 2 = hombre) y se muestra el porcentaje de mujeres y hombres.

**Ejemplos:**  
- 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres  
- 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres  
- 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres

**Respuesta en pseudocódigo:**

```
Inicio

1. Definir sexo
2. Definir contador = 0
3. Definir porcentaje_mujeres = 0
4. Definir porcentaje_hombres = 0
5. Mientras (contador < 6):
    1. Mostrar “Ingrese el sexo: ”
    2. Pedir sexo
    3. Si (sexo == 1):
        1. porcentaje_mujeres = porcentaje_mujeres + 1
       Sino, si (sexo == 2):
        1. porcentaje_hombres = porcentaje_hombres + 1
    FinSi
    4. contador = contador + 1
FinMientras
6. porcentaje_mujeres = porcentaje_mujeres / 6
7. porcentaje_hombres = porcentaje_hombres / 6
8. Mostrar porcentaje_hombres   
9. Mostrar porcentaje_mujeres

Fin
