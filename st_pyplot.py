"""
Curso Básico de Python para CTIM
PDVSA Intevep
Instructor: Jorge Luis Rojas D'Onofrio
"""

"""
Lección 12

Primera parte
"""

import streamlit as st
from matplotlib import pyplot
import math
fig, ax = pyplot.subplots()
x = [i*0.01 for i in range(-500, 500)]
y = [math.sin(i) for i in x]
y2 = [math.sin(i - 2) for i in x]
y3 = [1.0/3*math.sin(i)*math.sin(25*i) for i in x]
ax.plot(x,y, label='seno')
ax.plot(x,y2, label='seno desfasado')
ax.plot(x,y3, label='senal modulada')
#ax.xlabel('Abcisas')
#ax.ylabel('Ordenadas')
ax.set_title('Grafica')
ax.legend(loc='center left', bbox_to_anchor=(0.6, -0.22))
st.pyplot(fig)
