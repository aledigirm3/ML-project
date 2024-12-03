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


# Note
## NN
Best parameters using gris search with R2 score: {'activation': 'logistic', 'alpha': 0.1, 'hidden_layer_sizes': (50,), 'learning_rate': 'constant', 'solver': 'adam'}
