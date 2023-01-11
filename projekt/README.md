# Aplikacja imitująca działanie słownika T9 w telefonie komórkowym.

Domyślnie obsługiwanym językiem jest angielski (słówka zamieszczone w pliku ‘english.txt’), jednak język może być dowolny o ile słówka nie zawierają polskich liter.

Działanie opiera się na wczytaniu słówek do struktury drzewiastej, w której każdy węzeł odpowiada wciśnięciu pewnej kombinacji klawiszy. Każdy węzeł posiada listę słów oraz 8 podwęzłów, które odpowiadają wciśnięciu następnego klawisza z literkami.

Jeśli lista słów w węźle jest pusta, oznacza to że w słowniku nie posiadamy słowa odpowiadającemu wciśniętym klawiszom.
Jeśli któryś z podwęzłów jest nullem, oznacza to że wciśnięcie klawisza który odpowiada temu podwęzłowi (np. node[0] - klawisz 2) kończy naszą wędrówkę po drzewie.

Aplikacja nie przewiduje w przyszłość (chodzi o sytuację, gdy nie dokończymy całego słowa, ale już jednoznacznie wiadomo o jakie słowo chodzi), choć można by to zaimplementować sprawdzając w każdym kroku wszystkie podwęzły i wszystkie listy słów, czy znajduje się dokładnie jedno słowo w tym zbiorze. 

### Na chwilę obecną musimy wcisnąć dokładnie tyle klawiszy ile literek ma nasze słówko np. "hello" - klawisze 4,3,5,5,6.

Graficzny interfejs oparty jest na tkinter, podczas wciskania klawiszy podświetlać się będą na zielono 2 przyciski, których wciśnięcie spowoduję akcję opisaną na przycisku, chodzi o przycisk „ok” który zatwierdza słowo o ile takie istnieje oraz przycisk „change” który zmienia słowo, jeśli w danym węźle znajduje się więcej słów, które odpowiadają wciśniętej kombinacji.

Aplikację można uruchomić wpisując polecenie ```python main.py``` znajdując się w folderze projektowym.