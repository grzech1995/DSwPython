from operator import attrgetter

#Zdefiniowanie klasy Movie
class Movie:

    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

    def __repr__(self):
        return '{' + self.title + ', ' + self.year + ', ' + str(self.score) + '}'

#Stworzenie listy filmów
movies = [
    Movie('Bad Boys 2', '2003', 5.5),
    Movie('Aliens', '1986', 8.0),
    Movie('American Pie', '1999', 5.5),
    Movie('Die Hard 3', '1995', 6.2),
    Movie("Harry Potter and the Sorcerer's Stone", '2001', 7.3),
    Movie('Apocalypse Now', '1979', 8.5),
    Movie('Platoon', '1986', 9.0),
    Movie('Die Hard 5', '2013', 2.0),
    Movie('Armageddon', '1998', 5.7),
    Movie('Men In Black', '1997', 6.2),
    Movie('Rocky 4', '1985', 7.0)
]

#Sortowanie listy
# 1. Sortowanie po tytule filmu ('title')
movies.sort(key=lambda x: x.title)
print("Lista posortowana wg tytułów /A-Z/:")
print(movies)
print(' ')

# 2. Sortowanie po roku produkcji i tytule filmu ('year' i 'title' )
print("Lista posortowana wg roku produkcji i tytułach filmów:")
movies.sort(key=lambda x: (x.year, x.title))
print(movies)
# 2a. Sortowanie po tytule i roku produkcji
print("Lista posortowana wg tytułów i roku produkcji filmów:")
movies.sort(key=lambda x: (x.title, x.year))
print(movies)
print(' ')

# 3. Sortowanie po ocenie od najwyższej
print("Lista posortowana wg oceny krytyków /od najwyższej/:")
movies.sort(key=lambda x: -x.score)
print(movies)
print(' ')

# 4. Sortowanie po roku produkcji (od najnowszego) i tytule
print("Lista posortowana wg roku produkcji /od najnowszego/ i tytułu /Z-A/:")
movies.sort(key=lambda x: (x.year, x.title), reverse=True)
print(movies)
print(' ')

# 5. Sortowanie po ocenie i następnie tytule - z wykorzystaniem operatora attrgetter
print("Lista posortowana wg oceny /od najniższej/ i tytułu filmu:")
movies.sort(key=attrgetter('score', 'title'))
print(movies)
print(' ')


#Pytania
# 1. Jak wyświetlić listę z obiektami jeden pod drugim?
# 2. Jak zapisać polecenie posortowania wg dwóch argumentów w kluczu, ale żeby tylko jeden był reverse=True? - przykład nr 4?