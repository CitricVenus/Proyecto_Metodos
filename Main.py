from ast import If
from datetime import date
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as stat


prediction_G = 0
prediction_PG = 0
prediction_PG13 = 0
prediction_R = 0
prediction_TV14 = 0
prediction_TVG = 0
prediction_TVMA = 0
prediction_TVPG = 0
prediction_TVY = 0
prediction_TVY7= 0
prediction_NC17 = 0
suma_ninos = 0
suma_adolescentes = 0
suma_adultos = 0
suma_total = 0

anio = 2022
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
nc_17 = df.loc[df["rating"]=="NC-17"]

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
nc17_anio = nc_17.groupby(["date_added"],as_index=False).count().drop("show_id",axis=1)


def prediccionRating(df,title,anio):
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

    prediccion = regresion.predict(X=[[anio]])
    
    #se saca el error
    error = regresion.score(df["date_added"].values.reshape(-1,1),df["Total"])
    error = error*100
    #se saca los datos 
    #print(regresion.__dict__)
   
    print("----------------------------------------------"+title+"----------------------------------------------")
    print("Por cada año que aumente el estado, el número de raiting incrementará en: " + str(regresion.__dict__.get("coef_")[0].round(2)))
    
    print("Nuestro modelo explica un " + str(error.round(2)) + "% de la variabilidad original del total de rating ")
    #prediccion
    print("Prediccion en el " + str(anio) +" : " + str(prediccion[0].round(2)))
    #desviación estándar
    print("La desviación estándar de los datos es: " + str(round(stat.pstdev(df['Total']), 2)))
    #se grafica
    
    #tabla
    fig.patch.set_visible(False)
    axs[1].axis('off') 
    axs[1].axis('tight')
    
    table = axs[1].table(cellText=df.values.round(2),colLabels=df.columns,loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    plt.title(title + str(anio) + "=" + str(prediccion.round(2)))
    
    #grafica
    #fig.tight_layout()
    sns.regplot(x="date_added", y="Total", data=df,ax=axs[0])
    plt.title(title)
    
    plt.show()
    return prediccion.round(2)
 
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
    

prediction_G = prediccionRating(g_anio,"Rating G",anio)
prediction_PG = prediccionRating(pg_anio,"Rating PG",anio)
prediction_PG13 = prediccionRating(pg13_anio,"Rating PG-13",anio)
prediction_R = prediccionRating(r_anio,"Rating R",anio)
prediction_TV14 = prediccionRating(tv14_anio,"Rating TV-14",anio)
prediction_TVG = prediccionRating(tvg_anio,"Rating TV-G",anio)
prediction_TVMA = prediccionRating(tvma_anio,"Rating TV-MA",anio)
prediction_TVPG = prediccionRating(tvpg_anio,"Rating TV-PG",anio)
prediction_TVY = prediccionRating(tvy_anio,"Rating TV-Y",anio)
prediction_TVY7 = prediccionRating(tvy7_anio,"Rating TV-Y7",anio)
prediction_NC17 = prediccionRating(nc17_anio,"Rating NC-17",anio)

suma_ninos = prediction_TVY + prediction_TVY7 + prediction_G + prediction_TVG + prediction_PG + prediction_TVPG

suma_adolescentes = prediction_PG13 + prediction_TV14

suma_adultos = prediction_R + prediction_TVMA + prediction_NC17

suma_total = suma_ninos + suma_adolescentes + suma_adultos

print("-----------------------------Resultados finales------------------------------")
print("Niños = " + str(suma_ninos[0].round(2)))
print("Adolescentes = " + str(suma_adolescentes[0].round(2)))
print("Adultos = " + str(suma_adultos[0].round(2)))

def mayorContenido():
    if suma_ninos>suma_adolescentes and suma_ninos>suma_adultos:
        print("En el año " + str(anio) + " la audiencia con mayor contenido en Netflix es Niños" )
    if suma_adolescentes>suma_ninos and suma_adolescentes>suma_adultos:
        print("En el año " + str(anio) + " la audiencia con mayor contenido en Netflix es Adolescentes" )
    if suma_adultos>suma_ninos and suma_adultos>suma_adolescentes:
        print("En el año " + str(anio) + " la audiencia con mayor contenido en Netflix es Adultos" )

def menorContenido():
    if suma_ninos<suma_adolescentes and suma_ninos<suma_adultos:
        print("En el año " + str(anio) + " la audiencia con menor contenido en Netflix es Niños" )
    if suma_adolescentes<suma_ninos and suma_adolescentes<suma_adultos:
        print("En el año " + str(anio) + " la audiencia con menor contenido en Netflix es Adolescentes" )
    if suma_adultos<suma_ninos and suma_adultos<suma_adolescentes:
        print("En el año " + str(anio) + " la audiencia con menor contenido en Netflix es Adultos" )


mayorContenido()
menorContenido()
print("-------------------------------Total de contenido de Netflix en "+str(anio)+"---------------------------------------")
print(str(suma_total[0].round(2)))
