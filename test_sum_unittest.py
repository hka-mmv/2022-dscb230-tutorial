import unittest


class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Summe sollte 6 ergeben.")

    def test_sum_tuple(self):
        # self.assertEqual(sum((1, 2, 3)), 6, "Summe in Tupel sollte 6 ergeben.")
        self.assertEqual(sum((1, 2, 2)), 6, "Summe in Tupel sollte 6 ergeben.")


"""
Vor dem Ausführen von Code liest der Python-Interpreter die Quelldatei und definiert nur wenige spezielle Variablen / globale Variablen.
Wenn der Python-Interpreter dieses Modul (die Quelldatei) als Hauptprogramm ausführt, setzt er die spezielle Variable __name__ auf den Wert "__main__".
Wenn diese Datei aus einem anderen Modul importiert wird, wird __name__ auf den Namen des Moduls gesetzt.
Der Name des Moduls ist als Wert für die globale Variable __name__ verfügbar.

Vorteile:
1. In jedem Python-Modul ist __name__ definiert. Wenn dies "__main__" ist, bedeutet dies, dass das Modul vom Benutzer eigenständig (engl. Standalone) ausgeführt wird und wir entsprechende Aktionen ausführen können.

2. Wenn Sie dieses Skript als Modul in ein anderes Skript importieren, wird __name__ auf den Namen des Skripts / Moduls gesetzt.

3. Python-Dateien können entweder als wiederverwendbare Module oder als eigenständige Programme fungieren.

4. if __name__ == "main": wird zum Ausführen eines Codes nur verwendet, wenn die Datei direkt ausgeführt und nicht importiert wurde.

"""

""" Auführbarbeit dieser Datei ohne folgeden Code im Terminal:
python -m unittest test_sum_unittest
"""

# if __name__ == '__main__':
#     unittest.main()
    