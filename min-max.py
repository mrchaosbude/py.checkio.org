def min(*args, **kwargs):
    key = kwargs.get("key", None)
    return None


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    return None


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

'''
In dieser Mission sollst Du Deine eigene Python 3 Variante der built-in Funktionen min und max implementieren. (Du kannst auch Python 2 nutzen)
Die folgenden built-in Funktionen stehen Dir dabei nicht zur Verfügung: __import__, eval, exec, globals. Vergiss nicht, dass Du zwei Funktionen implementieren sollst.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Gib das größte (kleinste) Element eines iterierbaren Arguments oder das größte (kleinste) von zwei oder mehr Argumenten zurück.

Wenn genau ein Positionsargument gegeben ist, sollte es iterierbar sein und sein größtes (kleinstes) Element zurückgegeben werden.
Wenn zwei oder mehr Positionsargumente gegeben sind, wird das größte (kleinste) zurückgegeben.

Das optionale Schlüsselwortargument liefert eine Funktion mit genau einem Argument.
Diese Funktion wird verwendet, um einen Vergleichsschlüssel aus jedem Listenelement zu extrahieren (z. B. key = str.lower).

Wenn mehrere Elemente maximal (minimal) sind, gibt Deine Funktion das erste, das gefunden wird, zurück.

Wirf ruhig auch einen Blick in die Python Dokumentation: Built-in Functions

Eingabe: Entweder ein iterierbares Positionsargument oder zwei oder mehr Positionsargumente sowie, optional, ein Schlüsselwortargument als Funktion.

Ausgabe: Das größte Element für die "max"-Funktion und das kleinste für die "min"-Funktion.

Beispiele:

max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]

1
2
3
4
5
6
7
Wozu das gut ist:
Diese Aufgabe wird Dir helfen, zu verstehen, wie einige der built-in Funktionen auf tieferer Ebene funktionieren.

Bedingungen:
Alle Testfälle sind korrekt und Deine Funktionen müssen keine Ausnahmen behandeln.
'''