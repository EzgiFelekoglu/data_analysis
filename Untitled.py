#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df=pd.read_csv(r'googleplaystore.csv')


# In[5]:


df.head()


# In[6]:


df.tail()


# In[8]:


df.columns


# In[13]:


### replacing gaps with '_'
df.columns=df.columns.str.replace(" ","_")


# In[14]:


df.columns


# In[15]:


df.shape


# In[16]:


df.dtypes


# In[17]:


### Null Values


# In[18]:


df.isnull().sum()


# In[20]:


### using seaborn


# In[22]:


sns.set_theme()
sns.set(rc={'figure.dpi':300,'figure.figsize':(12,9)})


# In[23]:


sns.heatmap(df.isnull(),cbar=False)


# In[24]:


### Finding median for 'Rating' column


# In[26]:


rating_median=df["Rating"].median()
rating_median


# In[28]:


df["Rating"].fillna(rating_median,inplace=True)


# In[29]:


## for the other columns 
df.dropna(inplace=True)


# In[31]:


df.isnull().sum()


# In[32]:


### changing data types


# In[33]:


df['Reviews'].describe()


# In[34]:


df['Reviews']=df['Reviews'].astype('int64')


# In[35]:


df['Reviews'].describe()


# In[36]:


df['Reviews'].describe().round()


# In[38]:


print(len(df["Size"].unique()))
df["Size"].unique()


# In[40]:


df["Size"].replace("M","",regex=True,inplace=True)
df["Size"].replace("k","",regex=True,inplace=True)


# In[42]:


df["Size"].unique()


# In[43]:


### finding median value and removing 'Varies with device' value from the column


# In[46]:


size_median=df[df["Size"]!="Varies with device"]["Size"].astype(float).median()
size_median


# In[47]:


df["Size"].replace("Varies with device",size_median,inplace=True)


# In[52]:


### changing Size column's data type to numeric type 
df.Size=pd.to_numeric(df.Size)


# In[53]:


df.Size.head()


# In[55]:


df.Size.describe().round()


# In[56]:


### 'Install' column


# In[57]:


df["Installs"].unique()


# In[58]:


### removing '+',','


# In[59]:


df.Installs=df.Installs.apply(lambda x:x.replace("+",""))
df.Installs=df.Installs.apply(lambda x:x.replace(",",""))
df.Installs=df.Installs.apply(lambda x:int(x))


# In[60]:


df["Installs"].unique()


# In[61]:


df.Price.unique()


# In[62]:


df.Price=df.Price.apply(lambda x:x.replace("$",""))
df.Price=df.Price.apply(lambda x:float(x))


# In[63]:


df.Price.unique()


# In[65]:


len(df.Genres.unique())


# In[66]:


df.Genres.head(10)


# In[67]:


df.Genres=df.Genres.str.split(";").str[0]


# In[68]:


len(df.Genres.unique())


# In[69]:


df.Genres.unique()


# In[71]:


df.Genres.value_counts()


# In[72]:


df.Genres.replace('Music & Audio','Music',inplace=True)


# In[75]:


df["Last_Updated"].head()


# In[76]:


## changing data type do datetime


# In[77]:


df.Last_Updated=pd.to_datetime(df.Last_Updated)


# In[84]:


print(df.Last_Updated.dtype)


# In[85]:


## checking updated data types
df.dtypes


# In[86]:


####### visulation ####


# In[87]:


df.Type.value_counts().plot(kind='bar',color='red')


# In[89]:


sns.boxplot(x='Type',y='Rating',data=df)


# In[97]:


sns.countplot(x='Content_Rating',data=df)
plt.title("Content rating with their counts")


# In[96]:


sns.boxplot(x='Content_Rating',y='Rating',data=df)


# In[99]:


cat_num=df.Category.value_counts()
sns.barplot(x=cat_num,y=cat_num.index,data=df)
plt.title("Number of Categories",size=25)


# In[100]:


sns.histplot(df.Rating,kde=True)


# In[ ]:




