from datetime import date
import pandas as pd
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

#agrupacion por año

dates = df.date_added.unique()
print(dates)


group_date = df.groupby(["date_added","rating"]).count()
print(group_date.loc[2021.0])
#print(pg13)