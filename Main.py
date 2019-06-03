import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from edit_distance import edit_distance
from n_gram import n_gram


dizionario = open("parole_italiane.txt", "r").read().split()
x = random.choice(dizionario)       # scelta casuale di una parola. altrimenti possiamo stabilirla arbitrariamente
y = random.choice(dizionario)       # scelta casuale di una parola. altrimenti possiamo stabilirla arbitrariamente

start = timer()
distanza_di_edit = edit_distance(x.lower(), y.lower())                                      # l'ho reso case-insensitive
stop = timer()
print("La Edit-distance tra " + x +" e " + y +" è " + str(distanza_di_edit) + "\ned è stata trovata in %.6f secondi" % (stop - start))


# INIZIO TEST
print("\n\nINIZIO TEST")
lungh_par = list(range(2, 9))
tempi_edit = []
tempi_ngram = []

for l in lungh_par:
    while True:
        parola_da_valutare = random.choice(dizionario)       # scelta casuale della parola di riferimento. altrimenti possiamo stabilirla arbitrariamente
        if len(parola_da_valutare) == l:
            break

    # Edit-Distance
    print("\nEdit-Distance")

    # parametri
    distanza_di_edit = 1

    print("\nLe parole distanti al massimo " + str(distanza_di_edit) + " da " + parola_da_valutare + " sono:")
    risultati = []
    start = timer()
    for parola in dizionario:                                      # case-insensitive e non restituisce la parola stessa
        if (edit_distance(parola.lower(), parola_da_valutare.lower(), False) <= distanza_di_edit) and (parola_da_valutare.lower() != parola.lower()):
            risultati.append(parola)
            print(parola)
    if len(risultati) == 0:
        print("<Nessuna>")
    stop = timer()
    tempo = stop - start
    print("Tempo richiesto: %.6f secondi" % tempo)
    tempi_edit.append(tempo)

    # N-gram
    print("\nN-gram")

    # parametri
    n = 2
    coefficiente_di_Jackard = 0.65

    print("\nLe parole con "+str(n)+"-grammi comuni oltre lo "+str(coefficiente_di_Jackard)+" del coeff. di Jackard a quelli di "+parola_da_valutare+" sono:")
    ngram_da_valutare = n_gram(parola_da_valutare.lower(), n)
    risultati = []
    start = timer()
    for parola in dizionario:
        common = 0
        ngram_parola = n_gram(parola.lower(), n)
        for i in ngram_da_valutare:
            if i in ngram_parola:
                common += 1
        if (common/(len(ngram_da_valutare)+len(ngram_parola)-common) > coefficiente_di_Jackard) and (parola.lower() != parola_da_valutare.lower()):
            risultati.append(parola)
            print(parola)
    if len(risultati) == 0:
        print("<Nessuna>")
    stop = timer()
    tempo = stop - start
    print("Tempo richiesto: %.6f secondi" % tempo)
    tempi_ngram.append(tempo)

plt.plot(lungh_par, tempi_edit)
plt.plot(lungh_par, tempi_ngram)
plt.title("Edit-distance vs N-gram")
plt.xlabel("lunghezza parola")
plt.ylabel("secondi")
plt.legend(["Edit", "N-gram"])
plt.show()
