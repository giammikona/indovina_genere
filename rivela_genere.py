#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import gender_guesser.detector as gender #https://pypi.org/project/gender-guesser/ c'è il comando per installarlo direttamente
print('ok') #per verificare

#set-up dello script
file_path = "..." #scrivere qui il file path del dataframe da analizzare
ds = pd.read_csv(file_path, sep= ';')
gen = gender.Detector() 

#VERIFICA DATI
#display(ds)

#l'algoritmo accetta solo nomi con la prima lettera maiuscola e il resto in minuscolo, UNICODE.
#test
#nome = ds.iloc[287,1].title()
#print(nome)
#print(gen.get_gender(nome, 'italy'))


#l'algoritmo cicla il DF e determina il genere del nome. Una volta determinato il genere scrive il risultato nella colonna
#genere. Tendenzialmente specificherei il Paese su cui basare l'analisi -> gen.get_gender(u"Nome", u'Italy')
index= 0
generi = []
for nome in ds.nome:					
    point = ds.iloc[index,1].title()  #ATTENZIONE: point = ds.iloc[index,1] il secondo elemento rappresenta l'indice della colonna
    generi.append(gen.get_gender(point,'italy'))
    index = index+1
      
ds['generi']=generi
#ds  #TEST
ds.to_csv(r'datapath\...\.csv') #SCRIVERE QUI DOVE SI VUOLE SALVARE IL NUOVO FILE

