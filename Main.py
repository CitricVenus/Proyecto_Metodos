from datetime import date
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv', usecols=('show_id', 'date_added', 'rating'))
df['date_added'] = pd.DatetimeIndex(pd.to_datetime(df['date_added'])).year
#year = pd.DatetimeIndex(pd.to_datetime(df['date_added'])).year
#print(df)
#print(df.loc[:,['show_id', 'year_added', 'rating']])


#agrupaciones por rating
g = df.loc[df["rating"]=="G"]
pg = df.loc[df["rating"]=="PG"]
pg_13 = df.loc[df["rating"]=="PG-13"]
r = df.loc[df["rating"]=="R"]
tv_14 = df.loc[df["rating"]=="TV-14"]
tv_g = df.loc[df["rating"]=="TV-G"]
tv_ma = df.loc[df["rating"]=="TV-MA"]
tv_pg = df.loc[df["rating"]=="TV-PG"]
tv_y = df.loc[df["rating"]=="TV-Y"]
tv_y7 = df.loc[df["rating"]=="TV-Y7"]


g_anio = g.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
pg_anio = pg.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
pg13_anio = pg_13.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
r_anio = r.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
tv14_anio = tv_14.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
tvg_anio = tv_g.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
tvma_anio = tv_ma.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
tvpg_anio = tv_pg.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
tvy_anio = tv_y.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)
tvy7_anio = tv_y7.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)


##Se hace la regresion lineal para g
print(g_anio)

regresion = linear_model.LinearRegression()
#se hace implementa la regresion
regresion.fit(g_anio["date_added"].values.reshape(-1,1),g_anio["rating"]) 
#se ahce la prediccion
prediccion = regresion.predict(X=[[2022]])
#se saca el error
error = regresion.score(g_anio["date_added"].values.reshape(-1,1),g_anio["rating"])
#se saca los datos 
print(regresion.__dict__)
print(error)
print(prediccion)
#se grafica
sns.regplot(x="date_added", y="rating", data=g_anio)
plt.show()

  
"""
Nuestro modelo explica un 38% de la variabilidad original del total de accidentes...

Por cada año que aumente el estado, el número de raiting incrementará en 1.03
"""





#sacar regresion lineal para cada categoria


#print(g)
#agrupacion por año

dates = df.date_added.unique()
#print(dates)


group_date = df.groupby(["date_added","rating"]).count()

#print(group_date.loc[2019.0])
#print(pg13)

#sacar por año la cantidad de peliculas o series cada rating

#2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021


#crear dataframe con dos columnas para cada rating con año y cantidad de peliculas.