# Importowanie funkcji potrzebnej do obliczeń
from converter import calculate
# Lista cykli procesów
processTimeList = []

fp = open("Data.txt", "r")
for line in fp:  # Wczytywanie danych z pliku
    x = line.split(',')
    x.reverse()
    processTimeList.append([int(s) for s in x if s.isdigit()])
fp.close()

# Zapisanie wymaganych wyników do zmiennych
AvOfAverageProcessingTime, AvOfAverageWaitinTime = calculate(processTimeList)

# Zapis wyników do pliku Results
fr = open("Results.txt", "a")
fr.write("LCFS:\n\nSredni czas przetwarzania procesow:\t\t%.2f\nSredni czas oczekiwania procesow:\t\t%.2f\n\n" %
         (AvOfAverageProcessingTime, AvOfAverageWaitinTime))
fr.close()
