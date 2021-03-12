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

+++ {"colab_type": "text", "id": "V-kf_C3Hhklj"}

# Transformación lineal del espacio de estado

Cosideremos un sistema descripto por las ecuaciones de estado

$$
\begin{eqnarray}
\dot{\mathbf {x}} &=&  \mathbf A \mathbf x + \mathbf B \mathbf u\\
 y &=& \mathbf C \mathbf x + Du
 \end{eqnarray}
$$

Una transformación lineal mediante la matriz $\mathbf T$, que hace:
$$\mathbf x= \mathbf T \mathbf z$$

Sustituyendo la ecuación de la transformación en la de la ecuación de estados

$$
\begin{eqnarray}
\dot{\mathbf {x}} = \mathbf {T\dot z} &=& \mathbf {AT} \mathbf z + \mathbf B \mathbf u\\
 \dot{\mathbf {z}} &=& \mathbf {T}^{-1}\mathbf{AT} \mathbf z + \mathbf {T}^{-1}\mathbf B \mathbf u
 \end{eqnarray}
$$

Sustituyendo el la ecuación de salida se tiene:

 $$y = \mathbf C \mathbf{Tz} + Du$$
 
Comparando las ecuaciones del sistema transformado, podemos ver que la matriz $\mathbf T$ tranforma al sistema en:

$$
\begin{eqnarray}
\mathbf{\bar A} &=& \mathbf {T^{-1}} \mathbf A \mathbf T\\
\mathbf{\bar B} &=& \mathbf{T^{-1} B}\\
\mathbf{\bar C} &=& \mathbf{CT}\\
\bar D &=& D
\end{eqnarray}
$$


+++ {"colab_type": "text", "id": "RN8i2Nymhkll"}

# Transformación a la forma canónica de controlabilidad

La matrices de un sistema de orden 3 lineal e invariente en el tiempo representado mediante su forma canónica de controloabilidad tiene la forma:

$$
A_c = \begin{bmatrix}
-a_1&-a_2&-a_3\\
1&0&0\\
0&1&0\\
\end{bmatrix},  \qquad B_c=\begin{bmatrix}
1\\
0\\
0\\
\end{bmatrix}$$

$$
C_c=\begin{bmatrix}
c_1&c_2&c_3
\end{bmatrix}, \qquad D_c=\begin{bmatrix}0\end{bmatrix}$$

+++ {"colab_type": "text", "id": "1AakGUPnhklm"}

Como vimos anteriormente, una transformación lineal mediante la matriz $\mathbf T$, que hace:

$$\mathbf x=\mathbf{Tz}$$

Por lo tanto podemos, llamando $\mathbf{\bar A} = \mathbf A_c$, tenemos que:

$$\mathbf{A_c} \mathbf {T^{-1}}=\mathbf{T^{-1}} \mathbf {A}$$

Escribimos $\mathbf {T^{-1}}$ como vectores fila, es decir:

$$\mathbf{T^{-1}} = \begin{bmatrix}
\mathbf{t_1}\\
\mathbf{t_2}\\
\mathbf{t_3}\\
\end{bmatrix}$$

$$
\begin{bmatrix}
-a_1&-a_2&-a_3\\
1&0&0\\
0&1&0\\
\end{bmatrix} 
\begin{bmatrix}
\mathbf{t_1}\\
\mathbf{t_2}\\
\mathbf{t_3}\\
\end{bmatrix} = \begin{bmatrix}
\mathbf{t_1}\mathbf A\\
 \mathbf{t_2}\mathbf A\\
 \mathbf{t_3}\mathbf A\\
\end{bmatrix}
$$

+++ {"colab_type": "text", "id": "2w9ccvl4hkln"}

Trabajando con las columnas 2 y 3 se tiene que:

$$\left.\begin{array}{lll}
\mathbf{t_1} &=&\mathbf{t_2 A}\\
\mathbf{t_2} &=& \mathbf{t_3 A}\end{array}\right\}\implies \mathbf{t_1} =\mathbf{t_3A}^2
$$

+++ {"colab_type": "text", "id": "LJFfkgNKhklo"}

Por otro lado, asumiendo que $\mathbf B_c$ está en la forma canónica de control, tenemos la relación

$$ \mathbf{T^{-1}}\mathbf B=\mathbf{B_c}$$ 

o:

