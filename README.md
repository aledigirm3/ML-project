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

## df:
- LINEAR REGRESSOR:

Mean Absolute Error: 1.1865045061594848 -> km^2 = 0.022756112934549187
Train error (MAE): 1.1240844078310506
------------
Mean Squared Error: 2.1844052584845253
Root Mean Squared Error: 1.477973361899505 -> km^2 = 0.033840517852264676
51 / 104 of y_test is 0
------------
Accuracy in percentage (with a tolerance of 5.0%): 8.65%
Accuracy in percentage (with a tolerance of 10.0%): 17.31%
Accuracy in percentage (with a tolerance of 30.0%): 85.58%
Accuracy in percentage (with a tolerance of 100%): 100.00%
=====================================
Best parameters: {'C': 10, 'gamma': 0.01}
- SVM:

Mean Absolute Error: 1.093445581881819 -> km^2 = 0.019845398530563815
Train error (MAE): 0.9814298262198534
------------
Mean Squared Error: 2.428889246437062
Root Mean Squared Error: 1.5584894117179822 -> km^2 = 0.037516380523181125
51 / 104 of y_test is 0
------------
Accuracy in percentage (with a tolerance of 5.0%): 20.19%
Accuracy in percentage (with a tolerance of 10.0%): 47.12%
Accuracy in percentage (with a tolerance of 30.0%): 81.73%
Accuracy in percentage (with a tolerance of 100%): 100.00%
=====================================


## df_clean:
- LINEAR REGRESSOR:

Mean Absolute Error: 1.0476254112443875 -> km^2 = 0.01850873422155759
Train error (MAE): 1.0892344598708417
------------
Mean Squared Error: 1.3903823061233724
Root Mean Squared Error: 1.1791447350191462 -> km^2 = 0.022515920405119627
57 / 102 of y_test is 0
------------
Accuracy in percentage (with a tolerance of 5.0%): 6.86%
Accuracy in percentage (with a tolerance of 10.0%): 15.69%
Accuracy in percentage (with a tolerance of 30.0%): 48.04%
Accuracy in percentage (with a tolerance of 100%): 100.00%
=====================================
Best parameters: {'C': 1, 'gamma': 0.1}
- SVM:

Mean Absolute Error: 0.891557982223772 -> km^2 = 0.014389264969401693
Train error (MAE): 0.8424871101316078
------------
Mean Squared Error: 1.3916464553580963
Root Mean Squared Error: 1.179680658211406 -> km^2 = 0.022533351111325067
57 / 102 of y_test is 0
------------
Accuracy in percentage (with a tolerance of 5.0%): 18.63%
Accuracy in percentage (with a tolerance of 10.0%): 32.35%
Accuracy in percentage (with a tolerance of 30.0%): 69.61%
Accuracy in percentage (with a tolerance of 100%): 100.00%
=====================================
Best parameters: {'learning_rate': 0.01, 'max_depth': 7, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
- GRADIENT BOOST REGRESSION:

Mean Absolute Error: 1.0473354705176057 -> km^2 = 0.018500469576624243
Train error (MAE): 0.8287923209243019
------------
Mean Squared Error: 1.4149150429021415
Root Mean Squared Error: 1.1895020146692235 -> km^2 = 0.022854446966737534
57 / 102 of y_test is 0
------------
Accuracy in percentage (with a tolerance of 5.0%): 2.94%
Accuracy in percentage (with a tolerance of 10.0%): 8.82%
Accuracy in percentage (with a tolerance of 30.0%): 67.65%
Accuracy in percentage (with a tolerance of 100%): 100.00%
