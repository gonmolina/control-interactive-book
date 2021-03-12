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
---
executionInfo:
  elapsed: 798
  status: ok
  timestamp: 1601061613590
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: C2YxmTMnkUa3
tags: [remove-cell]
---
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt
```

+++ {"id": "pNjfWDONkUa-"}

# Diseño para un motor de continua

+++ {"id": "v5bYjjrokUa_"}

Supongamos que la transferencia de nuestro sistema es:
$$G(s)=\frac{10}{s(s+2)(s+8)}$$
Diseño un controlador que ubique los polos en:
$$pc=[-1.42;\quad -1.04\pm2.14j]$$
y los del estimador tres veces más rápidos.

+++ {"id": "fwlecwjskUbA"}

Como tenemos el sistema en forma de función transferencia lo llevamos a alguna forma en espacio de estados (la que sea por defecto de Python)

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 40
executionInfo:
  elapsed: 204
  status: ok
  timestamp: 1601066354192
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: DEElFP03kUbB
outputId: ec527d4e-6096-49db-e3a2-2720cf5e4091
---
G=ctrl.tf(10,[1,10,16,0])
G
```

+++ {"id": "ck2NWiZltFkb"}

## Expresión en variables de estado

+++ {"id": "ZCX2Lsx_bjeG"}

De las formas canónicas disponibles, elegimos la forma canónica de observabilidad.

```{code-cell} ipython3
---
executionInfo:
  elapsed: 209
  status: ok
  timestamp: 1601066355517
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: IaoFQGmjx7uU
tags: [hide-output]
---
ctrl.canonical_form?
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 207
executionInfo:
  elapsed: 235
  status: ok
  timestamp: 1601066357175
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: eTyyF-0dkUbI
outputId: 143731ef-b4c6-4633-ea4d-73500b16505a
---
sys,_=ctrl.canonical_form(ctrl.ss(G),'observable')
sys
```

+++ {"id": "lL_pFIdWtUz2"}

## Ley de control y estimador completo


```{code-cell} ipython3
---
executionInfo:
  elapsed: 182
  status: ok
  timestamp: 1601066357992
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 35stRVbSkUbM
---
pc=np.array([-1.42, -1.04+2.14j,-1.04-2.14j])
pe = pc*3
```

+++ {"id": "8OGVJ_lSkm7B"}

Notar que hubiera podido escribir pc como una lista de los valores en donde quiero ubicar los polos a lazo cerrado. Sin embargo, luego no hubiera podido haer la operación de `pc*3` sobre la lista, ya que hubiera resultado en algo que no es lo que buscabamos.

+++ {"id": "SP7jOTRlkUbR"}

**Obtenemos la ley de control:**

```{code-cell} ipython3
---
executionInfo:
  elapsed: 185
  status: ok
  timestamp: 1601066361919
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: pjrTFXo9kUbS
---
K=ctrl.place(sys.A,sys.B,pc)
```

+++ {"id": "_aZofBISlFoy"}

**Obtenemos L del estimador:**

```{code-cell} ipython3
---
executionInfo:
  elapsed: 188
  status: ok
  timestamp: 1601065412554
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: GPR3nSm0kUbX
---
L=ctrl.place(sys.A.T,sys.C.T,pe).T
```

+++ {"id": "NwtaA4allMzr"}

Hemos podido utilizar el comando `place` debido a que los 3 polos tanto del estimador como de los elegidos para la ley de control son distintos. De haber querido ubicar dos polos en el mismo lugar, hubieramos tenido que usar el comando `acker`.

Sin mebargo es necesario tener en cuenta que `acker` no es recomendable para sistema de orden mayor a 4.

+++ {"id": "DJzcLBX2ts3Q"}