$$  \begin{bmatrix}
\mathbf{t_1}\mathbf B\\
\mathbf{t_2}\mathbf B\\
\mathbf{t_3}\mathbf B\\
\end{bmatrix} = \begin{bmatrix}
1\\
0\\
0\\
\end{bmatrix}$$  

Combinando las ecuaciones anteriores se tiene que:

$$\begin{eqnarray}
\mathbf{t_3}\mathbf B &=& 0\\
\mathbf{t_2}\mathbf B &=& \mathbf{t_3}\mathbf {AB} &=& 0\\
\mathbf{t_1}\mathbf B &=& \mathbf{t_3}\mathbf {A^2B} &=& 1\\
\end{eqnarray}$$

Estas ecuaciones pueden ser escritas de la siguiente manera:

$$\mathbf{t_3}\left[\mathbf B\quad \mathbf{AB}\quad \mathbf{A^2B}\right] = \left[0\quad 0 \quad 1 \right]$$

$$\mathbf{t_3}=[0\quad 0 \quad 1]\mathcal{C}^{-1}$$

donde $\mathcal C$ es la matriz de controlabilidad, con $\mathcal C = \left[\mathbf B\quad \mathbf{AB}\quad 
\mathbf{A^2B}\right]$. 

Obteniendo $\mathbf{t_3}$ podemos obetner el resto de las filas de $\mathbf{T^{-1}}$.

Por lo tanto, en general para un sistema de orden $n$, la matriz de controlabilidad es:

$$\mathcal C =\left[ \mathbf{B}\quad\mathbf{AB}\quad\mathbf{A^2B}\quad\dots\quad\mathbf{A^{n-1}B}\right]$$

Por lo tanto, la última columna de la matriz $\mathbf{T^{-1}}$ resulta:

$$\mathbf{t_n}=\left[0\quad 0\quad\dots\quad 1\right]\mathcal C^{-1}$$

La matriz $T^{-1}$  se construye como:

$$
\mathbf{T^{-1}}=\begin{bmatrix}
\mathbf{t_n}\mathbf{A^{n-1}}\\
\mathbf{t_n}\mathbf{A^{n-2}}\\
\vdots\\
\mathbf{t_n}\\
\end{bmatrix}
$$

+++ {"colab_type": "text", "id": "pn1SahVMhklp"}

## Definición:
**Un sistema es controlable si existe su forma canónica de controlabilidad.**

Podemos ver de las ecuaciones anteriores que solamente podremos obtener $\mathbf{T^{-1}}$ y por ende $\mathbf{T}$, si existe $\mathcal{C}^{-1}$. Para esto tenemos que asegurar que el rango de $\mathcal C$ sea igual al orden del sistema $n$.

Es importante notar que al definir la controlabilidad no depende de la matriz $\mathbf{C}$, sino que depende solo de la matriz $\mathbf{A}$ y $\mathbf{B}$.

La matriz $\mathbf{B}$ es la relacionada con las entradas del sistema. Nada tiene que ver con las salidas. En caso del que el sistema no sea contrlable será necesario rediseñar la forma en que actuamos sobre del sistema. Nada resolveremos respecto a la controlabilidad cambiando, mejorando o agregando mediciones.

+++ {"colab_type": "text", "id": "1BgZ-8CShklq"}

# Transformación a la forma canónica de observabilidad

+++ {"colab_type": "text", "id": "uPxBoPc4hklr"}

La matrices de un sistema de orden 3 lineal e invariente en el tiempo representado mediante su forma canónica de observabildad tiene la forma:

$$
\mathbf{A_o} = \begin{bmatrix}
-a_1&1&0\\
-a_2&0&1\\
-a_3&0&0\\
\end{bmatrix},  \qquad \mathbf{B_o}=\begin{bmatrix}
b_1\\
b_2\\
b_3\\
\end{bmatrix}$$

$$
\mathbf{C_o}=\begin{bmatrix}
1&0&0
\end{bmatrix}, \qquad D_o=\begin{bmatrix}0\end{bmatrix}$$

+++ {"colab_type": "text", "id": "DFzXyEI9hkls"}

Como vimos anteriormente, una transformación lineal mediante la matriz $\mathbf{T}$, que hace:

$$\mathbf{x}=\mathbf{Tz}$$

+++ {"colab_type": "text", "id": "T3pTcXxXhklt"}

