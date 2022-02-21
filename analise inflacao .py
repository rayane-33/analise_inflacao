Analise da evoluçao da inflação


#importando os dados disponibilizados no dalake 

import pandas as pd
import basedosdados as bd
import seaborn as sns
import matplotlib.pyplot as plt
# Para carregar o dado direto no pandas
df = bd.read_table(dataset_id='br_ibge_ipca', 
table_id='mes_brasil',
billing_project_id="inflacao-bd-341821")


# In[25]:


#exibição da tabela de dados

evolucao_inflacao= pd.read_csv('mes_brasil.csv')
display(evolucao_inflacao)


# In[92]:


#analise grafica da evolução da inflação trimestral de 1979 à 2021

graf_linha= sns.lineplot(data=evolucao_inflacao, x="ano", y="variacao_trimestral", color='red')
plt.show(graf_linha)


# In[88]:


#variaçao anual da inflação 1979 à 2021

graf_linha=sns.lineplot(data=evolucao_inflacao, x="ano", y="variacao_anual")
plt.show(graf_linha)


# In[91]:


#variação da inflação doze meses

graf_linha=sns.lineplot(data=evolucao_inflacao, x="ano", y="variacao_doze_meses")
plt.show(graf_linha)


# In[93]:


#variação da inflação mensal
graf_linha=sns.lineplot(data=evolucao_inflacao, x="ano", y="variacao_mensal")
plt.show(graf_linha)


# In[97]:


graf_linha=sns.lineplot(data=evolucao_inflacao, x="ano", y="variacao_mensal")
plt.show(graf_linha)


# In[ ]:





# In[ ]:




