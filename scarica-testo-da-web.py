import requests
from bs4 import BeautifulSoup
from datetime import datetime

def estrai_testo_da_url(url):
    try:
        # Effettua la richiesta GET all'URL specificato
        response = requests.get(url)
        response.raise_for_status()  # Genera un'eccezione se lo stato della richiesta non è 200 (OK)
        
        # Esegui il parsing del sorgente HTML utilizzando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Estrai il testo dalla pagina HTML
        testo = soup.get_text()
        
        return testo
    except requests.exceptions.RequestException as e:
        print("Si è verificato un errore durante la richiesta:", e)
        return None
    except Exception as e:
        print("Si è verificato un errore durante l'elaborazione dell'HTML:", e)
        return None

if __name__ == "__main__":
    url = input("Inserisci l'URL pubblico: ")
    
    testo_pagina = estrai_testo_da_url(url)
    
    if testo_pagina:
        # Ottieni la data corrente nel formato specificato
        data_corrente = datetime.now().strftime('%Y%m%d%H%M')
        
        # Costruisci il nome del file di output
        nome_file_output = f"html-output-{data_corrente}.txt"
        
        # Scrivi il testo estratto nel file di output
        with open(nome_file_output, 'w') as file_output:
            file_output.write(testo_pagina)
        
        print(f"Il testo è stato estratto correttamente e salvato nel file {nome_file_output}")