Esto transforma a mi sistema en:

$$
\begin{eqnarray}
\bar{\mathbf{A}} &=& \mathbf{T^{-1} A T}\\
\bar{\mathbf{B}} &=& \mathbf{T^{-1} B}\\
\bar{\mathbf{C}} &=&\mathbf{CT}\\
\bar D &=& D
\end{eqnarray}
$$

+++ {"colab_type": "text", "id": "Q8BmADcVhklu"}

Como queremos obtener el forma canónica de observabilidad llamamos $\mathbf{\bar A} = \mathbf{A_o}$, $\mathbf{\bar B} =  \mathbf{B_o}$, $\mathbf{\bar C} = \mathbf{C_o}$ y a $\bar D = D_o$. 

De las ecuaciones de la transformación tenemos:

$$\mathbf{TA_o}=\mathbf{AT}$$

Escribiendo $\mathbf{T}$ como:

$$
\mathbf{T}=\begin{bmatrix}
\mathbf{t_1}&\mathbf{t_2}&\mathbf{t_3}
\end{bmatrix}$$

donde $\mathbf{t_1}, \mathbf{t_2}, \mathbf{t_3}$ son vectores columnas que se corresponden con las columnas de $\mathbf{T}$.

+++ {"colab_type": "text", "id": "EQt9lV8uhklv"}

De esta manera tenemos que:

$$
\begin{bmatrix}
\mathbf{t_1}&\mathbf{t_2}&\mathbf{t_3}
\end{bmatrix}\begin{bmatrix}
-a_1&1&0\\
-a_2&0&1\\
-a_3&0&0\\
\end{bmatrix}=\begin{bmatrix}
\mathbf{At_1}&\mathbf{At_2}&\mathbf{At_3}
\end{bmatrix}$$

+++ {"colab_type": "text", "id": "bJGgX5D7hklw"}

De esta manera podemos obtener las siguientes igualdades:

$$
\left.\begin{array}{lll}
\mathbf{t_1} &=& \mathbf{At_2}\\
\mathbf{t_2} &=& \mathbf{At_3}\end{array}\right\}\implies \mathbf{t_1} =\mathbf{A^2t_3}$$

+++ {"colab_type": "text", "id": "BI3_sqnQhklx"}

Usando la ecuación de la transformación de la matriz $\mathbf{C_o=CT}$, se tiene que:

$$\begin{bmatrix}
1&0&0
\end{bmatrix}=\begin{bmatrix}
\mathbf{Ct_1}&\mathbf{Ct_2}&\mathbf{Ct_3}
\end{bmatrix}=\begin{bmatrix}
\mathbf{CA}^2\mathbf{t_3}&\mathbf{CAt_3}&\mathbf{Ct_3}
\end{bmatrix}$$

+++ {"colab_type": "text", "id": "1PELvtrDhkly"}

Esto lo podemos reordenar como un sistema de ecuaciones en forma matricial de la siguiente manera:

$$\begin{bmatrix}
\mathbf{C}\\
\mathbf{CA}\\
\mathbf{CA}^2
\end{bmatrix}\mathbf{t_3} = \begin{bmatrix}
0\\
0\\
1
\end{bmatrix}$$

+++ {"colab_type": "text", "id": "MoNibKachklz"}

Llamando a la matriz de observabilidad 

$$\mathcal{O}=\begin{bmatrix}
\mathbf{C}\\
\mathbf{CA}\\
\mathbf{CA}^2
\end{bmatrix}$$

podemos obtener $\mathbf{t_3}$ que esla última columna de la matriz de transformación $\mathbf{T}$, y con esta la otras columnas de la matriz de transformación.

+++ {"colab_type": "text", "id": "uK19iQSVhkl0"}

En general para un sistema de orden $n$, la matriz $\mathcal{O}$ resulta

$$\mathcal{O}=\begin{bmatrix}
\mathbf{C}\\
\mathbf{CA}\\
\vdots\\
\mathbf{CA}^{n-1}
\end{bmatrix}$$

y la última columna de la matriz de transformación resulta:

$$\mathbf{t_n} = \mathcal{O}^{-1}\begin{bmatrix}
0\\
0\\
\vdots\\
1
\end{bmatrix}
$$

+++ {"colab_type": "text", "id": "Lj-Sy0Gzhkl1"}

