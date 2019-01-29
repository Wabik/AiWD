#1.Czy wzrost koreluje z rokiem rozpoczęcia kariery zawodowej?
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

dane=pd.read_csv(r"NBA.csv")

zmiennaWzrost=dane["Height"]
zmiennaZawodowa=dane["Draft Year"]

print(st.pearsonr(zmiennaWzrost,zmiennaZawodowa))

plt.plot([zmiennaWzrost], [zmiennaZawodowa], 'ro')
plt.legend()
plt.xlabel("Wzrost")
plt.ylabel("Poczatek kariery zawodowej")
plt.show()


#2.Czy wzrost koreluje z wagą graczy?
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

dane=pd.read_csv(r"NBA.csv")

zmiennaWzrost=dane["Weight"]
zmiennaWaga=dane["Height"]

zmiennaWaga=zmiennaWaga.fillna(0)
zmiennaWzrost=zmiennaWzrost.fillna(0)

korelacja=st.pearsonr(zmiennaWzrost,zmiennaWaga)
print(korelacja)

plt.plot([zmiennaWaga], [zmiennaWzrost], 'ro')
plt.xlabel("Wzrost [ft]")
plt.ylabel("Waga [lbs]")
plt.show()


#3.Czy wiek gracza koreluje z liczbą sezonów w lidze?
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

dane=pd.read_csv(r"NBA.csv")

zmiennaWiekGracza=dane["Age"]
zmiennaLiczbaSezonow=dane["Seasons in league"]

zmiennaWiekGracza=zmiennaWiekGracza.fillna(0)
zmiennaLiczbaSezonow=zmiennaLiczbaSezonow.fillna(0)

korelacja=st.pearsonr(zmiennaWiekGracza,zmiennaLiczbaSezonow)
print(korelacja)

plt.plot([zmiennaWiekGracza],[zmiennaLiczbaSezonow], 'ro' )

plt.xlabel("Wiek")
plt.ylabel("Liczba sezonow")
plt.show()


#4.Który z graczy grał przez największą liczbę sezonów?
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

dane=pd.read_csv(r"NBA.csv")

gracze=dane["Player"].value_counts()[0:10]
sezony=dane["Seasons in league"].value_counts()[0:10]

print("Gracze:")
print(gracze)

os=range(len(sezony))

plt.rcParams.update({'font.size': 13})
plt.bar(os, gracze)

podpisy=['LeBron James', 'Kobe Bryant', 'Michael Jordan','Kevin Durant',
 'Allen Iverson','Karl Malone', 'Tim Duncan','Shaquille O’Neal',
 'Kevin Garnett','Dwyane Wade']

plt.xticks(os,podpisy, rotation=20)
plt.xlabel("Zawodnicy")
plt.ylabel("Liczba sezonow")

plt.show()


#5.Które zespoły najczęściej pojawiają się w bazie
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

dane=pd.read_csv(r"NBA.csv")

print(dane["Team"].describe())
print(dane["Team"].value_counts()[0:10])

druzyny=dane["Team"].value_counts()[0:10]
os=range(len(druzyny))

plt.bar(os, druzyny)
plt.xticks(os,dane["Team"].value_counts()[0:10].index, rotation=20)
plt.xlabel("Drużyny")
plt.ylabel("Występowanie w bazie")
plt.show()


# 6.1 Zawodnicy z konferencji wschodniej[5]
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

dane=pd.read_csv(r"NBA.csv")

zmiennaZawodnik=dane["Player"]
zmiennaKonferencja=dane["Conference"]
warunek=(zmiennaKonferencja=='East')
zawodnicy=zmiennaZawodnik[warunek][0:5]

print(zawodnicy)

#6.2 Zawodnicy z konferencji zachodniej[5]
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

dane=pd.read_csv(r"NBA.csv")

zmiennaZawodnik=dane["Player"]
zmiennaKonferencja=dane["Conference"]
warunek=(zmiennaKonferencja=='West')
zawodnicy=zmiennaZawodnik[warunek][0:5]

print(zawodnicy)


#7.Ile sezonów w lidze grają zawodnicy?
import matplotlib.pyplot as plt
import numpy as np

dane=pd.read_csv(r"NBA.csv")

zmiennaLiczbaSezonow=dane["Seasons in league"]

plt.hist(zmiennaLiczbaSezonow)
plt.xlabel("Liczba sezonow [-]")
plt.ylabel("Czestosc [-]")
plt.savefig("111.png")
plt.title("Histogram ukazujący liczbe sezonow wraz z czestotliwoscia wystepowania")
plt.show()