### Sistema controlador con estimador completo

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 42
executionInfo:
  elapsed: 131
  status: ok
  timestamp: 1601061624537
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 5lR6YIv-kUbc
outputId: 85f7f6f9-fda0-466c-ef06-6597bb582219
---
Dc=ctrl.ss(sys.A-sys.B@K-L@sys.C,L,-K,0)
ctrl.tf(Dc)
ctrl.isctime(Dc)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 136
  status: ok
  timestamp: 1601061625093
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: mMFVg9BWkUbg
outputId: 0c4c2657-0fe8-4e83-c259-f81ce4c42894
---
Dc.pole()
```

+++ {"id": "BT_0CPLakUbl"}

Podemos ver que el controlador diseñado es inestable!. Esto no es deseable.

La razones por la que no es deseable un controlador inestable  son:

1. Presenta dificultades para ser testeado, ya sea el compensador por si solo o en lazo abierto durante la puesta en funcionamiento. Sin embargo, en agunos casos, se puede lograr una mejor performance del sistema de controlado con un controlador inestable (hay casos de sistemas que ni siquiera pueden ser estabilizados con controladores estables.). En ese caso se aceptan estos incevenientes de testeo.

2. Para ganancias bajas el sistema a lazo cerrado con un controlador inestable resulta inestable (visulizar el root locus). En general, los actuadores prensetan saturaciones, es decir valor máximos de actuación. Cuando un actuador satura se ve desde el punto de vista de lazo como una reducción de la ganancia, llevando a la zona instable o acercandose a la misma.

Los sistemas que necesitan se vuelven inestables cuando su valor ganancia se reduce se los conoce como sistemas **condicionalmente estables** y **deben ser evitados** en la medida de lo posible.

+++ {"id": "jXC7vMdZkUbm"}

## Rediseñamos usando un estimador reducido

+++ {"id": "aJgzB1tWkUbn"}

Ahora pondremos los polos tal que $\omega_n=6$ rad/seg y $\zeta=0.707$


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 130
  status: ok
  timestamp: 1601061628113
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: S9ZlG-0OkUbn
outputId: b2469ee9-7d3d-406c-92b6-33a0e7d0789d
---
pe_red= np.roots([1,2*0.707*6,6**2])
pe_red
```

+++ {"id": "z6M7qlpOkUbr"}

Necesitamos las sub-matrices de A para calcular el estimadore reducido

```{code-cell} ipython3
---
executionInfo:
  elapsed: 117
  status: ok
  timestamp: 1601061628598
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 6CVGVGS6kUbs
---
Aaa=sys.A[0:1,0:1]
Aab=sys.A[0:1,1:]
Aba=sys.A[1:,0:1]
Abb=sys.A[1:,1:]

Ba = sys.B[0:1,0]
Bb = sys.B[1:,0]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 133
  status: ok
  timestamp: 1601061628836
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: mmSW8nkCkUbx
outputId: 5a7dcf36-275e-4771-b074-522bbf626649
---
Aaa
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 156
  status: ok
  timestamp: 1601061629103
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: Z36Jm24IkUb2
outputId: cda74b08-a168-49f5-a932-00ab15d775dc
---
Ltred = ctrl.place(Abb.T,Aab.T,pe_red).T
Ltred
```

+++ {"id": "IGZLjmdptkmN"}

### Sistema controlador con estimador reducido

```{code-cell} ipython3
---
executionInfo:
  elapsed: 117
  status: ok
  timestamp: 1601061631996
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: tNixGvOhkUb6
---
Ka=K[0,0:1]
Kb=K[0,1:]

Ar = Abb-Ltred@Aab-(Bb-Ltred@Ba)@Kb
Br = Ar@Ltred + Aba - Ltred@Aaa - (Bb-Ltred@Ba)@Ka
Cr = -Kb
Dr = -Ka-Kb@Ltred
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 173
executionInfo:
  elapsed: 140
  status: ok
  timestamp: 1601061632459
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: wtwYI1g9kUb9
outputId: f695be77-cf4f-408c-a46c-79e2642a9457
---
Dcr = ctrl.ss(Ar,Br,Cr,Dr)
Dcr
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 42
executionInfo:
  elapsed: 136
  status: ok
  timestamp: 1601061632844
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: S5Z2SrB8kUcC
outputId: f5bc166e-9092-4279-bd93-2d7ba06d0a01
---
ctrl.tf(Dcr)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 141
  status: ok
  timestamp: 1601061633790
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: yxH8ZsnFkUcG
outputId: cc4ec476-9c82-40ca-92eb-88f7ec955f2d
---
Dcr.pole()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 159
  status: ok
  timestamp: 1601061634482
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: BWeAryLBkUcL
outputId: c0c31b1b-1b5d-4ed1-a459-9e52349f340d
---
Dcr.zero()
```

+++ {"id": "gIvbVSEfkUcP"}

