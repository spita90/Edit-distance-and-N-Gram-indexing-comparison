def edit_distance(x, y, stampareTabella=True):
    costi = {'copia': 0, 'sostituzione': 1, 'cancellazione': 1, 'inserimento': 1, 'scambio': 1}
    x, y = ' ' + x, ' ' + y
    m, n = len(x), len(y)

    tab = [[0 for x in range(m)] for y in range(n)]

    for j in range(m):
        tab[0][j] = j

    for i in range(n):
        tab[i][0] = i

    for i in range(1, n):
        for j in range(1, m):
            costo = []
            if x[j] == y[i]:
                costo.append(tab[i - 1][j - 1] + costi['copia'])
            else:
                costo.append(tab[i - 1][j - 1] + costi['sostituzione'])
            costo.append(tab[i - 1][j] + costi['cancellazione'])
            costo.append(tab[i][j - 1] + costi['inserimento'])
            if x[j] == y[i - 1] and x[j - 1] == y[i]:
                costo.append(tab[i - 2][j - 2] + costi['scambio'])

            tab[i][j] = min(costo)

    if stampareTabella:
        stampaTabella(tab, x, y)

    return tab[n-1][m-1]


def stampaTabella(tab, x, y):
    X = [" "]
    for j in x:
        X.append(j)
    print(X)

    for i in range(len(y)):
        row = [y[i]]
        for j in range(len(x)):
            row.append(str(tab[i][j]))
        print(row)
    print("\n")
