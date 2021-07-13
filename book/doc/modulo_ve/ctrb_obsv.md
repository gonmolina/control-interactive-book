---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

import control as ctrl
import numpy as np
```

# Análisis de los sistemas en su forma de espacio de estados

+++

Supongamos que tenemos la siguiente función transferencia:

```{code-cell} ipython3
G=ctrl.tf([1,1],[1,2,3])
G
```

De los apuntes de teoría podemos escribir una representación de espacios de estados en la forma canónica de controlabilidad que tendrá el mismo comportamiento externo de $G$ de la siguiente manera :

```{code-cell} ipython3
Ac=np.matrix([[-2, -3],[1,0]])
Ac
```

Antes de seguir, verificamos que los polos de $G$ sean los autovalores de $Ac$

```{code-cell} ipython3
G.pole()
```

```{code-cell} ipython3
np.linalg.eigvals(Ac)
```

Ahora definimos el resto de las matrices

```{code-cell} ipython3
Bc=np.matrix("1;0")
Bc
```

```{code-cell} ipython3
Cc=np.matrix("1 1")
Cc
```

```{code-cell} ipython3
Dc=0
```

Vamos ahora a definir un sistema $sys$ que se comporte igual que $G$

```{code-cell} ipython3
sys_c=ctrl.ss(Ac,Bc,Cc,Dc)
```

Si $sys$ tiene los mismos polos, los mismos ceros y la misma ganancia en estado estacionario, entonces se comportará igual que $G$.

```{code-cell} ipython3
sys_c.pole()
```

```{code-cell} ipython3
sys_c.zero()
```

```{code-cell} ipython3
sys_c.dcgain()
```

```{code-cell} ipython3
G.dcgain()
```

Por lo tanto podemos ver que la función transfewrencia de $sys$ será la misma que la de $G$. Es decir, $sys$ se comporta externamente igual que $G$. Verificamos

```{code-cell} ipython3
ctrl.tf(sys_c)
```

Vamos ahora a definir el sistema en espacio de estados, que se comporte como $G$ en la forma canónica de observabilidad. De la teoría sabemos que:

```{code-cell} ipython3
Ao=Ac.T
Bo=Cc.T
Co=Bc.T
Do=Dc
```

```{code-cell} ipython3
sys_o=ctrl.ss(Ao,Bo,Co,Do)
```

```{code-cell} ipython3
sys_o.pole()
```

```{code-cell} ipython3
sys_o.zero()
```

```{code-cell} ipython3
sys_o.dcgain()
```

```{code-cell} ipython3
ctrl.tf(sys_o)
```

```{code-cell} ipython3
ctrl.tf(sys_o)
```

El módulo de control de Python puede transformar una función transferencia a una forma de estados (no necesariameinte en alguna forma canónica). Esto se hace:

```{code-cell} ipython3
sys=ctrl.ss(G)
sys
```

Además Python puede transformar un sistema en espacio de estados a alguna de las formas canónicas.

Por ejemplo para escribir $sys$ (que está ahora en espacio de estados) en su forma canónica de controlabilidad podemos hacer

```{code-cell} ipython3
ctrl.canonical_form(sys, 'reachable') # controlable
```

Notar que esta función necesita como primer argumento un sistema de espacios de estados.

Si queremos la forma canónica de observabilidad podemos hacer:

```{code-cell} ipython3
ctrl.canonical_form(sys, 'observable')
```

Existe otra forma canónica de represetanción en espacio de estados que se la conoce como froma canónica modal. Esta la podemos obtener haciendo:

```{code-cell} ipython3
ctrl.canonical_form(sys, 'modal')
```

Esta forma canónica lo que haces es aislar los modos unos de otros. Es decir cada variables de estado aparece en la diagonal. Sin embargo, como vemos en este caso, no tenemos una forma diagonal de la matriz $A$. Esto sucede por que hay casos que no se puede o no se dease aislarlos:
- en caso de que se tengan autovales complejos conjugados, no se aislan para lograr tener una matriz $A$, $B$ y $C$ a coficiente reales.
- en caso de que sean multiples no se pueden aislar por que tienen el mismo autovector y no se pueden usar estos para la transformación. Para estos casos se utiliza la forma de Jordan (no se dará en este curso).

+++

Vamos a ver otro ejemplo:

```{code-cell} ipython3
s=ctrl.tf('s')
G2 = 1/((s+1)*(s+2)*(s+3))
G2
```

Vemos que esta función trnasferencia tiene los polos en -1, -2 y -3. Transformemosla a espacio de estados usando la función `ss`.

```{code-cell} ipython3
sys2 = ctrl.ss(G2)
sys2
```

Veamos al sistema en su forma canónica de controlabilidad.

```{code-cell} ipython3
ctrl.canonical_form(sys2, 'reachable')
```

Ahora veamoslo en la forma canónica de observabilidad

```{code-cell} ipython3
ctrl.canonical_form(sys2, 'observable')
```

Finalmente obtengamos la forma conónica modal:

```{code-cell} ipython3
sys2_m, _=ctrl.canonical_form(sys2, 'modal')
```

```{code-cell} ipython3
sys2_m.A
```

Notar:
- La función `canoincal_form` devuelve un sistema en la forma canónica solicitada y la amtriz de trnasformación necesaria para obtenerlo
- En la diagonal tenmos los modos del sistema (polos de $G$ o autovalores de $A$)
- Fuera de la diagonal tenemos ceros o valores muy cercanos a ceros (debido a problemas numericos en el cálculo)

+++

Verificamos el resto de las matrices:

```{code-cell} ipython3
sys2_m.B
```

```{code-cell} ipython3
sys2_m.C
```

```{code-cell} ipython3
sys2_m.D
```

En esta forma canónica, la matriz $B$ como la conexión de la entrada con el modo del sistema . Y de forma análoga a la mariz $C$ como la conexión del modo con la salida del sistema.

+++

## Ejemplo de conexión de sistemas

```{code-cell} ipython3
G1=ctrl.tf(1,[1,1])
G2=ctrl.tf([1,1],[1,2])
```

Podemos ver que G1 tiene un polo en -1 y G2 tiene un polo en -2 y un cero en -1.

+++

Ahora supogamos que queremos un nuevo sistema que:
- conecta la salida de G1 con la entrada de G2
- la salida es la salida de G2
- la entrada es la entrada de G1

+++

Para eso vamos a usar una función que se llama `connect`. Esta utiliza sistemas en espacio de estados, entonces hacemos:

```{code-cell} ipython3
sys1 = ctrl.ss(G1)
sys2= ctrl.ss(G2)
```

Y lueog relizamos las conexiones:

```{code-cell} ipython3
sys_c = ctrl.connect(ctrl.append(sys1, sys2),[[2,1]],[1],[2])
sys_c
```

Analizamos  los polos y ceros del sistema ya interconectado 

```{code-cell} ipython3
sys_c.pole()
```

```{code-cell} ipython3
sys_c.zero()
```

Vemos que el sistema conserva los mismos polos y los mismos ceros que el original, lo cual era de esperarse, ya que su función transferencia sería G1*G2

+++

Obtngamos la forma canónica de controlabilidad del sistema

```{code-cell} ipython3
ctrl.canonical_form(sys_c, 'reachable')
```

Podemos ver que las matrices A, B, C y D coinciden con lo visto en teoría.

Ahora obtengamos la forma canónica de observabilidad:

```{code-cell} ipython3
ctrl.canonical_form(sys_c, 'observable')
```

Podemos ver que este sistema no puede ser escrito en su forma canónica de observabilidad. Esto sucede por que el sistema no es observable.

La interptertación se da por que un sistema observable necesita tener evidencia de lo que sucede con cada modo a la salida. Como el modo en -1 se ve completamente tapado por el cero en esa misma frecuencia este sistema no es observable por que no tiene niguna evidencia del modo en -1 a la salida del mismo.

+++

Ahora hagamos la conexión al revez (primero G1 y luego G2):

```{code-cell} ipython3
sys_o = ctrl.connect(ctrl.append(sys1, sys2),[[1,2]],[2],[1])
sys_o
```

Obtengamos la forma canónica observable:

```{code-cell} ipython3
ctrl.canonical_form(sys_o, 'observable')
```

```{raw-cell}
Y ahora la forma canónica controlable:
```

```{code-cell} ipython3
ctrl.canonical_form(sys_o, 'reachable')
```

Podemos ver que ahora no podemo obtener la forma canónica de obserbavilidad.

La razón de esto es que no se puee exitar el modo -1, que ahora quedó tapado desde el lado de la entrada. Toda excitación que tenga "frecuencia generalizada -1" será tapada por el cero en -1. Por lo tanto este sistema no es controlable, ya que no puede exitar desde esa entrada el modo -1.

Es importante destacar que ambos sistemas presentan la misma función tranferencia G1*G2, pero uno es solo controlable y el otro es solo observable. Esto se debe a que la controlabilidad y la observabilda son propiedades internas de un sistema, por lo que no pueden ser deciddidas a partir de modelos externos de un sistema como son las funciones transferencias.

+++

Estas dos mismas pripiedades pueden ser analizadas con la forma modal. Tomemos el sistema $sys_C$ donde la entrada esta conectada a G1 y lasalida a G2:

```{code-cell} ipython3
ctrl.canonical_form(sys_c, 'modal')
```

Podemos ver que la matriz B tiene todos los valores distintos de 0. Esto significa que todos los modos están conectados a la entrada, por lo que deducimos que el sistema es controlable.

Pero podemos ver que C tiene un 0 en el primer elemento. Y que en la diagona de A el primer elemento es -1. Esto quiere decir que no hay niguna evidencia del modo -1 en la salida por que el sistema no es observable.

+++

Probemos ahora con la segunda conexión:

```{code-cell} ipython3
ctrl.canonical_form(sys_o, 'modal')
```

Podemos ver ahora que la matriz C no tiene ningún valor igual a 0, por lo que ahora el sistema sería observable (todos los modos están presentes de alguna manera en la salida). Pero tenesmo un 0 en la primer fila de B, que se corresponde con el modo en -1. Esto quiere decir que no podemos excitar este modo. Por lo tanto no es controlable.

```{code-cell} ipython3

```
