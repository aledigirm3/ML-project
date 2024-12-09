import numpy as np

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import r2_score

# Valutazione performace
def evaluate(y_test, y_pred, y_train, y_train_pred, max_area):

    # R2 score
    #print(f"R²: {r2_score(y_test, y_pred)}")
    #print(f"Train R²: {r2_score(y_train, y_train_pred)}")
    #print('------------')

    # MAE.
    mae = mean_absolute_error(y_test, y_pred)
    print('Mean Absolute Error:', mae, '-> km^2 =', (np.exp(mae) - 1) / 100)
    print(f"Train error (MAE): {mean_absolute_error(y_train, y_train_pred)}")
    print('------------')

    # MSE
    print('Mean Squared Error:', (root_mean_squared_error(y_test,y_pred))**2)
    # RMSE = SQRT di MSE
    rmse = root_mean_squared_error(y_test,y_pred)
    print('Root Mean Squared Error:', rmse, '-> km^2 =', (np.exp(rmse) - 1) / 100)

    # Attenzione ai valori nulli per la normalizzazione
    print((y_test == 0).sum(), '/', len(y_test), 'of y_test is 0')

    print('------------')

    # Calcola la precisione
    precision_percentage = (1 - (rmse / max_area)) * 100

    print(f"Precisione del modello rispetto all'area massima: {precision_percentage:.2f}%")
    print('------------')


    # Intervalli per la tolleranza dell'errore (in %)
    tolerances = [0.05, 0.1, 0.25, 0.5] 

    # Calcolare l'errore relativo
    err_rel = np.abs(y_test - y_pred)

    # Normalizzazione Min-Max
    err_rel_norm = (err_rel - np.min(err_rel)) / (np.max(err_rel) - np.min(err_rel))

    for tolerance in tolerances:

        # Verifica quante previsioni sono accettabili (errore relativo <= tolleranza)
        acceptable_predictions = err_rel_norm <= tolerance

        # Calcolare la percentuale di previsioni accettabili
        accuracy_percentage = np.mean(acceptable_predictions) * 100

        # Stampa l'accuratezza in percentuale
        print(f'Accuracy in percentage (with a tolerance of {tolerance * 100}%): {accuracy_percentage:.2f}%')
   
    
'''
 tolerances = [5,10,30,100] 

    # Calcolare l'errore relativo (errore assoluto / valore reale)
    percent_err = (np.abs(y_test - y_pred) / max_area) * 100

    for tolerance in tolerances:

        # Verifica quante previsioni sono accettabili (errore relativo <= tolleranza)
        result = percent_err <= tolerance

        # Calcolare la percentuale di previsioni accettabili
        accuracy_percentage = (np.sum(result) / len(result)) * 100

        # Stampa l'accuratezza in percentuale
        print(f'Accuracy in percentage (with a tolerance of {tolerance}%): {accuracy_percentage:.2f}%')


        '''