## Definición:
**Un sistema es observable si existe su forma canónica de observabilidad.**

Podemos ver de las ecuaciones anteriores que solamente podremos obtener $\mathbf{T}$ si existe $\mathcal{O}^{-1}$. Para esto tenemos que asegurar que el rango de $\mathcal O$ sea igual al orden del sistema $n$.

Es importante notar que definir la obervabilidad no depende de la matriz $\mathbf{B}$, sino que depende solo de la matriz $\mathbf{A}$ y $\mathbf{C}$.

La matriz $\mathbf{C}$ es la relacionada con las salidas del sistema. Nada tiene que ver con las entradas. En caso del que el sistema no sea observable será necesario rediseñar la forma en que tomamos las mediciones del sistema. Nada resolveremos respecto a la observabilidad modificando los actuadores.

+++ {"colab_type": "text", "id": "GDEfgM0vhkl2"}

## Ejemplo masa resorte: obtener la forma canónica de observabilidad y con matriz de transformación T

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: zRh6NAAShkl3
:tags: [remove-cell]

import control as ctrl
import numpy as np
```

+++ {"colab_type": "text", "id": "iLudHvyqhkl9"}

Definimos los parámetros del sistema

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: mjstqLOJhkl-

b=20
k=10
m=1
```

+++ {"colab_type": "text", "id": "7C3ENjWihkmC"}

Definimos las matrices del sistema a paritr de las ecaciones diferenciales:

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: 3N3_H61_hkmD
:outputId: dc69f636-e993-486e-f041-761a5cdb9869

A=np.array([[0,1],
   [-k/m, -b/m]])

B=np.array([[0,1/m ]]).T
C=np.array([[1,0]])
D=np.array([0])
sys = ctrl.ss(A,B,C,D)
sys
```

+++ {"colab_type": "text", "id": "qyH_eXeVhkmL"}

Para obetener la forma canónica de observabildiad debemos obetner la matriz $\mathcal{O}$. Como el sistema es de orden 2 es:
$$\mathcal{O}=\begin{bmatrix}
\mathbf C\\
\mathbf{CA}
\end{bmatrix}$$

+++ {"colab_type": "text", "id": "_1FGwSgFhkmM"}

Apilamos verticalmente $\mathbf C$ y $\mathbf{CA}$

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: j931A9hvhkmO
:outputId: 60a04ce5-dfab-4437-a1c1-52523cfc7682

O=np.vstack((sys.C, sys.C@sys.A))
O
```

+++ {"colab_type": "text", "id": "gjIXEvO_hkmS"}

Ahora calculamos la última columna de $\mathbf T$.

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: pb67wP_ShkmT
:outputId: 43a06e98-6b2f-4c89-ef04-2a5cc2c76fb1

t2=np.linalg.inv(O)*np.matrix("0;1")
t2
```

+++ {"colab_type": "text", "id": "TFO-1IaChkmX"}

Calculamos la columna $\mathbf {t_1}$

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: 2kMD7LpPhkmY

t1=A@t2
```

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: IrPFVO1Ohkmc
:outputId: 9a416f72-8a05-46db-d5df-490831ae43d2

t1
```

+++ {"colab_type": "text", "id": "VMOs9Hz1hkmj"}

Apilamos horizontalmente $\mathbf{t_1}$ y $\mathbf{t_2}$.

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: nqdojy6khkmj

T=np.hstack((t1,t2))
T
```

```{code-cell} ipython3
invT=np.linalg.inv(T)
invT
```

+++ {"colab_type": "text", "id": "QEcxE8wjhkmn"}

Finalmente calculamos las matrices del sistema transformado:

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: HtIhLaL4hkmo

Ao=invT@sys.A@T
Bo=invT@B
Co=sys.C@T
Do=D
```

+++ {"colab_type": "text", "id": "8nO6SeK9hkmr"}

Podemos verificar que las funciones transferencias del sistema antes de transformar y después de transformarlo son las mismas:

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: 7qM4yHLJhkms

sys_o=ctrl.ss(Ao,Bo,Co,Do)
sys_o
```

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: GScJZIX-hkmx
:outputId: e529817e-53f3-47fb-8f8d-14c1de4ca0d5

