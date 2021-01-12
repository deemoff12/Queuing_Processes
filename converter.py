def calculate(processTimeList):
    # czas czekania poszczególnego procesu
    waitinTime = 0
    # lista oczekiwania poszczególnych procesów
    WaitinTimeList = []
    # Suma czasów oczekiwania w cyklu
    sumUpWaitinTime = 0
    # Średni czas oczekiwania w cyklu
    averageWaitinTime = 0
    # Lista średnich czasów oczekiwania w poszczególnych cyklach
    averageWaitinTimeList = []
    # Średnia średnich czasów czekania
    AvOfAverageWaitinTime = 0
    # Średnia średnich czasów przetwarzania
    AvOfAverageProcessingTime = 0
    # Sumę czasów trwania procesów
    sumUpProcessTime = 0
    # Srednia czasu przetwarzania w cyklu
    avarageProcessingTime = 0
    # Lista średnich czasów przetwarzania poszczególnych cykli
    AverageProcessingTimeList = []

    # Dla pierwszego procesu czas oczekiwania to 0
    WaitinTimeList.append(waitinTime)

    # Liczenie czasów srednich
    for i in range(0, 100):
        for j in range(1, len(processTimeList[i])):
            waitinTime += processTimeList[i][j-1]
            WaitinTimeList.append(waitinTime)
            if j == len(processTimeList[i])-1:
                # Sumowanie czasów oczekiwania
                sumUpWaitinTime = sum(WaitinTimeList)
                # Suma czasów trwania procesów w cyklu
                sumUpProcessTime = sum(processTimeList[i])
                # Średnia czasów przetwarzania procesów w cyklu
                avarageProcessingTime = (
                    sumUpWaitinTime + sumUpProcessTime)/100.0
                # Uzupełnienie listy średnich czasów przetwarzania
                AverageProcessingTimeList.append(avarageProcessingTime)
                # Obliczanie średniej czasu oczekiwania w cyklu
                averageWaitinTime = sumUpWaitinTime/100.0
                # Uzupełnienie listy ze średnimi czasów oczekiwania
                averageWaitinTimeList.append(averageWaitinTime)
                # Czyszczenie zmiennej czasu oczekiwania
                waitinTime = 0
                # Czyszczenie listy przechowującej czas czekania odpowiedniego procesu w cyklu
                WaitinTimeList[:] = []

    # Obliczenie średniej ze średnich czasów oczekiwania procesów
    AvOfAverageWaitinTime = sum(averageWaitinTimeList)/100.0
    # Obliczenie średniej ze średnich czasów przetwarzania wszystkich cykli
    AvOfAverageProcessingTime = sum(AverageProcessingTimeList)/100.0

    return AvOfAverageProcessingTime, AvOfAverageWaitinTime


def calculateRR(processTimeList, t):
    # Suma czasów oczekiwania w cyklu
    sumUpWaitinTime = 0
    # Średnia czasów oczekiwania w cyklu
    averageWaitinTime = 0
    # Lista średnich czasów oczekiwania
    averageWaitinTimeList = []
    # Średnia średnich czasów oczekiwania
    avOfAverageWaitinTime = 0
    # Licznik niezakończonych procesów
    notFinishedCounter = 0
    # Sumę czasów trwania procesów w cyklu
    sumUpProcessTime = 0
    # Srednia czasu przetwarzania w cyklu
    averageProcessingTime = 0
    # Lista średnich czasów przetwarzania poszczególnych cykli
    averageProcessingTimeList = []
    # Średnia średnich czasów przetwarzania
    avOfAverageProcessingTime = 0

    for i in range(0, len(processTimeList)):
        # Wyzerowanie licznika czekania w cyklu
        sumUpWaitinTime = 0
        # Ustawienie licznika niezakończonych procesów
        notFinishedCounter = len(processTimeList[i])
        # print(notFinishedCounter)
        # Obliczenie sumy czasów trwania procesów w cyklu
        sumUpProcessTime = sum(processTimeList[i])
        while notFinishedCounter != 0:
            for j in range(0, len(processTimeList[i])):
                # Sprawdzenie czy proces zajmie pełny kwant czasu
                if processTimeList[i][j] > t:
                    # Obliczenie ile procesów czeka w danym kwancie
                    sumUpWaitinTime += (notFinishedCounter-1)*t
                    # Zmniejszenie wartości procesu o zrealizowany kwant
                    processTimeList[i][j] -= t
                # Warunek sprawdzający czy proces nie zajmię pełnego kwantu, ale nie może być zerowy
                elif processTimeList[i][j] <= t and processTimeList[i][j] != 0:
                    # Zwiększenie sumy czasów oczekiwania o pozostałą wartość procesu
                    sumUpWaitinTime += processTimeList[i][j] * \
                        (notFinishedCounter-1)
                    # Wyzerowanie wartości procesu aby oznaczyć go jako zakończony
                    processTimeList[i][j] = 0
                    # Zmniejszenie ilości niezakończonych procesów
                    notFinishedCounter -= 1
        # Obliczenie średniego czasu oczekiwania w cyklu
        averageWaitinTime = sumUpWaitinTime/100.0
        # Zapisanie średniego czasu oczekiwania w cyklu do listy
        averageWaitinTimeList.append(averageWaitinTime)
        # Obliczenie średniego czasu przetwarzania w cyklu
        averageProcessingTime = (sumUpWaitinTime+sumUpProcessTime)/100.0
        # Zapisanie średniego czasu przetwarzania w cyklu do listy
        averageProcessingTimeList.append(averageProcessingTime)
    # Obliczenie średniej ze średnich czasów oczekiwania
    avOfAverageWaitinTime = sum(averageWaitinTimeList)/100.0
    # Obliczenie średniej ze średnich czasów przetwarzania
    avOfAverageProcessingTime = sum(averageProcessingTimeList)/100.0
    return avOfAverageProcessingTime, avOfAverageWaitinTime
