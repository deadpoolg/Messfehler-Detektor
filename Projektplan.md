# 8-Wochen-Roadmap: Messfehler-Detektor

> **Ziel:** Funktionierender Prototyp in 8 Wochen.  
> **Motto:** "Erst zum Laufen bringen, dann schön machen."

## Phase 1: Setup & Grundlagen (Wochen 1-2)

### Woche 1: Die Infrastruktur steht

**Fokus:** Umgebung einrichten & Datei einlesen.

- [x] Installiere Python & VS Code (falls nicht vorhanden).
- [x] Erstelle den Ordner `messfehler_detector`.
- [x] Erstelle darin die Unterordner `src` (für Code) und `daten` (für CSV-Dateien).
- [x] Erstelle eine Test-Datei `daten/test.csv` mit folgendem Inhalt:
  ```csv
  Zeit,Wert
  1,10.5
  2,11.0
  3,10.8
  4,50.0
  5,10.9
  ```
- [x] **Programmieren:** Schreibe die Funktion `lade_csv` in `utils.py`.
  - Ziel: Die Datei wird eingelesen und du hast zwei Listen: `x_werte` und `y_werte`.
  - Test: Drucke die Listen mit `print()` aus.

### Woche 2: Statistik (Der einfache Teil)

**Fokus:** Mathematische Grundlagen.

- [ ] Arbeite in `statistik.py`.
- [ ] Implementiere `berechne_mittelwert`: Summe aller Werte geteilt durch Anzahl.
- [ ] Implementiere `berechne_spannweite`: Maximum minus Minimum.
- [ ] Nutze für `berechne_median` und `berechne_standardabweichung` das Python-Modul `statistics` (Erfinde das Rad nicht neu!).
  ```python
  import statistics
  return statistics.median(daten)
  ```
- **Checkpoint:** Dein Programm liest die CSV und gibt korrekt Mittelwert (18.64) und Median (10.9) der Testdatei aus.

## Phase 2: Die Logik (Wochen 3-5)

### Woche 3: Einfache Fehlererkennung

**Fokus:** Was fehlt oder ist doppelt?

- [ ] Arbeite in `regeln.py`.
- [ ] **Duplikate:** Gehe die Liste durch. Wenn `wert[i] == wert[i+1]`, speichere den Index `i`.
- [ ] **Vollständigkeit:** Prüfe, ob `len(daten)` der erwarteten Anzahl entspricht.
- **Tipp:** Nutze for-Schleifen mit `range(len(daten) - 1)`.

### Woche 4: Komplexe Fehler (Der Kern)

**Fokus:** Ausreißer und Sprünge finden.

- [ ] **Ausreißer:**
  1. Berechne Mittelwert und Standardabweichung (hast du schon aus Woche 2).
  2. Grenze = 2 * Standardabweichung.
  3. Loop durch Daten: Wenn `abs(wert - mittelwert) > grenze`, ist es ein Fehler.
- [ ] **Sprünge:**
  1. Berechne Differenz zum Vorgänger: `diff = abs(wert[i] - wert[i-1])`.
  2. Wenn `diff > schwellwert` (z.B. 3 * Standardabweichung), ist es ein Sprung.

### Woche 5: Zusammenführung (Integration)

**Fokus:** Alles verbinden.

- [ ] Arbeite in `detector.py` (Main).
- [ ] Rufe alle Funktionen nacheinander auf:
  1. CSV laden.
  2. Statistik berechnen -> `print` Ausgabe.
  3. Fehler suchen -> `print "Fehler an Stelle X gefunden"`.
- **Checkpoint:** Das Programm läuft im Terminal komplett durch und meldet bei der `test.csv` den Wert 50.0 als Ausreißer.

## Phase 3: Visualisierung & Abschluss (Wochen 6-8)

### Woche 6: Grafische Darstellung

**Fokus:** Matplotlib.

- [ ] Arbeite in `plots.py`.
- [ ] Installiere Matplotlib: `pip install matplotlib`.
- [ ] Erstelle einen einfachen Plot: `plt.plot(x_werte, y_werte)`.
- [ ] Markiere Fehler: Nutze `plt.scatter()`, um rote Punkte an den Fehler-Indizes zu zeichnen.
- [ ] Speichere das Bild: `plt.savefig("analyse.png")`.

### Woche 7: Polishing & Doku

**Fokus:** Aufräumen.

- [ ] Fange Fehler ab: Was passiert, wenn die CSV nicht existiert? (Nutze `try...except FileNotFoundError`).
- [ ] Kommentiere deinen Code ordentlich (für die Note!).
- [ ] Erstelle `README.md` mit einer Anleitung, wie man das Programm startet.

### Woche 8: Präsentation & Puffer

**Fokus:** Vorbereitung.

- [ ] Erstelle 3 Folien: Problem, Lösung (dein Code), Ergebnis (das Diagramm).
- [ ] Bereite die Live-Demo vor.
- [ ] Schreibe die Reflexion (siehe PRD Punkt 11).

## Chef-Tipps für die Note 1

1. **Hardcoden verboten:** Schreibe keine festen Pfade wie `C:\Users\Kevin\Desktop\...` in den Code. Nutze relative Pfade (`daten/datei.csv`).
2. **Git nutzen:** Wenn du es kannst, mache jede Woche einen Commit. Lehrer lieben Versionshistorie.
3. **Fehlertoleranz:** Dein Programm darf nicht abstürzen, wenn in der CSV mal "Bananenbrot" statt einer Zahl steht.
