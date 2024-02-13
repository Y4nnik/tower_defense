<!-- https://github.com/skills/communicate-using-markdown -->


# Grading Criteria Programmieren T3INF1004
In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)
<!-- Siehe Kenntnisse in prozeduraler Programmierung: zutreffendes wählen und beweisen-->
# - Algorithmenbeschreibung
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L630-L634
    Name des Algorithmus: Gegner Erkennung der Türme
    Problem welches gelöst wird: Die Türme müssen die Gegner erkennen , welche in ihre Schussreichweite kommen, damit diese von ihnen Angegriffen werden können.
    Beschreibung der Lösung: Es wird für jeden Lebenenen Geegner geprüft, ob dieser sich in der Schussreichweite des Turms befindet, da die Türme jeweils nur eine Gewisse Anzahl an Feinen gleichzeitig angreifen sollen (max_targets) wird zusätzlich geprüft ob die Türme überhaupt noch weitere Gegner angreifen können (targets_number) und um zu verhindern, dass Gegner mehrmals angegriffen werden, wird noch überprüft, ob sie sich bereits in der Liste der "anvisierten" Gegner befinden (target_enemys). Sollten diese ganzen Voraussetzungen erfüllt sein wird der Gegner in die Liste der "anvisierten" Gegner hinzugefügt und die Anzahl der Gegner die der Turm gerade angreift (targets_number) um eins erhöht.

    Zum Verständniss: Gegner die sich in target_enemys befinden, werden in einer anderen Funktion dann angegriffen und nehmen Schaden dieser Algorithmus dient ledeglich zur Erkennung dieser Gegner.

# - Datentypen
    https://github.com/Y4nnik/tower_defense/blob/main/merging.py#L30
    An dieser Stelle zeigt sich ein erweitertes Verständniss der verschiedenen Datentypen, da verschieden Datentypen durch Umwandlung kombiniert werden.
    Dieses Wissen lässt sich auch an vielen anderen Stellen im Programmtext erkennen
# - E/A-Operationen und Dateiverarbeitung
    Da wir ein Videospiel als Projekt haben, besteht dies aus sehr vielen Ein- und Ausgabe-Operationen:
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L897
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L898
    In diesen 2 Zeilen, wird wenn die Escape-Taste auf der Tastatur gedrückt wird der Spielmodus auf "paused" gestellt was zur folge hat, dass nun das Pause-Menu angezeigt wird und das Spiel pausiert.
# - Operatoren
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L538-L541
    In diesen Zeilen, wird der Schaden des ausgewählten Archer Turms nach Mausklick auf das Upgrade Feld, durch eine Addition erhöht.
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L113
    In dieser Zeile wird der Betrag Bewegungsvektor eines Gegners, durch eine Multiplikation mit dem Verlangsamungswert eines Slower Towers (Der Wert ist natürlich kleiner 1) verringert ohne jedoch dabei seine Richtung zu ändern.

# - Kontrollstrukturen
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L104-L107
    In der 4. Zeile dieses Codabschnittes befindet sich eine Kontrollstruktur, die prüft, ob Gegner die sterben überhaupt noch am Leben waren. Dies war nötig, da es passieren konnte, das Gegner das Ende des weges erreicht hatten, deswegen aus der Liste entfernt wurden, aber im gleichen Moment auch durch Turmschaden gestorben wären, sie wären also doppelt aus der Liste entfernt worden, was zu einem Absturz führte.

# - Funktionen
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L104-L110
    Funktion, dass Gegner schaden nehmen
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L111-L115
    Funktion, dass Gegner verlangsamt werden 
    ...
# - Stringverarbeitung
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L30-L32
    In diesem Beispiel wird zuerst ein String erstellt, welcher dann in einem Font Rendering verwendet bwird um schlussendlich auf dem Bildschirm angezeigt zu werden.
# - Strukturierte Datentypen
    https://github.com/Y4nnik/tower_defense/blob/03d695fe57b860809f7a5e19f6bafb7830caccfc/merging.py#L76-L77
    Hier ein Beispiel anhand unseres Datentyps "Enemy" welcher als Attribute postion, vector, width, height, health, damage, value, speed und picture hat.- 
# Sie können die Syntax und Semantik von Python (10)
<!-- Eine Stelle aus ihrem Programmieren wählen auf die sie besonders stolz sind und begründen -->


# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)
<!-- Anhand von commits zeigen, wie jeder im Projekt einen Beitrag geleistet hat -->


# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)
<!-- Eine Stelle aus dem Projekt wählen auf die sie besonders stolz sind und begründen -->



## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)
<!-- Beweise anbringen für Nutzen folgender Tools (können links, screenshots und screnncasts sein) -->

<!-- zB -->
<!-- GIT -->
<!-- VSC -->
<!-- Copilot -->
<!-- other -->



## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)
<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

# Sie können existierenden Code analysieren und beurteilen. (5)
<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)
<!-- Which technology did you learn outside of the teacher given input -->
<!-- Did you or your group get help from someone in the classroom (get a support message here from the person who helped you) -->



## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)
<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->
<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->



## Kenntnisse in prozeduraler Programmierung:

# - Algorithmenbeschreibung

# - Datentypen

# - E/A-Operationen und Dateiverarbeitung

# - Operatoren

# - Kontrollstrukturen

# - Funktionen

# - Stringverarbeitung

# - Strukturierte Datentypen


