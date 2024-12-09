# ML-project

Machine learning project about fores firest using a dataset taken from UC Irvine.

# Descrizione Problema (ita)

Si tratta di un compito regressione, in cui l'obiettivo è prevedere l'area bruciata dagli incendi boschivi, nella regione nordorientale del Portogallo, utilizzando dati meteorologici e di altro tipo.
DATASET: Multivariato
AREA TEMATICA: Clima e Ambiente
(Basato su campionu reali)

Descrizione delle variabili di input
Le variabili di input possono essere suddivise in categorie principali:

## 1. Coordinate spaziali

- X: Coordinata sulla mappa del parco lungo l'asse x (da 1 a 9).

- Y: Coordinata sulla mappa del parco lungo l'asse y (da 2 a 9).
  Queste indicano la posizione geografica all'interno del parco Montesinho.

## 2. Informazioni temporali

- **month**: Mese dell'anno (da gennaio a dicembre).

- **day**: Giorno della settimana (da lunedì a domenica).

Queste variabili forniscono contesto temporale agli incendi, poiché la stagionalità e il giorno della settimana possono influenzare il rischio di incendio.

## 3. Indici del sistema di pericolo d'incendio (FWI)

Questi indici, derivati dal sistema FWI, rappresentano condizioni ambientali che influiscono sul comportamento degli incendi:

- **FFMC** (Fine Fuel Moisture Code): Indica l'umidità dei combustibili sottili sulla superficie; valori più alti indicano un maggiore rischio di incendio.

- **DMC** (Duff Moisture Code): Misura l'umidità dei combustibili di profondità media.

- **DC** (Drought Code): Riflette la secchezza dei combustibili profondi; valori più alti suggeriscono condizioni di lunga siccità.

- **ISI** (Initial Spread Index): Stima la velocità di propagazione iniziale di un incendio, influenzata dal vento e dalla secchezza.

## 4. Condizioni meteorologiche

- **temp**: Temperatura dell'aria in gradi Celsius (da 2.2 a 33.3). Temperature più alte possono favorire incendi.

- **RH**: Umidità relativa in percentuale (da 15% a 100%). Valori più bassi indicano un rischio maggiore.

- **wind**: Velocità del vento in km/h (da 0.4 a 9.4). Il vento può accelerare la propagazione di un incendio.

- **rain**: Pioggia esterna in mm/m² (da 0.0 a 6.4). La pioggia riduce il rischio di incendio.

5. Output

- **area**: Superficie bruciata in ettari (da 0.0 a 1090.84).

## Obiettivo del modello:

L'obiettivo del modello è prevedere l'area bruciata (**area**) in base alle variabili di input. Il modello tenta di identificare relazioni complesse tra fattori ambientali, indici di rischio, e caratteristiche temporali e spaziali, per stimare in modo accurato l'impatto di un incendio.

# Migliori modelli

Stima dei migliori modelli, nei vari approcci, sulla base di tutte le statistiche (principalmente la tolleranza del 5% e 10% dell'accuratezza).

## v.0

### SVM:

Best parameters: {'C': 10, 'gamma': 0.01}

Mean Absolute Error: 1.0947580331649245 -> km^2 = 0.019884594878182008
Train error (MAE): 0.9619051663230452

---

Mean Squared Error: 2.541493792715267
Root Mean Squared Error: 1.594206320623296 -> km^2 = 0.03924419110806051
51 / 104 of y_test is 0

---

Precisione del modello rispetto all'area massima: 77.21%

---

Accuracy in percentage (with a tolerance of 5.0%): 23.08%
Accuracy in percentage (with a tolerance of 10.0%): 44.23%
Accuracy in percentage (with a tolerance of 25.0%): 77.88%
Accuracy in percentage (with a tolerance of 50.0%): 92.31%

## v.1

### SVM:

Best parameters: {'C': 1, 'gamma': 0.1}

Mean Absolute Error: 1.0863498908523048 -> km^2 = 0.01963437437045906
Train error (MAE): 0.878988975927549

---

Mean Squared Error: 2.485849786629047
Root Mean Squared Error: 1.5766577899560346 -> km^2 = 0.03838756614799872
51 / 104 of y_test is 0

---

Precisione del modello rispetto all'area massima: 77.46%

---

Accuracy in percentage (with a tolerance of 5.0%): 26.92%
Accuracy in percentage (with a tolerance of 10.0%): 49.04%
Accuracy in percentage (with a tolerance of 25.0%): 76.92%
Accuracy in percentage (with a tolerance of 50.0%): 92.31%

## v.2

### SVM:

Best parameters: {'C': 1, 'gamma': 0.1}

Mean Absolute Error: 1.0463738850255944 -> km^2 = 0.018473077110773423
Train error (MAE): 0.8885643944721647

---

Mean Squared Error: 2.0550198568475304
Root Mean Squared Error: 1.4335340445373213 -> km^2 = 0.031934930266136474
56 / 103 of y_test is 0

---

Precisione del modello rispetto all'area massima: 79.51%

---

Accuracy in percentage (with a tolerance of 5.0%): 22.33%
Accuracy in percentage (with a tolerance of 10.0%): 43.69%
Accuracy in percentage (with a tolerance of 25.0%): 79.61%
Accuracy in percentage (with a tolerance of 50.0%): 95.15%

## v.3

### SVM:

Best parameters: {'C': 1, 'gamma': 0.1}

Mean Absolute Error: 1.133739043527318 -> km^2 = 0.021072529608497047
Train error (MAE): 0.9556174749036942

---

Mean Squared Error: 2.505638427122861
Root Mean Squared Error: 1.5829208530823204 -> km^2 = 0.03869157153804398
51 / 104 of y_test is 0

---

Precisione del modello rispetto all'area massima: 77.37%

---

Accuracy in percentage (with a tolerance of 5.0%): 23.08%
Accuracy in percentage (with a tolerance of 10.0%): 40.38%
Accuracy in percentage (with a tolerance of 25.0%): 78.85%
Accuracy in percentage (with a tolerance of 50.0%): 94.23%

## Considerazioni sui risultati

Come è stato gia detto questi sono i risultati migliori per quanto riguarda l'accuratezza con una bassa tolleranza.
Si può notare come il modello migliore sia SVM. C'è però inoltre da dire che la stessa cosa non vale se vogliamo considerare la precisione rispetto
l'area massima degli incendi e per quanto riguarda l'accuratezza con una tolleranza piu alta (es.: 25%); in tal caso risultano migliori i modelli Gradient Boost
di regressione per quanto riguarda la versione 0, la versione 1 e la versione 3, mentre per la versione 2 risulta migliore il Regressore Lineare.
Si può concludere dicendo che il modello migliore dipende da cosa è di interesse per le previsioni e quanta tolleranza (a livello di area) siamo disposti ad accettare.
