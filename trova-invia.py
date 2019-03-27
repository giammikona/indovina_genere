#!/usr/bin/env python
# coding: utf-8

#importo le dipendenze e set-up dello script
import pandas as pd
import nexmo
client = nexmo.Client(key='xxx', secret='xxx') ##scrivere qui le chiavi di nexmo 
msg_m_open = open("...", "r") #scrivere qui il file path del messaggio per i MASCHI, SOLO .txt 
msg_f_open = open("...", "r") #scrivere qui il file path del messaggio per le FEMMINE, SOLO .txt 
msg_g_open = open("...", "r") #scrivere qui il file path del messaggio GENERICO, SOLO .txt 
print("ok")

file_path = "..." #scrivere qui il file path del dataframe da analizzare
ds = pd.read_csv(file_path, sep= ';')
msg_m= msg_m_open.read()
msg_m_open.close()
msg_f= msg_f_open.read()
msg_f_open.close()
msg_u= msg_u_open.read()
msg_u_open.close()
#ds
#msg_m
#msg_f



index= 0
for gen in ds.generi:
    if gen == 'male':
        point = ds.iloc[index,2] #il secondo attributo deve puntare sul numero di telefono (n colonna)   
        responseData = client.send_message(
        {
            "from": "Acme Inc",
            "to": point,
            "text": msg_m,
        }
        )

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        index = index+1
        print('ok' + msg_m)
    
    if gen == 'female':
        point = ds.iloc[index,2] #il secondo attributo deve puntare sul numero di telefono (n colonna)   
        responseData = client.send_message(
        {
            "from": "Acme Inc",
            "to": point,
            "text": msg_f,
        }
        )

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        index = index+1
        print('ok' + msg_f)
    
    if gen == 'unknown':
        point = ds.iloc[index,2] #il secondo attributo deve puntare sul numero di telefono (n colonna)   
        responseData = client.send_message(
        {
            "from": "Acme Inc",
            "to": point,
            "text": msg_u,
        }
        )

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
        index = index+1
        print('ok' + msg_u)
        
                

