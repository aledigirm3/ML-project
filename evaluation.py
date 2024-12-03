import numpy as np

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score

# Valutazione performace
def evaluate(y_test, y_pred, train_error):

    # R2 score
    print(f"R²: {r2_score(y_test, y_pred)}")
    print('------------')

    # MAE.
    print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred), '-> km^2 =', (np.exp(mean_absolute_error(y_test, y_pred)) - 1) / 100)
    print(f"Train error (MAE): {train_error}")
    print('------------')

    # MSE
    print('Mean Squared Error:', (root_mean_squared_error(y_test,y_pred))**2)
    # RMSE = SQRT di MSE
    print('Root Mean Squared Error:', root_mean_squared_error(y_test,y_pred), '-> km^2 =', (np.exp(root_mean_squared_error(y_test, y_pred)) - 1) / 100)

    # Attenzione ai valori nulli per la normalizzazione
    print((y_test == 0).sum(), '/', len(y_test), 'of y_test is 0')

    print('------------')

    # Intervalli per la tolleranza dell'errore (in %)
    tolerances = [0.05,0.1,0.3,1] 

    for tolerance in tolerances:
        # Calcolare l'errore relativo (errore assoluto / valore reale)
        err_rel = np.abs(y_test - y_pred)

        # Normalizzazione Min-Max
        err_rel_norm = (err_rel - np.min(err_rel)) / (np.max(err_rel) - np.min(err_rel))

        # Verifica quante previsioni sono accettabili (errore relativo <= tolleranza)
        acceptable_predictions = err_rel_norm <= tolerance

        # Calcolare la percentuale di previsioni accettabili
        accuracy_percentage = np.mean(acceptable_predictions) * 100

        # Stampa l'accuratezza in percentuale
        print(f'Accuracy in percentage (with a tolerance of {tolerance * 100}%): {accuracy_percentage:.2f}%')