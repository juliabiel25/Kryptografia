### Czy	taki	sposób	ukrywania	informacji	w	obrazie	jest	odporny	na	ataki	i	próby	zniszczenia	osadzonej	wiadomości?

Nie. Odczytanie wiadomości polega wyłącznie na znalezieniu kolejności w jakiej bity są zapisywane na poszczególnych pikselach. W mojej implementacji kolejeność jest najprostsza z możliwych (tj. iteracja po kolejnych wierszach, kolumnach i liczbach RGB), a więc i odczytanie wiadomości jest bardzo proste.

Zakładając, że bity zostały zapisane w maksymalnie losowej kolejności na poszczególnych pikselach obrazu, problem odczytania wiadomości będzie równy problemowi wykonania wszystkich możliwych permutacji bitów, a więc 3 * liczba_pikseli_w_obrazie permutacji.

Wiadomość może być dość łatwo zniszczona, poprzez jakąkolwiek edycję przesyłanego obrazu, w tym zwykłą kompresję, która może odrzucić interesujące nas piksele przechowujące naszą wiadomość.

### Maksymalny rozmiar wiadomości jaka może zostać ukryta:
liczba_pikseli * 3 bitów, 

czyli maksymalnie floor(liczba_pikseli * 3 / 8) znaków
