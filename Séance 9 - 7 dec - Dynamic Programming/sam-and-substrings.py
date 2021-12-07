def substrings(n):
    t = int(len(n))
    somme = [0 for i in range(t)]
    somme[0] = int(n[0])
    if t == 1:
        return somme[0]
    somme[1] = 11 * somme[0] + 2 * int(n[1])
    if type == 2:
        return somme[1]
    for i in range(2, t):
        somme[i] = (10 * (somme[i - 1] - somme[i - 2]) + somme[i - 1] + (i + 1) * int(n[i])) % 1000000007
    return somme[t - 1]