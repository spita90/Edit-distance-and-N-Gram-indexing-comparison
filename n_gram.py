def n_gram(string, n):
    if 2 <= n <= 4:
        strlen = len(string)
        if strlen >= n:
            ngram = []
            for i in range(strlen - n + 1):
                ngram.append(string[i:i+n])
            return ngram
        else:
            return []
    else:
        print("Dimensione di n non accettabile. Deve essere 2<=n<=4")
