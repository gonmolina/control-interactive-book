# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md:myst,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] lang="en"
# # Introducción a los cuadernos de Jupyter y Sympy
#
# Sympy es un paquete de algebra para Python. A este paquete, y luego a todos
# los demás los utilizaremos a usaremos a través de una interfaz conveniente
# que son los [Jupyter Notebook](http://jupyter.org/). Este cuaderno intenta
# mostrarles algunas de las características más útiles de Sympy y de esta manera comenzar a interiorizarnos con el uso de los cuadernos.
#
# Este cuaderno usará Python como lenguaje de programación. Esto significa que
# la mayor parte de lo aprendido en este curso puede ser desarrollado y
# aplicado en cuadernos. Los cuadernos se dividen en celdas donde se puede
# poner código y luego correrlo haciendo **Mayúscula + Enter**.
#
# Si a este cuaderno lo está visualizando a través de una pagina web, puede
# descargarlo haciendo click en icono de descarga ubicado arriba a la izquierda
# y seleccionando el forma `ipynb`. Los archivos con la extensión `.ipynb` son
# cuadernos de jupyter o jupyter notebooks.

# %% [markdown] lang="en"
# Existen varias alternativas para visualizar los cuadernos de Jupyter. Paso a
# describir las más utilizadas:
#
# - Jupyter Notebook: se encuentra instalada con el software recomendado para
# la materia y consiste en una página web, que es servida por nuestra propia
# computadora. Es relativamente liviana en cuanto a recursos computacionales y
# con esta se pueden ver, ejecutar y editar los cuadernos
#
# - Jupyter Lab: es similar a la anterior, también se encuentra pre instalada
# con el software recomendado para la materia, pero cuenta con algunas
# funcionalidades extra como explorador de variables, ayuda contextual,
# explorador de archivos, y otras funcionalidades instalables a través de
# plugins. esta es la forma recomendada por la cátedra para acceder a los
# cuadernos
#
# - Spyder: este es un entorno de desarrollo integrado (IDE) pre-instalado con
# el software recomendado por la cátedra. Para los cuadernos se usa un plugin
# que se llama spyder-notebook. Este IDE trata de emular el entorno ofrecido
# por Matlab. Es una buena elección para personas que están habituadas a
# utilizar Matlab y quiere o debe comenzar a utilizar Python y los cuadernos
# de jupyter.
#
# - Visual Studio Code: es un software gratuito de microsoft, que con un
# plugin (Python es el nombre del mismo) soporta todo lo referente a los cuadernos. 
# Si bien utiliza jupyter para mostrar los cuadernos, provee una interface propia.
# Es recomendable para personas que están habituadas a programar o que quieran además de utilizar los cuadernos, escribir programas en Python o cualquier otro lenguaje en un mismo entorno.
# Puede ser algo complejo de configurar y lo puede  descargar desde
# [aquí](https://code.visualstudio.com/).

# %% [markdown] lang="es"
# ## Un recorrido rápido
#
# Tómese un segundo para recorrer la interfaz del cuaderno con el software que
# haya elegido para visualizarlo y editarlo. Haga doble click sobre las celdas
# y mire el código fuente de cada una. Trate de entender la forma es que se
# escriben los títulos, que se definen las ecuaciones y como es diferencia una
# celda donde se va escribir código y una donde se escribe texto o ecuaciones
# matemáticas.
#
# Ahora que está familiarizado con la nomenclatura, ¡ejecutemos algo de código!
#
# *Evalúe la celda a continuación para imprimir por pantalla el mensaje
# "Hello World" haciendo clic dentro de la celda y luego presionando
# Shift + Enter*

# %%
for word in ['Hello', 'World']:
    print(word)

# %%
a = 1
a

# %% [markdown] lang="es"
# ### Matemáticas en cuadros de texto
#
# El editor de texto admite matemáticas en notación [$\LaTeX$] (latex). Puede
# hacer doble clic en un cuadro de texto para ver los códigos utilizados para
# ingresarlo:
#
# $$f(a)=\int^{a=\infty}_{a=0} \frac{1}{a+2} \mathrm{d}a$$
#
# Haga doble clic en la fórmula anterior para ver el código que la produjo.

# %% [markdown]
# Aprovechemos lo aprendido para introducirnos en el mundo de algebra
# simbólica con Python utilizando el paquete `SymPy`.

# %% [markdown] lang="es"
# ## Introducción a SymPy
#
# Necesitamos importar
# [el paquete SymPy](http://docs.sympy.org/latest/index.html)
# para obtener capacidades matemáticas simbólicas.

# %%
import sympy as sp

# %% [markdown] lang="es"
# Necesitamos comenzar la forma de imprimir formulas por pantalla para obtener
# una visualización tipográfica agradable.
#
# _Tenga en cuenta que esto cambia algo en función de la versión de sympy_

# %%
sp.init_printing()

# %% [markdown] lang="es"
# Para hacer cálculos simbólicos, necesitamos crear un símbolo.

# %%
x = sp.Symbol('x')

