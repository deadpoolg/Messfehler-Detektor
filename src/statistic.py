import statistics

def berechne_mittelwert(d):
    if not d:
        return 0
    s = 0
    i = 0
    while i < len(d):
        s = s + float(d[i])
        i = i + 1
    return s / len(d)

def berechne_median(d):
    if not d:
        return 0
    return statistics.median([float(x) for x in d])

def berechne_spannweite(d):
    if not d:
        return 0
    m1 = float(d[0])
    m2 = float(d[0])
    j = 0
    while j < len(d):
        v = float(d[j])
        if v > m1:
            m1 = v
        if v < m2:
            m2 = v
        j = j + 1
    return m1 - m2

def berechne_standardabweichung(d):
    if not d:
        return 0
    vals = [float(x) for x in d]
    try:
        return statistics.pstdev(vals)
    except statistics.StatisticsError:
        return 0
