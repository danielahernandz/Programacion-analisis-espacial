#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Programación python
#Analisis espacial 


# In[2]:


get_ipython().system('pip3 install matplotlib')


# In[3]:


import pandas as pd #Paquete para manejo de bases de datos (dataframe) 
import geopandas as gpd #Paquete para manejo de bases de datos espaciales
#Geopandas version de pandas para trabajar con datos geograficos. 
#Contiene funciones que nos permite manipular las geometrias de las observaciones ademas almacena atributos estructurados


import matplotlib.pyplot as plt #Libreria para graficos y figuras de impacto
import numpy as np #Paquete para trabajar con operaciones numericas y vectores
from shapely.geometry import Point #Paquete para la manipulacion de objetos geograficos


# In[4]:


#Geopandas tiene precargadas algunas bases de datos (entre ellas, los paises del mundo)
paises=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


# In[5]:


paises


# In[6]:


type(paises)


# In[7]:


get_ipython().system('pip3 install descartes')


# In[8]:


paises.plot()


# In[9]:


paises.columns 


# In[10]:


paises.plot(column='pop_est')


# In[11]:


fig, ax = plt.subplots(figsize=(18,8))
paises.plot(column='pop_est', ax=ax, legend=True) 
plt.suptitle('Mapa Poblacion', fontsize=22) 
ax.axis('off') 


# In[12]:


fig, ax = plt.subplots(figsize=(18,8))
paises.plot(column='pop_est', ax=ax,legend=True,cmap='OrRd') #Recordar que es importante decir donde queremos que se pinte el grafico para ellos se utilza la funcion de los ejes (ax)
plt.suptitle('Mapa de población', fontsize=22)
ax.axis('off')


# In[13]:


paises.plot(column='pop_est', cmap='OrRd',figsize=(12,8))


# In[14]:


fig, ax=plt.subplots(1,2, figsize=(18,8))
paises.plot(column='pop_est',ax=ax[0], legend=True, cmap='OrRd') 
ax[0].set_title('Mapa población') 
ax[0].axis('off')
#subgrafico2
paises.plot(column='gdp_md_est', ax=ax[1], legend=True, cmap='plasma')
ax[1].set_title('Mapa_PIB') 
plt.suptitle('Ejemplo')


# In[ ]:




