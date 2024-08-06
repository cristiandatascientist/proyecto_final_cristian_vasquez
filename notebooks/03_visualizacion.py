#!/usr/bin/env python
# coding: utf-8

# ### Visualización

# In[ ]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


df_combinado = pd.read_csv('ds_combinado.csv')


# In[ ]:


df_combinado.info()


# In[ ]:


df_combinado['Date']


# In[ ]:


df_combinado['Date'] = pd.to_datetime(df_combinado['Date'], format='%Y-%m-%d %H:%M:%S')


# In[ ]:


df_combinado.info()


# ### la variable 'Gramaje_pope' es el gramaje de la hoja de papel fabricado. Se mide en g/m², y es una variable crítica que interesa controlar

# #### visualización del gramaje pope en el tiempo
# 
# Se observa un comportamieto ciclico que puede ser explicado por los distindos grados de fabricación

# In[ ]:


plt.figure(figsize=(10, 6))
plt.plot(df_combinado['Date'], df_combinado['Gramaje_pope'])
plt.grid(True, linewidth=0.2, color='gray')
plt.title('Gramaje pope')
plt.xlabel('Fecha')
plt.ylabel('Gramaje g/m²')
plt.show()


# In[ ]:


grado_gramaje_mean = df_combinado.groupby('Grado')['Gramaje_pope'].mean().reset_index()


# In[ ]:


plt.figure(figsize=(10,6))
plt.bar(grado_gramaje_mean['Grado'], grado_gramaje_mean['Gramaje_pope'])
plt.grid(True, linewidth=0.2, color='gray')
plt.title('Gramaje por grado')
plt.xlabel('Grado')
plt.ylabel('gramaje g/m²')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