print("sistema sin transformar:",ctrl.tf(sys),"sistema en su forma canónica de observabilidad:", ctrl.tf(sys_o))
```

+++ {"colab_type": "text", "id": "nzL0yFFjhkm1"}

## Obtención de la forma canónica de controlabilidad

+++ {"colab_type": "text", "id": "6zZRo3Vbhkm1"}

Para obetener la forma canónica de controlabilidad debemos obetner la matriz $\mathcal{C}$. Como el sistema es de orden 2 es:
$$\mathcal{C}=\begin{bmatrix}
\mathbf B & \mathbf{AB}
\end{bmatrix}$$

Apilamos horizontalmente $\mathbf B$ y $\mathbf{AB}$

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: zvdA4-6Shkm2
:outputId: 11cea158-f8e2-44ba-bba7-b97118f6271a

Con=np.hstack((sys.B,sys.A@sys.B))
Con
```

+++ {"colab_type": "text", "id": "H-iXcKunhkm7"}

Ahora calculamos la última fila de $\mathbf{T}^{-1}$, $\mathbf{t2}$

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: WtE_kPFlhkm8
:outputId: 65e6103d-0e7d-4d2d-a950-5b4fc390146a

t2=np.matrix([[0,1]])*np.linalg.inv(Con)
t2
```

+++ {"colab_type": "text", "id": "owT0QfNchkm_"}

Calculamos la fila $\mathbf {t_1}$

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: xI9s68RXhknA

t1=t2@A
```

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: Rt_KqFquhknE
:outputId: efea1c40-dd73-434a-b5ca-8359ffbcb60c

t1
```

+++ {"colab_type": "text", "id": "IQf03x8ChknH"}

Apilamos verticalmente $\mathbf{t_1}$ y $\mathbf{t_2}$.

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: V_UCAFa-hknI

invT=np.vstack((t1,t2))
T=np.linalg.inv(invT)
```

+++ {"colab_type": "text", "id": "n_EgeFhMhknL"}

Finalmente calculamos las matrices del sistema transformado:

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: T4aSM2TchknM

Ac=invT*sys.A*T
Bc=invT@B
Cc=sys.C@T
Dc=D
```

+++ {"colab_type": "text", "id": "3-YSMsdHhknQ"}

Podemos verificar que las funciones transferencias del sistema antes de transformar y después de transformarlo son las mismas:

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: 708G63SvhknQ

sys_c=ctrl.ss(Ac,Bc,Cc,Dc)
```

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: ZOq714IshknX
:outputId: 2f59fb73-d2db-4966-ce46-1c8731844947

