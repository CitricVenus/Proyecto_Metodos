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




def prediccionRating(df,title):
    fig, axs = plt.subplots(1, 2)
    ##Se hace la regresion lineal para g
    df.rename(columns={"rating":"Total"},inplace=True)
    #print(df)

    regresion = linear_model.LinearRegression()
    #se hace implementa la regresion
    regresion.fit(df["date_added"].values.reshape(-1,1),df["Total"]) 
    #se ahce la prediccion
    prediccion_df = regresion.predict(df["date_added"].values.reshape(-1,1))

    #df.insert(0,"pred",prediccion_df)
    df["prediction"] = prediccion_df
    #print(df)

    prediccion = regresion.predict(X=[[2022]])
    #se saca el error
    error = regresion.score(df["date_added"].values.reshape(-1,1),df["Total"])
    error = error*100
    #se saca los datos 
    #print(regresion.__dict__)
   
    print("----------------------------------------------"+title+"----------------------------------------------")
    print("Por cada año que aumente el estado, el número de raiting incrementará en: " + str(regresion.__dict__.get("coef_")))
    
    print("Nuestro modelo explica un " + str(error) + "% de la variabilidad original del total de rating ")
    #prediccion
    print("Prediccion en el 2022: " + str(prediccion))
    #se grafica
    
    #tabla
    fig.patch.set_visible(False)
    axs[1].axis('off') 
    axs[1].axis('tight')
    
    table = axs[1].table(cellText=df.values,colLabels=df.columns,loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    plt.title(title)
    
    
    #grafica
    #fig.tight_layout()
    sns.regplot(x="date_added", y="Total", data=df,ax=axs[0])
    plt.title(title)
    
    plt.show()

 





    #sacar regresion lineal para cada categoria


    #print(g)
    #agrupacion por año

    #dates = df.date_added.unique()
    #print(dates)


    #group_date = df.groupby(["date_added","rating"]).count()

    #print(group_date.loc[2019.0])
    #print(pg13)

    #sacar por año la cantidad de peliculas o series cada rating

    #2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021


    #crear dataframe con dos columnas para cada rating con año y cantidad de peliculas.
    

prediccionRating(g_anio,"Rating G")
prediccionRating(pg_anio,"Rating PG")
prediccionRating(pg13_anio,"Rating PG-13")
prediccionRating(r_anio,"Rating R")
prediccionRating(tv14_anio,"Rating TV-14")
prediccionRating(tvg_anio,"Rating TV-G")
prediccionRating(tvma_anio,"Rating TV-MA")
prediccionRating(tvpg_anio,"Rating TV-PG")
prediccionRating(tvy_anio,"Rating TV-Y")
prediccionRating(tvy7_anio,"Rating TV-Y7")