---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Sonido wav en los cuadernos

```{code-cell} ipython3
:tags: [remove-input]

from scipy.io import wavfile
import IPython
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
:tags: [remove-input]

IPython.display.Audio(filename='sorohanro_-_solo-trumpet-06.wav')
```

```{code-cell} ipython3
wav=wavfile.read('sorohanro_-_solo-trumpet-06.wav')
s=np.array(wav[1])
final_time = 3.5
frequency = wav[0]
num = round(final_time*wav[0])
t=np.linspace(0., num/frequency, num)
```

```{code-cell} ipython3
:tags: [hide-input]

fig, ax = plt.subplots(1,2, figsize=(12,4))
ax[0].plot(t, s[0:num])
ax[0].set_title('Ejemplo audio: solo trompeta')
ax[0].set_xlabel('tiempo');
ax[0].set_ylabel('Amplitud de la señal')
ax[0].grid()
ax[1].plot(t, s[0:num])
ax[1].set_title('Ejemplo audio: solo trompeta')
ax[1].set_xlim([2.,2.2]);
ax[1].set_xlabel('tiempo');
ax[1].set_ylabel('Amplitud de la señal')
ax[1].grid()
fig.tight_layout()
```

```{code-cell} ipython3
fig.savefig('trumpet_sound.png')
```
