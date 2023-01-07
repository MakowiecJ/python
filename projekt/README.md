Aplikacja imitująca działanie słownika T9 w telefonie komórkowym.

Domyślnie obsługiwanym językiem jest angielski (słówka zamieszczone w pliku ‘english.txt’), jednak język może być dowolny o ile słówka nie zawierają polskich liter.

Działanie opiera się na wczytaniu słówek do struktury drzewiastej, w której każdy węzeł odpowiada wciśnięciu pewnej kombinacji klawiszy.

Graficzny interfejs oparty jest na tkinter, podczas wciskania klawiszy podświetlać się będą na zielono przyciski, których wciśnięcie spowoduję akcję opisaną na przycisku, chodzi o przycisk „ok” który zatwierdza słowo o ile takie istnieje oraz przycisk „change” który zmienia słowo, jeśli w danym węźle znajduje się więcej słów, które odpowiadają wciśniętej kombinacji.

Aplikację można uruchomić wpisując polecenie ```python main.py```