Si bien este diseño mejoró al anterior ya que el controlador resultante es estable, este presenta un problema potencialmente menos danino. El problema es que es un controlador de no mínima fase, ya que tiene un 0 en el lado derecho del plano $s$, limitando la velocidad del sistema controlado.

```{code-cell} ipython3
L=-ctrl.tf(Dcr)*G/ctrl.db2mag(6)
ctrl.bode(L,dB=True, margins=True, omega_num=2000);
plt.gcf().set_size_inches(12,8)
```

```{code-cell} ipython3
T=ctrl.feedback(L)
plt.figure()
ctrl.bode(T,dB=True);
plt.gcf().set_size_inches(12,8)
```

```{code-cell} ipython3
:tags: [remove-cell]

ctrl.gangof4_plot(G,-ctrl.tf(Dcr))
ctrl.gangof4_plot(ctrl.tf(1,[1,0]),ctrl.tf(1,1))
plt.gcf().set_size_inches(12,12)
```

```{code-cell} ipython3
_=ctrl.nyquist(L);
plt.gcf().set_size_inches(8,6)
```

+++ {"id": "-VJrPFw1otAC"}

Agragamos referencia al controlador de orden reducido. 

```{code-cell} ipython3
---
executionInfo:
  elapsed: 126
  status: ok
  timestamp: 1601061639833
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: nWB3yyE1tI-h
---
def seguimiento_referencia(sys):
    aux1=np.vstack((np.hstack((sys.A,sys.B)),
                   np.hstack((sys.C,sys.D))))
    n=np.shape(sys.A)[0]
    aux2=np.vstack((np.zeros((n,1)),[1]))
    N=np.linalg.inv(aux1)@aux2
    Nx=N[0:n]
    Nu=N[n]
    return Nx, Nu

def calculate_Nbar(Nx,Nu,K):
    return Nu+K@Nx
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 90
  status: ok
  timestamp: 1601061756872
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: aCnx2Ms-txcs
---
Nx, Nu = seguimiento_referencia(sys)
Nbar = calculate_Nbar(Nx,Nu, K)
Nbar
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 122
  status: ok
  timestamp: 1601061815774
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: -8Cw7a7kpBCO
outputId: 5c1578d4-0f36-4429-9d91-cf3357ed7466
---
N=Nbar # Lo vemos mañana como se saca
M=(Bb-Ltred@Ba)*N
M
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 173
executionInfo:
  elapsed: 141
  status: ok
  timestamp: 1601061915405
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: hsA8clZSphT_
outputId: c55eef74-0298-499e-875a-2959d7e831f6
---
Dcr_ref = ctrl.ss(Ar, np.hstack((Br,M)), Cr, np.hstack((Dr,N)))
Dcr_ref
```

+++ {"id": "xnlYaJRykUcQ"}

## Rediseño usando SRL

+++ {"id": "kNU5MoqzkUcQ"}

Vamos a diseñar el sistema para ubicar los polos de forma tal que se tenga un ancho de banda de 2.5rad/seg y que los polos del estimador esten aproximadamiente 2.5 veces más raṕido.

+++ {"id": "bnQk1tCekUcR"}

Para usar SRL vamos a tomat que $\mathbf{C} = \mathbf{C_1}$ y que $\mathbf{B} = \mathbf{B_1}$

```{code-cell} ipython3
:id: 6I-HAPcYkUcR

def conjugate_tf(G):
    num = ctrl.tf(G).num[0][0]
    den = ctrl.tf(G).den[0][0]
    nume = [num[i]*((-1)**(len(num)%2+1-i)) for i in range(0, len(num))]
    dene = [den[i]*((-1)**(len(den)%2+1-i)) for i in range(0, len(den))]
    return ctrl.tf(nume,dene)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 39
executionInfo:
  elapsed: 91
  status: ok
  timestamp: 1600975647827
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: sp9MJld-shkt
outputId: 1b55d12a-8c3d-4159-cc62-fc7a064e94f7
---
Gm=conjugate_tf(G)
Gm
```

```{code-cell} ipython3
:id: UYbi7FCnkUcV

_=ctrl.rlocus(G*Gm)
plt.gcf().set_size_inches(8,6)
```

+++ {"id": "27hDxbKRkUcY"}

Con $K=26$ obtenemos los polos con una frecuenca de corte de 2.5 rad/seg.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 97
  status: ok
  timestamp: 1600975661115
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: ZrxfY0bwkUcZ
outputId: 0594025a-2d54-4c23-b92e-fc26b48c8fa2
---
pc,_=ctrl.rlocus(G*conjugate_tf(G),kvect=[26],Plot=False)
pc = pc[pc.real<0]
pc
```

+++ {"id": "UIqZ2COCkUcc"}

Y con K=1350 tenemos los polos del estimador.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 129
  status: ok
  timestamp: 1600975662387
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: GpVx_qsBkUcd
outputId: 49af759f-1117-49f8-cf15-d9981db1203b
---
pe,_=ctrl.rlocus(G*conjugate_tf(G),kvect=[1350],Plot=False)
pe = pe[pe.real<0]
pe
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 72
executionInfo:
  elapsed: 106
  status: ok
  timestamp: 1600975663050
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: ZAU6vH6NkUcg
outputId: 4525f9f1-f306-4ee6-d738-7119db8cce4a
---
print("Polos de la ley de control: ",pc)
print("Polos del estimador: ",pe)
```

```{code-cell} ipython3
:id: yJRkFBptkUck

K=ctrl.place(sys.A,sys.B,pc)
L=ctrl.place(sys.A.T,sys.C.T,pe).T
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 41
executionInfo:
  elapsed: 85
  status: ok
  timestamp: 1600975664779
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: Qtb9laB3kUcp
outputId: 069faced-0c1a-401b-d8f9-207e2e6de38f
---
Dcsrl=ctrl.ss(sys.A-sys.B@K-L@sys.C,L,-K,0)
ctrl.tf(Dcsrl)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 81
  status: ok
  timestamp: 1600975669015
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: tMLrdU2ZkUct
outputId: f6dd59e2-bc77-4f78-a2ed-204b8310bdbf
---
Dcsrl.pole()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 76
  status: ok
  timestamp: 1600975670237
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 7GvVnY4RkUcx
outputId: d8ceb104-e231-4181-f283-9b6f2515b2a2
---
Dcsrl.zero()
```

```{code-cell} ipython3
:id: IuQl5nJwkUc0

_=ctrl.bode((-sys*Dc,-sys*Dcr,-sys*Dcsrl),omega_limits=(1e-2,1e2),dB=True)
plt.gcf().set_size_inches(12,8)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 69
executionInfo:
  elapsed: 97
  status: ok
  timestamp: 1600975672255
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: IpTdYQNykUc4
outputId: ec4135e0-4f1a-401e-f641-7d26efee4c13
---
print(ctrl.margin(-sys*Dc))
print(ctrl.margin(-sys*Dcr))
print(ctrl.margin(-sys*Dcsrl))
```

```{code-cell} ipython3
:id: UtrD_mUEkUc8

T1=ctrl.feedback(-sys*Dc)
T2=ctrl.feedback(-sys*Dcr)
T3=ctrl.feedback(-sys*Dcsrl)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 104
executionInfo:
  elapsed: 113
  status: ok
  timestamp: 1600975921642
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: ZASkbVMSuHrt
outputId: c6883ac8-0846-4e93-fe55-d26bbac04bdb
---
print(f"Los polos de T1 son: {T1.pole()}")
print(f"Los polos de T2 son: {T2.pole()}")
print(f"Los polos de T3 son: {T3.pole()}")
```

+++ {"id": "OOewQwPNvU2S"}

### Respuesta al escalón del sistema "controlado" (a partir de una salida distinta de 0)

```{code-cell} ipython3
:id: 2XXJ3s_wuGbN

t1,y1 = ctrl.initial_response(T1, X0=np.matrix([0,0,0,-1,0,0]).T,T=np.linspace(0,5,1000))
t2,y2 = ctrl.initial_response(T2, X0=np.matrix([0,0,-1,0,0]).T,T=np.linspace(0,5,1000))
t3,y3 = ctrl.initial_response(T3, X0=np.matrix([0,0,0,-1,0,0]).T,T=np.linspace(0,5,1000))
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 430
executionInfo:
  elapsed: 356
  status: ok
  timestamp: 1600975942871
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: -kfJ70e2kUc_
outputId: 7f830759-1289-4692-b796-5156d89b9c5b
tags: [hide-input]
---
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t1,y1,label="T1")
ax.plot(t2,y2,label="T2")
ax.plot(t3,y3,label="T3")
plt.legend()
ax.set_title('Respuesta a condiciones iniciales')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Salida")
ax.grid()
```

+++ {"id": "b85hR1QlyvH2"}

## Conxión de sistemas entrada/salida

+++ {"id": "r-5qTqXZy75T"}

Podemos ver en el caso anterior que mediante el uso de la función ctrl.feedback hemos perdido, al menos parcialmente, saber de que manera estan ordenados los estados del sistema.

Par aun mayor control de como están ubicados los eatados, las entradas y la salidas es conveniente usar la función `ctrl.append` y `ctrl.connect`.

```{code-cell} ipython3
:id: cWT1nwst7qSH
:tags: [hide-output]

ctrl.connect?
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 243
executionInfo:
  elapsed: 91
  status: ok
  timestamp: 1600976148231
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 0p5DCavSL3kk
outputId: 51d752d1-cca9-45c9-9900-491a2cc97897
---
sys_conectado_1 = ctrl.connect(ctrl.append(sys,Dc),
                               [[1,2],[2,1]],[1],[1,2])
sys_conectado_1
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 225
executionInfo:
  elapsed: 84
  status: ok
  timestamp: 1600976174487
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 0_vRmFzT1Kaj
outputId: 5097e786-b0b5-458f-dc64-18bbe686160e
---
sys_conectado_2 = ctrl.connect(ctrl.append(sys,Dcr),[[1,2],[2,1]],[1],[1,2])
sys_conectado_2
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 347
executionInfo:
  elapsed: 84
  status: ok
  timestamp: 1600976189652
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: RG6KpNo71fMO
outputId: 8cf148f1-17e1-4ccd-c784-1335e1fcede1
---
sys_conectado_3 = ctrl.connect(ctrl.append(sys, Dcsrl), [[1,2], [2,1]], [1], [1,2])
sys_conectado_3
```

+++ {"id": "7GGfr40J6aWe"}

La manera en que `ctrl.connect` trabaja es:

1. El primer argumento es un sistema de muchas entradas y muchas salidas que se tienen que interconectar. Para esto, agrupamos todos los sistemas que queremos interconectar mediante la función `ctrl.append`. Esta función nos va a devolver un único sistema en general de muchas entradas y muchas salidas.

2. El segundo argumento es una matriz de interconexión, donde cada fila nos dice que entrada se conecta con que salida. Las entradas y las salidas quedan ordenadas según el orden que hayamos puesto en la función `ctrl.append`, y están númeradas a partir de 1.

3. El tercer argumento, nos dice que entradas van a ser tomadas como entradas del sistema.

4. El cuarto y último argumento son las salidas del sistema.

+++ {"id": "ka77Rz1x8CVa"}

Revisemos la utilización de `ctrl.connect` en nuetro ejemplo:

1. El primer argumento es un sistema construído a partir de `ctrl.append` que incluye a `sys` (la planta que queremos controlar) y a `Dc` (el controlador). Esta función nos va a devoler un sistema cuyos primeros 3 estados serán los estados de `sys` y los restantes son los del observador; tendrá dos donde la primer entrada es la de `sys` y la segunda entrada es la de `Dc`; y la primer salida es la de `sys` y la segunda salida es la de `Dc`.

2. El segundo argumento es la matriz de interconexión. Primero conecto la entrada de `sys` con la salida de `Dc`. Como `sys` en `ctrl.append` está primero, la entrada 1 corresponde a la de `sys` y la salida 2 corresponde a la salida de `Dc`. De esta manera tenemos la primer fila de `Q`. La segunda fila de `Q` conecta la entrada de `Dc` con la salida de `sys`.

3. El sistema que estamos generando no tiene entradas, pero el módulo de control tiene algunos problemas en sistemas que notienen entradas o que no tiene salidas, por eso el tercer argumento vamos a poner [1], que significa una entrada que se sumará a la salida de `Dc` en la entrada de `sys`.

4. El último argumento son las salidas. Voy a tomar como salidas de mi sistema el esfuerzo de control, es decir la salida del sistema `Dc`, y la salida de la planta, es decir la salida de `sys`.

+++ {"id": "qzLJto6U_Opj"}

