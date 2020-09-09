#!/usr/bin/env python
# coding: utf-8

# We all have some expectation of our lives. Most of our desires comes in various forms of achievements. Life can be very unpredictable. How do people achieve what they want? It luck more important, or our talent and hardworking? We will use an interesting simulation to discover the formula for success. 
# 
# The formula we want to explore is: 
# #### Success = Hardworking + Talent + Luck + Start up.
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# ### Experiment 1: Luck is unform distribution, same start point

# In[2]:


N = 50
P = 2000
r1, r2 = 1, 0.5

mu_IQ, sigma_IQ = 100, 15
IQ = np.random.normal(mu_IQ, sigma_IQ, P) / mu_IQ
luck_unif = 2 * np.random.random_sample((N,P)) - 0.5


# In[3]:


Achieve_v1 = np.ones(P)

for i in range(0, P):
    for j in range(0, N):
        Achieve_v1[i] = r1 * Achieve_v1[i] + r2 * Achieve_v1[i] * IQ[i] * luck_unif[j,i]


# In[4]:


IQ_vs_Luck_Norm = plt.plot(IQ * mu_IQ, Achieve_v1, 'bo')
plt.xlabel('IQ (Talent)')
plt.ylabel('Achievement')
plt.title('IQ: Normal(100, 15). Luck: Uniform(-0.5, 1.5).')
plt.yscale('log')


# ### Experiment 2: Luck is lognormal distribution, same start point

# In[5]:


luck_log = np.random.lognormal(1,1,(N,P))
Achieve_v2 = np.ones(P)

for i in range (0, P):
    for j in range(0, N):
        Achieve_v2[i] = r1 * Achieve_v2[i] + r2 * Achieve_v2[i] * IQ[i] * luck_log[j,i]


# In[17]:


IQ_vs_Luck_logN = plt.plot(IQ * mu_IQ, Achieve_v2, 'bo') 
plt.yscale('log')
plt.xlabel('IQ (Talent)')
plt.ylabel('Achievement')
plt.title('IQ: Normal(100, 15). Luck: Lognormal(1,1)')


# In[7]:


# luck_log_Graph = np.random.lognormal(1,1,N)
# count, bins, ignored = plt.hist(luck_log_Graph, N, align='mid') ***Plot Histogram of Lognormal distribution


# ### Experiment 3: Luck is lognormal distribution, Inherit money to start with

# In[22]:


Inherit_Money = np.random.lognormal(10,4,P)
Achieve_v3 = Inherit_Money  ##Start with inherent money at random level

for i in range (0, P):
    for j in range(0, N):
        Achieve_v3[i] = r1 * Achieve_v3[i] + r2 * Achieve_v3[i] * IQ[i] * luck_log[j,i]


# In[24]:


IQ_vs_Luck_logN_inh = plt.plot(IQ * mu_IQ, Achieve_v3, 'bo') 
plt.yscale('log')
plt.xlabel('IQ (Talent)')
plt.ylabel('Achievement')
plt.title('IQ: Normal(100, 15). Luck: Lognormal(1,1). Start Fortune: Lognormal(10,4)')


# In[10]:


# Inh_vs_IQ = plt.plot(Inherit_Money, Achieve_v3, 'bo') 
# plt.yscale('log')
# plt.xscale('log')


# ### Experiment 4: Luck is lognormal distribution, Lognormal start point, Continuous Effort

# In[11]:


WorkHard = 2 * np.random.random(P) - 0.5
WorkHard_IQ = WorkHard + IQ

Achieve_v4 = np.ones(P)
for i in range (0, P):
    for j in range(0, N):
        Achieve_v4[i] = r1 * Achieve_v4[i] + r2 * Achieve_v4[i] * WorkHard_IQ[i] * luck_log[j,i]


# In[12]:


IQWorkHard_vs_Luck = plt.plot(WorkHard, Achieve_v4, 'bo') 
plt.yscale('log')
plt.xlabel('WorkHard')
plt.ylabel('Achievement')
plt.title('IQ: Normal(100,15). Luck: Lognormal(1,1). Start Fortune: 1. WorkHard: Uniform(-0.5,1.5)')


# In[13]:


IQWorkHardIQ_vs_Luck = plt.plot(IQ * mu_IQ, Achieve_v4, 'bo') 
plt.yscale('log')
plt.xlabel('IQ (Talent)')
plt.ylabel('Achievement')
plt.title('IQ: Normal(100, 15). Luck: Lognormal(1,1). Start Fortune: 1. WorkHard: Uniform(-0.5,1.5)')


# ### Experiment 5: Luck is lognormal distribution, Lognormal start point, Continuous Effort, Inherit Money

# In[25]:


Achieve_v5 = Inherit_Money

for i in range (0, P):
    for j in range(0, N):
        Achieve_v5[i] = r1 * Achieve_v5[i] + r2 * Achieve_v5[i] * WorkHard_IQ[i] * luck_log[j,i]


# In[26]:


IQWorkHard_vs_Luck_Inh = plt.plot(WorkHard, Achieve_v5, 'bo')
plt.yscale('log')
plt.xlabel('Workhard')
plt.ylabel('Achievement')
plt.title('IQ: Normal(100,15). Luck: Lognormal(1,1). Start Fortune: Lognormal(10,1). WorkHard: Uniform(-0.5,1.5)')


# In[27]:


IQWorkHardIQ_vs_Luck_Inh = plt.plot(IQ * mu_IQ, Achieve_v5, 'bo') 
plt.yscale('log')
plt.yscale('log')
plt.xlabel('IQ (Talent)')
plt.ylabel('Achievement')
plt.title('IQ: Normal(100, 15). Luck: Lognormal(1,1). Start Fortune: Lognormal(10,1). WorkHard: Uniform(-0.5,1.5)')


# In[ ]:




