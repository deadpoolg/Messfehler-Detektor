def finde_duplikate(d):
    out = []
    i = 0
    n = len(d) - 1
    while i < n:
        if d[i] == d[i+1]:
            out.append(i)
        i = i + 1
    return out

def ist_vollstaendig(d, erwartet):
    return len(d) == erwartet
