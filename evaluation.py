import numpy as np

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score

# Valutazione performace
def evaluate(y_test, y_pred, y_train, y_train_pred):

    # R2 score
    print(f"R²: {r2_score(y_test, y_pred)}")
    print(f"Train R²: {r2_score(y_train, y_train_pred)}")
    print('------------')

    # MAE.
    print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred), '-> km^2 =', (np.exp(mean_absolute_error(y_test, y_pred)) - 1) / 100)
    print(f"Train error (MAE): {mean_absolute_error(y_train, y_train_pred)}")
    print('------------')

    # MSE
    print('Mean Squared Error:', (root_mean_squared_error(y_test,y_pred))**2)
    # RMSE = SQRT di MSE
    print('Root Mean Squared Error:', root_mean_squared_error(y_test,y_pred), '-> km^2 =', (np.exp(root_mean_squared_error(y_test, y_pred)) - 1) / 100)

    # Attenzione ai valori nulli per la normalizzazione
    print((y_test == 0).sum(), '/', len(y_test), 'of y_test is 0')

    print('------------')

    # Intervalli per la tolleranza dell'errore (in %)
    tolerances = [5,10,30,100] 

    # Calcolare l'errore relativo (errore assoluto / valore reale)
    percent_err = (np.abs(y_test - y_pred) / 5) * 100

    for tolerance in tolerances:

        # Verifica quante previsioni sono accettabili (errore relativo <= tolleranza)
        result = percent_err <= tolerance

        # Calcolare la percentuale di previsioni accettabili
        accuracy_percentage = (np.sum(result) / len(result)) * 100

        # Stampa l'accuratezza in percentuale
        print(f'Accuracy in percentage (with a tolerance of {tolerance}%): {accuracy_percentage:.2f}%')