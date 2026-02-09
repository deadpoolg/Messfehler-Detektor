# Product Requirements Document (PRD)
## Automatischer Fehler-Detektor für Messreihen

**Projekt-Typ:** MINT-Praktikumsprojekt  
**Klassenstufe:** 10. Klasse Gymnasium  
**Dauer:** 4 Monate  
**Version:** 1.0  
**Datum:** Dezember 2024  

---

## Inhaltsverzeichnis

1. [Projektübersicht](#1-projektübersicht)
2. [Projektziele](#2-projektziele)
3. [Technische Spezifikation](#3-technische-spezifikation)
4. [Projektstruktur](#4-projektstruktur)
5. [Modulbeschreibung](#5-modulbeschreibung)
6. [Datenformat](#6-datenformat)
7. [Funktionale Anforderungen](#7-funktionale-anforderungen)
8. [Entwicklungsplan](#8-entwicklungsplan)
9. [Erfolgskriterien](#9-erfolgskriterien)
10. [Grenzen und Einschränkungen](#10-grenzen-und-einschränkungen)
11. [Reflexion und Präsentation](#11-reflexion-und-präsentation)

---

## 1. Projektübersicht

### 1.1 Beschreibung

Entwicklung eines Python-Programms zur automatischen Analyse von Messreihen aus naturwissenschaftlichen Experimenten (Biologie, Chemie, Physik). Das Programm liest Messdaten aus CSV-Dateien ein, führt statistische Auswertungen durch, erkennt typische Messfehler und stellt die Ergebnisse grafisch dar.

### 1.2 Motivation

In naturwissenschaftlichen Experimenten entstehen häufig große Mengen an Messdaten. Die manuelle Überprüfung auf Fehler ist zeitaufwändig und fehleranfällig. Dieses Tool unterstützt Schüler:innen und Lehrkräfte bei der systematischen Datenanalyse.

### 1.3 Zielgruppe

- Schüler:innen der Sekundarstufe I und II
- MINT-Klassen und -Kurse
- Lehrkräfte zur Unterstützung bei Experimentauswertungen

---

## 2. Projektziele

### 2.1 Hauptziele

- ✅ Automatisierte Einlesung und Validierung von Messdaten
- ✅ Berechnung statistischer Kennwerte
- ✅ Erkennung von vier Hauptfehlertypen
- ✅ Visuelle Darstellung der Analyse-Ergebnisse

### 2.2 Lernziele

- Strukturierte Softwareentwicklung (Modularisierung)
- Umgang mit Dateiformaten (CSV)
- Anwendung statistischer Methoden
- Algorithmus-Design
- Datenvisualisierung

### 2.3 Nicht-Ziele

Das Projekt umfasst **NICHT**:
- Machine Learning oder KI-Algorithmen
- Grafische Benutzeroberfläche (GUI)
- Automatische Fehlerkorrektur
- Webbasierte Anwendung
- Datenbank-Integration

---

## 3. Technische Spezifikation

### 3.1 Technologie-Stack

| Komponente | Technologie | Version |
|------------|-------------|---------|
| Programmiersprache | Python | ≥ 3.8 |
| Datenverarbeitung | Standardbibliothek `csv` | - |
| Statistik | `statistics`, `math` | - |
| Visualisierung | `matplotlib` | ≥ 3.5.0 |
| Type Hints | `typing` | - |

### 3.2 Installation

```bash
# Repository klonen
git clone [repository-url]
cd messfehler_detector

# Abhängigkeiten installieren
pip install -r requirements.txt
```

### 3.3 Systemanforderungen

- **Betriebssystem:** Windows, macOS, Linux
- **RAM:** Mindestens 512 MB
- **Speicher:** 50 MB freier Speicherplatz

---

## 4. Projektstruktur

```
messfehler_detector/
│
├── daten/                          # Testdaten
│   ├── beispiel_korrekt.csv
│   └── beispiel_fehlerhaft.csv
│
├── src/                            # Quellcode
│   ├── detector.py                 # Hauptprogramm
│   ├── statistik.py                # Statistische Berechnungen
│   ├── regeln.py                   # Fehlererkennungslogik
│   ├── plots.py                    # Visualisierung
│   └── utils.py                    # Hilfsfunktionen
│
├── tests/                          # Testfälle
│   └── test_funktionen.py
│
├── docs/                           # Dokumentation
│   └── beispiel_ausgabe.png
│
├── README.md                       # Projektdokumentation
├── requirements.txt                # Python-Abhängigkeiten
└── .gitignore                      # Git-Konfiguration
```

---

## 5. Modulbeschreibung

### 5.1 `detector.py` – Hauptprogramm

**Zweck:** Zentrale Steuerung des Programmablaufs

**Verantwortlichkeiten:**
- Kommandozeilenargumente verarbeiten
- Module orchestrieren
- Ergebnisse formatieren und ausgeben

**Hauptfunktion:**
```python
def main():
    """
    Hauptfunktion des Programms
    
    Ablauf:
    1. CSV-Datei einlesen
    2. Daten validieren
    3. Statistik berechnen
    4. Fehler erkennen
    5. Ergebnisse ausgeben
    6. Diagramm erstellen und speichern
    """
    pass
```

**Ausgabe:**
- Zusammenfassung im Terminal
- Gespeichertes Diagramm (PNG)

---

### 5.2 `statistik.py` – Statistische Auswertung

**Zweck:** Berechnung statistischer Kennwerte

**Funktionen:**

| Funktion | Parameter | Rückgabe | Beschreibung |
|----------|-----------|----------|--------------|
| `berechne_mittelwert()` | `daten: List[float]` | `float` | Arithmetisches Mittel |
| `berechne_median()` | `daten: List[float]` | `float` | Zentralwert der sortierten Reihe |
| `berechne_spannweite()` | `daten: List[float]` | `float` | Differenz Max - Min |
| `berechne_standardabweichung()` | `daten: List[float]` | `float` | Streuungsmaß |

**Verwendete Bibliotheken:**
```python
import statistics
import math
from typing import List
```

**Beispiel:**
```python
daten = [23.5, 24.1, 23.9, 24.0, 23.8]
mittelwert = berechne_mittelwert(daten)  # 23.86
```

---

### 5.3 `regeln.py` – Fehlererkennungslogik

**Zweck:** Erkennung typischer Messfehler durch algorithmische Regeln

**Fehlertypen:**

1. **Sprünge**
   - Plötzliche große Änderungen zwischen aufeinanderfolgenden Messwerten
   - Schwellwert: 3× Standardabweichung

2. **Ausreißer**
   - Werte, die stark vom Durchschnitt abweichen
   - Kriterium: >2× Standardabweichung vom Mittelwert

3. **Duplikate**
   - Identische aufeinanderfolgende Messwerte
   - Verdächtig bei kontinuierlichen Messungen

4. **Fehlende Werte**
   - Lücken in der erwarteten Messreihe
   - Prüfung gegen erwartete Anzahl

**Funktionssignaturen:**
```python
def erkenne_spruenge(daten: List[float], schwellwert: float) -> List[int]:
    """
    Erkennt große Sprünge zwischen aufeinanderfolgenden Werten
    
    Args:
        daten: Liste der Messwerte
        schwellwert: Maximale erlaubte Differenz
    
    Returns:
        Liste der Indizes mit erkannten Sprüngen
    """
    pass

def erkenne_ausreisser(daten: List[float], faktor: float = 2.0) -> List[int]:
    """
    Erkennt Ausreißer basierend auf Standardabweichung
    
    Args:
        daten: Liste der Messwerte
        faktor: Vielfaches der Standardabweichung
    
    Returns:
        Liste der Indizes mit Ausreißern
    """
    pass

def erkenne_duplikate(daten: List[float]) -> List[int]:
    """
    Findet identische aufeinanderfolgende Werte
    
    Args:
        daten: Liste der Messwerte
    
    Returns:
        Liste der Indizes mit Duplikaten
    """
    pass

def pruefe_vollstaendigkeit(daten: List[float], erwartete_anzahl: int) -> bool:
    """
    Prüft, ob alle erwarteten Messwerte vorhanden sind
    
    Args:
        daten: Liste der Messwerte
        erwartete_anzahl: Erwartete Anzahl an Messwerten
    
    Returns:
        True wenn vollständig, sonst False
    """
    pass
```

---

### 5.4 `plots.py` – Visualisierung

**Zweck:** Grafische Darstellung der Messdaten und erkannten Fehler

**Funktionen:**
```python
def erstelle_messreihen_plot(x_werte: List[float], 
                             y_werte: List[float], 
                             titel: str = "Messreihe") -> None:
    """
    Erstellt ein Liniendiagramm der Messwerte
    """
    pass

def markiere_fehlerhafte_punkte(x_werte: List[float], 
                                y_werte: List[float], 
                                fehler_indices: List[int]) -> None:
    """
    Markiert fehlerhafte Punkte rot im Diagramm
    """
    pass

def speichere_diagramm(dateiname: str = "ergebnis.png") -> None:
    """
    Speichert das aktuelle Diagramm als PNG-Datei
    """
    pass
```

**Diagrammelemente:**
- Liniendiagramm mit durchgezogener Linie
- Rote Markierungen (Kreis) für erkannte Fehler
- Beschriftete X- und Y-Achse
- Aussagekräftiger Titel
- Legende zur Erklärung

**Verwendete Bibliothek:**
```python
import matplotlib.pyplot as plt
```

---

### 5.5 `utils.py` – Hilfsfunktionen

**Zweck:** Wiederverwendbare Hilfsfunktionen

**Funktionen:**
```python
def lade_csv(dateipfad: str) -> Tuple[List[float], List[float]]:
    """
    Lädt CSV-Datei und extrahiert X- und Y-Werte
    
    Args:
        dateipfad: Pfad zur CSV-Datei
    
    Returns:
        Tupel mit (x_werte, y_werte)
    
    Raises:
        FileNotFoundError: Datei existiert nicht
        ValueError: Ungültiges Datenformat
    """
    pass

def validiere_daten(daten: List[float]) -> bool:
    """
    Prüft, ob alle Werte numerisch und gültig sind
    
    Args:
        daten: Zu validierende Datenliste
    
    Returns:
        True wenn gültig, sonst False
    """
    pass

def formatiere_ausgabe(statistik_dict: dict) -> str:
    """
    Erstellt lesbare Textausgabe der Statistik
    
    Args:
        statistik_dict: Dictionary mit statistischen Kennwerten
    
    Returns:
        Formatierter String für Terminal-Ausgabe
    """
    pass
```

---

## 6. Datenformat

### 6.1 CSV-Struktur

**Erwartetes Format:**
```csv
Zeit,Messwert
0,23.5
1,24.1
2,23.9
3,24.0
4,23.8
```

### 6.2 Spezifikation

| Element | Anforderung |
|---------|-------------|
| **Erste Zeile** | Header mit Spaltennamen |
| **Erste Spalte** | X-Werte (Zeit, Messnummer, etc.) |
| **Zweite Spalte** | Y-Werte (Messergebnisse) |
| **Dezimaltrennzeichen** | Punkt (`.`) |
| **Trennzeichen** | Komma (`,`) |
| **Zeichenkodierung** | UTF-8 |

### 6.3 Beispieldaten

**Korrekte Messreihe:**
```csv
Zeit,Temperatur
0,20.5
1,20.7
2,20.6
3,20.8
4,20.7
```

**Fehlerhafte Messreihe:**
```csv
Zeit,Temperatur
0,20.5
1,20.7
2,20.6
3,35.2    # Sprung/Ausreißer
4,20.7
5,20.7    # Duplikat
```

---

## 7. Funktionale Anforderungen

### 7.1 Muss-Kriterien (Must Have)

- **FR-001:** CSV-Dateien mit zwei Spalten einlesen
- **FR-002:** Berechnung von Mittelwert, Median, Spannweite
- **FR-003:** Erkennung von Sprüngen
- **FR-004:** Erkennung von Ausreißern
- **FR-005:** Ausgabe der Ergebnisse im Terminal
- **FR-006:** Erstellung eines Liniendiagramms

### 7.2 Soll-Kriterien (Should Have)

- **FR-007:** Berechnung der Standardabweichung
- **FR-008:** Erkennung von Duplikaten
- **FR-009:** Prüfung auf Vollständigkeit
- **FR-010:** Speicherung des Diagramms als PNG
- **FR-011:** Markierung fehlerhafter Punkte im Diagramm

### 7.3 Kann-Kriterien (Nice to Have)

- **FR-012:** Verarbeitung mehrerer CSV-Dateien
- **FR-013:** Konfigurierbare Schwellwerte
- **FR-014:** Export der Ergebnisse als Textdatei
- **FR-015:** Farbcodierung verschiedener Fehlertypen

---

## 8. Entwicklungsplan

### 8.1 Woche 1: Grundgerüst

**Ziel:** Projektstruktur und Basis-Funktionalität

- [ ] Projektordner anlegen
- [ ] `requirements.txt` erstellen
- [ ] `utils.py`: CSV-Einlesen implementieren
- [ ] `detector.py`: Grundgerüst mit `main()`
- [ ] Test mit einfacher CSV-Datei

**Deliverables:**
- Lauffähiges Minimalbeispiel
- Erste Testdatei

---

### 8.2 Woche 2: Statistik-Modul

**Ziel:** Alle statistischen Berechnungen

- [ ] `statistik.py`: Mittelwert-Funktion
- [ ] `statistik.py`: Median-Funktion
- [ ] `statistik.py`: Spannweite-Funktion
- [ ] `statistik.py`: Standardabweichung-Funktion
- [ ] Tests mit bekannten Ergebnissen

**Deliverables:**
- Vollständiges Statistik-Modul
- Dokumentierte Funktionen

---

### 8.3 Woche 3: Fehlererkennungs-Modul

**Ziel:** Implementierung aller Fehlererkennungs-Algorithmen

- [ ] `regeln.py`: Sprung-Erkennung
- [ ] `regeln.py`: Ausreißer-Erkennung
- [ ] `regeln.py`: Duplikat-Erkennung
- [ ] `regeln.py`: Vollständigkeitsprüfung
- [ ] Tests mit fehlerhaften Beispieldaten

**Deliverables:**
- Funktionierendes Fehlererkennungs-Modul
- Beispiel-CSV mit bekannten Fehlern

---

### 8.4 Woche 4: Visualisierung

**Ziel:** Grafische Darstellung der Ergebnisse

- [ ] `plots.py`: Einfaches Liniendiagramm
- [ ] `plots.py`: Markierung fehlerhafter Punkte
- [ ] `plots.py`: Speicherfunktion
- [ ] Integration in `detector.py`

**Deliverables:**
- Vollständiges Plot-Modul
- Beispiel-Diagramm

---

### 8.5 Woche 5-6: Integration und Tests

**Ziel:** Alle Module verbinden und testen

- [ ] Integration aller Module in `detector.py`
- [ ] `test_funktionen.py` erstellen
- [ ] End-to-End-Tests durchführen
- [ ] Fehlerbehandlung implementieren
- [ ] Code-Kommentare vervollständigen

**Deliverables:**
- Vollständig integriertes Programm
- Test-Suite

---

### 8.6 Woche 7-8: Dokumentation und Präsentation

**Ziel:** Projekt abschließen und präsentieren

- [ ] `README.md` schreiben
- [ ] Inline-Kommentare überprüfen
- [ ] Beispiel-Ausgaben dokumentieren
- [ ] Präsentation vorbereiten
- [ ] Reflexion schreiben

**Deliverables:**
- Vollständige Dokumentation
- Präsentationsmaterial
- Abschlussbericht

---

## 9. Erfolgskriterien

### 9.1 Technische Kriterien

Das Projekt gilt als erfolgreich, wenn:

- ✅ Mindestens 2 verschiedene CSV-Dateien korrekt analysiert werden
- ✅ Alle 4 Fehlertypen zuverlässig erkannt werden
- ✅ Statistische Kennwerte mathematisch korrekt berechnet werden
- ✅ Ein aussagekräftiges Diagramm erzeugt wird
- ✅ Das Programm ohne Fehler durchläuft

### 9.2 Code-Qualität

- ✅ Code ist in logische Module aufgeteilt
- ✅ Funktionen haben aussagekräftige Namen
- ✅ Alle Funktionen sind dokumentiert (Docstrings)
- ✅ Kommentare erklären komplexe Stellen
- ✅ Keine redundanten Code-Teile

### 9.3 Dokumentation

- ✅ README erklärt Installation und Verwendung
- ✅ Beispielausgaben sind vorhanden
- ✅ Grenzen des Systems sind dokumentiert
- ✅ Reflexion ist vorhanden

---

## 10. Grenzen und Einschränkungen

### 10.1 Was das Programm NICHT kann

| Einschränkung | Begründung |
|---------------|------------|
| **Physikalische Plausibilität bewerten** | Erfordert Fachwissen über den Experimentkontext |
| **Messfehler automatisch korrigieren** | Risiko falscher Korrekturen, menschliche Entscheidung nötig |
| **Experimentaufbau bewerten** | Systematische Fehler sind algorithmisch nicht erkennbar |
| **Kausale Zusammenhänge erklären** | Statistik ≠ Kausalität |

### 10.2 Warum menschliche Experten wichtig bleiben

- **Fachwissen:** Physikalische/chemische Prozesse müssen verstanden werden
- **Kontext:** Experimentbedingungen beeinflussen Interpretation
- **Entscheidungen:** Umgang mit Fehlern (löschen, korrigieren, akzeptieren) erfordert Urteilsvermögen
- **Validierung:** Algorithmen können falsch-positiv oder falsch-negativ sein

---

## 11. Reflexion und Präsentation

### 11.1 Reflexionsfragen

Für die Abschlusspräsentation sollten folgende Fragen beantwortet werden:

1. **Funktionalität**
   - Welche Fehlertypen erkennt dein Programm zuverlässig?
   - Wo stößt der Algorithmus an Grenzen?

2. **Parameterwahl**
   - Warum ist die Wahl der Schwellwerte wichtig?
   - Wie würdest du optimale Schwellwerte bestimmen?

3. **Erweiterungen**
   - Wie würdest du das Programm erweitern?
   - Welche zusätzlichen Fehlertypen wären interessant?

4. **Lerneffekt**
   - Was hast du über Softwarestruktur gelernt?
   - Welche Herausforderungen gab es?

### 11.2 Präsentationsstruktur

**Vorgeschlagener Aufbau (10-15 Minuten):**

1. **Einleitung (2 Min)**
   - Problem und Motivation
   - Projektziele

2. **Demonstration (5 Min)**
   - Live-Demo mit Beispieldaten
   - Erklärung der Ausgabe

3. **Technische Umsetzung (3 Min)**
   - Architektur-Übersicht
   - Ein Algorithmus im Detail

4. **Reflexion (3 Min)**
   - Erfolge und Herausforderungen
   - Grenzen und Ausblick

5. **Fragen (2 Min)**

---

## Anhang

### A. Beispiel-Ausgabe

```
=== MESSREIHEN-ANALYSE ===

Datei: temperatur_messung.csv
Anzahl Messwerte: 20

--- STATISTIK ---
Mittelwert: 24.3 °C
Median: 24.1 °C
Spannweite: 3.2 °C
Standardabweichung: 0.8 °C

--- FEHLERANALYSE ---
⚠️  2 Sprünge erkannt (Positionen: 7, 14)
    Position 7: Änderung von 2.4°C
    Position 14: Änderung von 3.1°C

⚠️  1 Ausreißer erkannt (Position: 12)
    Wert: 27.5°C (Abweichung: 3.2°C vom Mittelwert)

✓  Keine Duplikate gefunden
✓  Messreihe vollständig (20/20 Werte)

Diagramm gespeichert: analyse_temperatur_messung.png
```

### B. Programmstart

```bash
# Einfache Analyse
python src/detector.py daten/beispiel_fehlerhaft.csv

# Mit benutzerdefiniertem Ausgabename
python src/detector.py daten/messung.csv --output diagramm.png
```

### C. Kontakt und Support

**Projektverantwortliche:** [Dein Name]  
**Schule:** [Schulname]  
**Klasse:** 10. Klasse  
**Betreuer:** [Lehrername]  

---

**Dokument-Ende**