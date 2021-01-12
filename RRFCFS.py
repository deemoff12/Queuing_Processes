# Importowanie funkcji potrzebnej do obliczeń
from converter import calculateRR
# Lista cykli procesów
processTimeList = []
# Definicja kwantu czasu
t = 1.5


fp = open("Data.txt", "r")
for line in fp:  # Wczytywanie danych z pliku
    x = line.split(',')
    processTimeList.append([int(s) for s in x if s.isdigit()])
fp.close()

# Zapisanie wymaganych wyników do zmiennych
avOfAverageProcessingTime, avOfAverageWaitinTime = calculateRR(
    processTimeList, t)


# Zapis wyników do pliku Results
fr = open("Results.txt", "a")
fr.write("Round Robin FCFS dla kwantu %.1f:\n\nSredni czas przetwarzania procesow:\t\t%.2f\nSredni czas oczekiwania procesow:\t\t%.2f\n\n" %
         (t, avOfAverageProcessingTime, avOfAverageWaitinTime))
fr.close()