# %%
x

# %% [markdown] lang="es"
# Sympy nos permite hacer muchas operaciones matemáticas que serían tediosas a
# mano. Por ejemplo, podemos expandir un polinomio:

# %%
polynomial = (2*x + 3)**4
polynomial.expand()

# %% [markdown] lang="es"
# Observe lo que sucedió: definimos un nuevo nombre llamado `polynomial`
# y luego usamos el método `.expand()` para expandir el polinomio. Podemos ver
# todos los métodos asociados con un objeto escribiendo su nombre y un punto y
# luego presionando "tabulador".
#
# Acceda a la lista de métodos para la variable polynomial ingresando "." y
# presionando tabulador al final de la línea en la celda a continuación.

# %% [markdown] lang="es"
# Para obtener ayuda sobre cualquier método, podemos escribir su nombre y
# agregar un `?` al final, luego evaluar la celda.
#
# Obtenga ayuda sobre el método `.expand()` mediante la evaluación de la celda
# a continuación:

# %%
# polynomial.expand?

# %% [markdown] lang="es"
# También es posible obtener ayuda para una función colocando el cursor entre
# los paréntesis y presionando Mayúscula + Tabulador

# %% [markdown] lang="es"
# Por supuesto, también podemos factorizar polinomios:

# %%
(x**2 + 2*x + 1).factor()

# %% [markdown] lang="es"
# ### Cálculo
#
# Sympy sabe integrar y diferenciar.

# %%
polynomial.diff(x)  # First derivative

# %%
polynomial.diff(x, 2)  # Second derivative

# %%
# indefinite integral - note no constant of integration is added
polynomial.integrate(x)

# %%
# Note that integrate takes one argument which is a tuple for the definite
# integral
polynomial.integrate((x, 1, 2))

# %% [markdown] lang="es"
# ### Límites
#
# Podemos evaluar los límites usando SymPy, incluso para límites "interesantes"
# donde necesitaríamos la regla de L'Hopital

# %%
sp.limit((2*sp.sin(x) - sp.sin(2*x))/(x - sp.sin(x)), x, 0)

# %% [markdown] lang="es"
# ### Aproximación
#
# SymPy tiene soporte incorporado para la expansión de series de Taylor

# %%
nonlinear_expression = sp.sin(x)

# taylor expansion in terms of the x variable, around x=2, first order.
sp.series(nonlinear_expression, x, 2, 2)

# %% [markdown] lang="es"
# Para eliminar el término de perdida use `.removeO()`

# %%
temp = sp.series(nonlinear_expression, x, 2, 2)
temp.removeO()

# %% [markdown] lang="es"
# También notará que el comportamiento predeterminado de SymPy es retener
# representaciones exactas de ciertos números:

# %%
number = sp.sqrt(2)*sp.pi
number

# %% [markdown] lang="es"
# Para convertir las representaciones exactas de arriba en representaciones
# aproximadas de [punto flotante]
# (https://en.wikipedia.org/wiki/Floating_point), use uno de estos métodos.
# `sympy.N` funciona con expresiones complicadas que también contienen
# variables. `float` devolverá un número de tipo `float` de Python normal y es
# útil cuando se interactúa con programas que no son de Sympy.

# %%
sp.N(number*x)

# %%
float(number)

# %% [markdown] lang="es"
# ### Resolver ecuaciones
#
# Sympy puede ayudarnos a resolver y manipular  ecuaciones utilizando la
# función `solve`. Como muchas funciones de resolución, encuentra ceros de una
# función, por lo que tenemos que reescribir las ecuaciones de igualdad para
# que sean iguales a cero,
#
# $$
# \begin{aligned}
#  2x^2 + 2 &= 4 \\
#  2x^2 + 2 - 4 &= 0
# \end{aligned}
# $$

# %%
solutions = sp.solve(2*x**2 + 2 - 4)
solutions

# %%
solutions[0]

# %% [markdown] lang="es"
# También podemos usar `sympy.Eq` para construir ecuaciones

# %%
equation = sp.Eq(2*x**2 + 2, 4)
equation

# %% [markdown] lang="es"
# La función roots nos dará también la multiplicidad de las raíces.

# %%
sol = sp.roots(equation)
sol

# %% [markdown]
# Esto no dice que la ecuación anterior tiene una solución -1 y otra solución
# igual 1.

# %% [markdown] lang="es"
# También podemos resolver sistemas de ecuaciones pasando una lista de
# ecuaciones para resolver y pidiendo una lista de variables para resolver.

# %%
x, y = sp.symbols('x, y')
sp.solve([x + y - 2,
          x - y - 0], [y, x])

# %% [markdown] lang="es"
# Esto incluso funciona con variables simbólicas en las ecuaciones.

# %%
a, b, c = sp.var('a, b, c')
solution = sp.solve([a*x + b*y - 2,
                     a*x - b*y - c], [x, y])
solution

# %%
solution.items()

# %%
a = [i for i in solution.values()]

# %%
a[0]

# %%
a[1]
