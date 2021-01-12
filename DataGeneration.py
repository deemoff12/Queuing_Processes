import random
with open("Data.txt", "w") as file:  # Generowanie danych do pliku
    for i in range(100):
        for j in range(100):
            a = random.randint(1, 20)
            file.write(str(a)+',')
        file.write('\n')

print(a)