Vamos a realizar nuevamente las simulaciones con los sistemas definidos mediante el connect.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 703
executionInfo:
  elapsed: 110
  status: error
  timestamp: 1600976196686
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: -Fm-3l-j1s86
outputId: 1c9bd191-80df-45b8-ca77-2b83c14e7d81
---
t1,y1 = ctrl.initial_response(sys_conectado_1, X0=np.matrix([1,0,0,0,0,0]).T,T=np.linspace(0,5,1000))
t2,y2 = ctrl.initial_response(sys_conectado_2, X0=np.matrix([1,0,0,0,0]).T,T=np.linspace(0,5,1000))
t3,y3 = ctrl.initial_response(sys_conectado_3, X0=np.matrix([1,0,0,0,0,0]).T,T=np.linspace(0,5,1000))
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 703
executionInfo:
  elapsed: 110
  status: error
  timestamp: 1600976196686
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: -Fm-3l-j1s86
outputId: 1c9bd191-80df-45b8-ca77-2b83c14e7d81
---
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t1,y1[0,:],label="sys conectado 1")
ax.plot(t2,y2[0,:],label="sys conectado 2")
ax.plot(t3,y3[0,:],label="sys conectado 3")
plt.legend()
ax.set_title('Respuesta a condiciones iniciales')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Salida")
ax.grid()
```

+++ {"id": "224fcVeYO3Ya"}

Podemos también mirar el esfuerzo de control, ya que es salida de la planta.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 430
executionInfo:
  elapsed: 466
  status: ok
  timestamp: 1600885884174
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: _WxxKQsg_haz
outputId: 2eb3b46e-547d-4106-c581-8f9595f2107e
---
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t1,y1[1,:],label="sys conectado 1")
ax.plot(t2,y2[1,:],label="sys conectado 2")
ax.plot(t3,y3[1,:],label="sys conectado 3")
plt.legend()
ax.set_title('Respuesta a condiciones iniciales')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Esfuerzp de control")
ax.grid()
```

+++ {"id": "4-G2F9KzPHeD"}