print("sistema sin transformar:",ctrl.tf(sys),"sistema en su forma canónica de controlabilidad:", ctrl.tf(sys_c))
```

+++ {"colab_type": "text", "id": "GrlvgGo7hknc"}

## Transformación a la forma canónica modal:

Veremos solo el caso de autovalores reales simples.

### Definición.

Sea la matriz $\mathbf{A} \in \Bbb R^{n\times n}$. Diremos que  $\lambda \in \Bbb K (= \Bbb R\text{ o } \Bbb C)$ es un autovalor de $\mathbf{A}$ si existe un vector $\mathbf{v} \in \Bbb K^n$, con $\mathbf v \neq 0$ tal que:

$$\mathbf{Av}=\lambda \mathbf{v}$$

en cuyo caso se dice que $\mathbf{v}$ es un autovector asociado al autovalor $\lambda$.

+++ {"colab_type": "text", "id": "FlBmm0L1hknd"}

Suponiendo que $\mathbf A$ tienen $n$ autovalores diferentes, entonces podemos escribir en forma matricial $n$ ecuaciones para los $n$ pares autovalores-autovectores

+++ {"colab_type": "text", "id": "vwHIusJlhkne"}

$$
\begin{bmatrix}
\mathbf{v_1}&\mathbf{v_2}&\mathbf{v_3}
\end{bmatrix}\begin{bmatrix}
\lambda_1&0&0\\
0&\lambda_2&0\\
0&0&\lambda_3\\
\end{bmatrix}=\mathbf A\begin{bmatrix}
\mathbf{v_1}&\mathbf{v_2}&\mathbf{v_3}
\end{bmatrix}$$

+++ {"colab_type": "text", "id": "Jg5eGPDehkne"}

Si hacemos que:
$$\mathbf{T}=\begin{bmatrix}
\mathbf{v_1}&\mathbf{v_2}&\mathbf{v_3}
\end{bmatrix}$$
tenemos que:
$$\begin{bmatrix}
\lambda_1&0&0\\
0&\lambda_2&0\\
0&0&\lambda_3\\
\end{bmatrix}=\mathbf{T}^{-1}\mathbf{A T}$$


donde:
$$\mathbf{A_m}=\begin{bmatrix}
\lambda_1&0&0\\
0&\lambda_2&0\\
0&0&\lambda_3\\
\end{bmatrix}$$

Nuevamente $\mathbf{B_m}$ se obtiene como $\mathbf{B_m}=\mathbf{T}^{-1}\mathbf{B}$ y $\mathbf{C_m}=\mathbf{CT}$ 

La forma canónica modal tiene la particularidad de independizar los estados unos de otros. Es decir, cada estado se conecta solo con la entrada y con la salida y no se conectan entre si (cada estado no depende de otro estado).

Esta formca canónica nos da la posibilidad de estudiar controlabilidad y observabilidad sin pasar por las matrices $\mathcal C$ y $\mathcal O$. 

Si todos los estados están conectados con la entrada entonces el sistema es controlable. Para que se de esto, la matriz $\mathbf{B_m}$  tiene que tener todas sus componentes distintas de 0.

Si todos los estados están conectados con la salida entonces el sistema es observable. Para que se de esto, la matriz $\mathbf{C_m}$ tiene que tener todas sus componentes distintas de 0.

+++ {"colab_type": "text", "id": "fg05YWSVhknf"}

## Ejemplo de tranformación a la forma canónica modal

La matriz de transformación son los autovectores. 

El módulo linalg de numpy tiene una función que se llama eig, que los devuelve los autovectores y autovalores. Los autovalores lo devuelve en forma de ndarray y luego devuevlo los atuvalores como un array. Vamos a utilizar esta función para calcular la matriz de transformación $T$. Los autovalores los vamos a usar para verificar que luego de aplicar la transformación la matriz $A_m$ resulte ser diagonal con los autovalores en la diagonal.

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: L9IEG9Qyhkng
:outputId: 81c46788-7c7b-44e7-b473-084a4ce216cf

lamb,v=np.linalg.eig(A)
print("autovectores:\n ", v)
print("autovalores:\n ", lamb )
```

+++ {"colab_type": "text", "id": "oNmoJfqfhknm"}

La matriz de transformación T es la de los autovectores. Entonces:

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: nLfKcEXjhknm

T=v
invT=np.linalg.inv(T)
```

+++ {"colab_type": "text", "id": "hwOsTMXohknq"}

Calculamos la transformación:

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: fxCjq6Mxhknq

Am=invT@A@T
Bm=invT@B
Cm=C@T
Dm=D
```

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: ap4piO2uhknu

sys_m = ctrl.ss(Am,Bm,Cm,Dm)
```

```{code-cell} ipython3
:colab: {}
:colab_type: code
:id: j93Y2uuxhkny
:outputId: 69ddba01-5462-4c8e-e283-5a916083525d

sys_m
```

+++ {"colab_type": "text", "id": "eL_DZs0bhkn1"}

Obervando la matriz $\mathbf{A}$ del sistema en su forma canónica modal tiene en su diagonal lo autovalores, y fuera de esto valores igual a 0 o muy cercanos a ceros. Las diferencias con ceros son error númericos y podemos considerar que la transformación resultó correcta.

+++ {"colab_type": "text", "id": "XRRQiBAyhkn2"}

Por otro lado podemos ver que todos las componentes de B en esta forma canónica son distintos de 0, por lo que el sistema es controlable.

+++ {"colab_type": "text", "id": "pr9a5Lvxhkn3"}

Finalmente, para el sistema en la forma canónica modal, todas las componentes de C son distintas de 0,por lo que el sistema es observable.

+++ {"colab_type": "text", "id": "BZhxHf4Ihkn4"}

**Nota**:

Respecto al uso de numpy. La multiplicaión de matrices usando el * la entiende como elemento a elemento si el tipo de datos es un ndarray o un array. Si usamos ese tipo de datos, entonces para que numpy entienda multiplicación de matrices se debe usar el simbolo @.

Si el tipo de datos que se está operando es una matriz de numpy entonces la multiplicación de matrices se puede hacer con *.

**SER MUY CUIDADOSOS!!!!**

```{code-cell} ipython3

```
