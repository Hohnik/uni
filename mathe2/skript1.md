Insbesondere ist Q selbst ein angeordneter Körper und zwar der kleinste den es gibt. Der positivbereich ist Q\<u = {m/n: m,n elem |N}

**Zwischenstand:** |Q und |R sind angeordnete Körper. Wo ist jetzt der Unterschied? Vollständigkeit!

**Def.:** Sei K ein Angeordneter Körper und M teilmenge K.
Ein element x elem M heißt {Maximum, Minimum} von M, wenn gilt { y <= x, y >= x } für alle y elem M.

**Bew.:**

- Wenn ein Minimum/Maximum existiert, so ist es eindeutig.
- Wir schreiben max(M) bzw. min(M).

**Bsp.:** Sei K = |Q

1. M1 = {x elem |Q: x <= 2} hat kein minimum,aber max(M1) = 2.
2. M2 = {x elem |Q: x < 2} hat kein Maximum, weil es für jedes x elem M2 ein y elem M2 gibt mit x < y < 2, z.B. y = (x+2)/2
3. M3 = {x elem |Q: x^2 <= 2} hat kein Maximum, weil für jedes x elem M3 gilt x^2 = 2 order x^2 < 2. Aber x^2 = 2 hat keine Lösung in |Q und für x^2 < 2 finden wir (wie oben) stets ein y elem |Q mit x < y und y^2 < 2.
4. M4 = |Z hat kein Maximum, weil für jedes z elem M4 ist z + 1 > z und z + 1 elem M4.

**Def.:**
Sei K ein angeordneter Körper und M teilmenge K.
Die Menge M heißt _nach oben beschränkt_, wenn es ein x elem K (!) gibt mit y <= x für alle y elem M.
Das Element x heißt dann eine _obere Schranke_ von M.
Ein Element s elem K heißt _kleinste obere Schranke (Supremum, kurz sep(M))_, wenn für jede andere obere Schranke x von M gilt:
$$ s \leq x $$
Analog definieren wir: _Nach unten beschränkt_, _Untere Schranke_, _Größte untere Schranke(Infinum, kurz inf(M)_
Die Menge M heißt _beschränkt_, wenn sie nach unten und oben beschränkt ist.

**Bsp.: (fortgesetzt)**

- M1 hat als obere Schranken 2, 3, 4, 10^100, … und sup(M1) = 2. M1 hat keine untere Schranke.
- M2 hat als obere Schranken 24, 30, 40, 10^100, … und sup(M2) = 2 (Obwohl kein Max. existieret!). M2 hat keine untere Schranke.
- M3 hat als obere Schranken 2, 1.5, 4, 10^100, …, aber es gibt keine obere Schranke. **Wir können uns mit rationalen Zahlen beliebig von oben an $\sqrt{2}$, aber keine davon ist die kleinste rationale Zahl oberhalb von $\sqrt{2}$.**
- M4 später!

**Bem.:**

- Wenn M ein Maximum hat, dann ist es auch das Supremum. Allerdings gibt es Meingen ohne Maximum, aber mit Supremum.
- In rationalen Zahlen gibt es Mengen mit oberen Schranken, aber ohne Supremum. Das sind die "Lücken", die die reellen Zahlen schließen.

**Def. 1.6:**
Ein angeordnerter Körper K heißt _vollständig_, wenn jede nicht-leere, nach oben beschränkte Menge ein Supremum in K besitzt.

**Bem.:**
|Q ist nicht vollständig. (Bsp. M3)

**Satz 1.7:** (Ohne Beweis)
Es gibt genau einen vollständigen, angeordneten Körper. Dieser ist |R.

**Bsp.:**
\sqrt{2} elem |R, denn \sqrt{2} = sup{x elem |R: x^2 \leq 2}

a) zu $0<x<y$ gibt es ein $n \in \mathbb{N}$ mit $n\times x > y$  
b) zu $x>0$ gibt es ein $n \in \mathbb{N}$ mit $\frac{1}{n}<x$  
c) zu $x \in \mathbb{R}$ existiert $m = max\{z \in \mathbb{Z}: z \le x\}$  