Este ejemplo muestra claramente como la elección de los polos usando cirterios de optimización como son los de lugar simétrico de las ráices nos da un control mucho mejor, tanto en tiempo de respuesta como en el esfuerzo de control.

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 89
  status: ok
  timestamp: 1601061963921
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: mUQ4gHl6PAK-
outputId: cf7f98c7-9e0d-444c-9045-424220b97616
---
psys_controlado_con_ref = ctrl.connect(ctrl.append(sys,Dcr_ref), [[1, 2],[2,1]], [3], [1,2])
psys_controlado_con_ref.pole()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 87
  status: ok
  timestamp: 1601062068231
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: nroB82_4utfJ
outputId: 6d7d49a6-3d4a-48e1-a442-996cc8f63705
---
ctrl.dcgain(psys_controlado_con_ref)
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 115
  status: ok
  timestamp: 1601062019233
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: OCJ6-IvDqicE
---
t,y = ctrl.step_response(psys_controlado_con_ref)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 117
  status: ok
  timestamp: 1601062116626
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 3iImUh49uVgf
outputId: 8da72d94-5f66-44d6-af35-e56f3a6ed380
---
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t,y[0,:],label="psys conectado con ref")
ax.set_title('Respuesta al escalón en la referencia')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Salida")
ax.grid()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 128
  status: ok
  timestamp: 1601062130311
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 0Z2CTQWJuaKh
outputId: 60ed8471-71f1-45e6-b17c-fe12f462224a
---
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t,y[1,:],label="psys conectado con ref")
ax.set_title('Respuesta al escalón en la referencia')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Esfuerzo de control")
ax.grid()
```

+++ {"id": "MvRx1V1S2TnA"}

## Control integral y estimador de orden completo

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 69
executionInfo:
  elapsed: 91
  status: ok
  timestamp: 1601064254755
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: 5XEsY1w03VID
outputId: 3e24bb96-0aa7-4bdd-a6a3-27a32e14831e
---
np.hstack((np.zeros((1,1)), sys.C))
np.hstack((np.zeros((3,1)), sys.A))
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 86
executionInfo:
  elapsed: 137
  status: ok
  timestamp: 1601067258375
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: _ZyQvnrx2Swj
outputId: aaee9f45-edec-4458-c91a-b13b6c16a2cc
---
Au=np.vstack((np.hstack((np.zeros((1,1)), sys.C)),
              np.hstack((np.zeros((3,1)), sys.A))))
Au
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 86
executionInfo:
  elapsed: 124
  status: ok
  timestamp: 1601067260230
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: HDLxcWv32Zcp
outputId: 08459074-5a2d-4f4f-8971-a790a841b4c2
---
Bu = np.vstack((0,sys.B))
Bu
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 121
  status: ok
  timestamp: 1601067278136
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: xTjVE_VV4Fyd
outputId: 53c42b25-7d44-4edd-a92a-6bc09917ec85
---

Ku = ctrl.place(Au,Bu, np.array([-1.42, -1.04+2.14j,-1.04-2.14j, -3])) 
Ku
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 89
  status: ok
  timestamp: 1601064658307
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: e83Oos2L4wHu
outputId: 795bc121-f660-4ad2-e43e-f84f668e48a9
---
Ki=Ku[0,0]
Ki
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 138
executionInfo:
  elapsed: 171
  status: ok
  timestamp: 1601066269611
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: W51VcJ0p46dv
outputId: 204a55ec-734b-4811-fca2-648638db3154
---
integrador=ctrl.ss([[0]],[[Ki,-Ki]],[1],[0, 0])
integrador
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 69
executionInfo:
  elapsed: 61
  status: ok
  timestamp: 1601067364768
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: GqECqPKz5lsy
outputId: f9109784-4fa7-431e-aab4-ab0acc349ab0
---
###  Estimado  mas ley de control

L=ctrl.place(sys.A.T, sys.C.T, np.array([-1.42, -1.04+2.14j,-1.04-2.14j])*3).T
L
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 69
executionInfo:
  elapsed: 93
  status: ok
  timestamp: 1601067365280
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: s8sJaVhB7q4h
outputId: bb5821b4-cf52-4b10-82d5-ece890af7896
---
Ae=sys.A-L@sys.C
Ae
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 69
executionInfo:
  elapsed: 94
  status: ok
  timestamp: 1601067365912
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: KP1zSKxc7xW3
outputId: 7cdc84d0-a3ce-4747-8989-3bb351c9a991
---
Be=np.hstack((L,sys.B))
Be
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 85
  status: ok
  timestamp: 1601067366792
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: Hdl8n3i58IVH
outputId: 14499339-d225-4f93-b3b8-82abaa9f5167
---
Ce=-Ku[0,1:]
Ce
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 148
  status: ok
  timestamp: 1601066272646
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: LZmu2ztl8kEe
tags: [hide-output]
---
De=0
estim = ctrl.ss(Ae,Be,Ce,0)
estim
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 123
  status: ok
  timestamp: 1601069598163
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: s5yGIPBR86ME
tags: [hide-output]
---
planta_controlada = ctrl.connect(ctrl.append(sys, estim, integrador), 
                                 [[1,2],[1,3],[2,1],[3,2],[3,3],[5,1]],[4],[1,2,3])
planta_controlada
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 146
  status: ok
  timestamp: 1601069601080
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: rbAlftZN9iqa
---
t,y = ctrl.step_response(planta_controlada)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 118
  status: ok
  timestamp: 1601069602083
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: xyw-x2pr9tg5
outputId: f909c522-af22-4b3e-a58b-ab29e5ca0a03
tags: [hide-input]
---
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t,y[0,:],label="psys conectado con ref")
ax.set_title('Respuesta al escalón en la referencia')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Salida")
ax.grid()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 52
executionInfo:
  elapsed: 98
  status: ok
  timestamp: 1601069608244
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: YApZZWyD9vSw
outputId: 3ad7cb80-dacb-4b7f-b336-fa54add3112a
---
planta_controlada.pole()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 108
  status: ok
  timestamp: 1601070775243
  user:
    displayName: gonzalo molina
    photoUrl: ''
    userId: 03146719216223860883
  user_tz: 180
id: VroD8-gpCUGv
outputId: 7c68b395-7c4e-4da5-afed-dbb32c8c87b9
---
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(t,y[1,:],label="psys conectado con ref")
ax.set_title('Respuesta al escalón en la referencia')
ax.set_xlabel("Tiempo")
ax.set_ylabel("Esfuerzo de control")
ax.grid()
```
