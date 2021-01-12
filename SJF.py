# Importowanie funkcji potrzebnej do obliczeń
from converter import calculate
# Lista cykli procesów
processTimeList = []


fp = open("Data.txt", "r")
for line in fp:  # Wczytywanie danych z pliku
    x = line.split(',')
    processTimeList.append([int(s) for s in x if s.isdigit()])
fp.close()

# Szeregowanie kolejki procesów zgodnie z zasadami SJF
for cycle in range(0, len(processTimeList)):
    processTimeList[cycle].sort()

# Zapisanie wymaganych wyników do zmiennych
AvOfAverageProcessingTime, AvOfAverageWaitinTime = calculate(processTimeList)

# Zapis wyników do pliku Results
fr = open("Results.txt", "a")
fr.write("SJF:\n\nSredni czas przetwarzania procesow:\t\t%.2f\nSredni czas oczekiwania procesow:\t\t%.2f\n\n" %
         (AvOfAverageProcessingTime, AvOfAverageWaitinTime))
fr.close()
