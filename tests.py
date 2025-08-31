from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def setup_method(self):
        self.collector = BooksCollector()
    


    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    # Тест установки жанра книги
    def test_set_book_genre_valid_data(self):
        self.collector.add_new_book("Мурка украла сосиску")
        self.collector.set_book_genre("Мурка украла сосиску", "Детективы")
        assert self.collector.get_book_genre("Мурка украла сосиску") == "Детективы"

    # Тест получения жанра книги
    def test_get_book_genre_existing_book(self):
        self.collector.add_new_book("Жизнь кота Васьки")
        self.collector.set_book_genre("Жизнь кота Васьки", "Романы")
        assert self.collector.get_book_genre("Жизнь кота Васьки") == "Романы"


    # Тест вывода списка книг конкретного жанра
    def test_get_books_with_specific_genre_valid_genre(self):
        self.collector.add_new_book("Робокот")
        self.collector.set_book_genre("Робокот", "Фантастика")
        result = self.collector.get_books_with_specific_genre("Фантастика")
        assert result == ["Робокот"]

    # Тест получения всех книг
    def test_get_books_genre_all_books(self):
        self.collector.add_new_book("Хвосты")
        self.collector.add_new_book("Лапки")
        expected_result = {"Хвосты": '', "Лапки": ''}
        assert self.collector.get_books_genre() == expected_result

    # Тест фильтрации детских книг
    def test_get_books_for_children_exclude_adult_genres(self):
        self.collector.add_new_book("Смешные пушистики")
        self.collector.set_book_genre("Смешные пушистики", "Комедии")
        self.collector.add_new_book("Острые когти")
        self.collector.set_book_genre("Острые когти", "Ужасы")
        children_books = self.collector.get_books_for_children()
        assert children_books == ["Смешные пушистики"]


    # Тест добавления книги в избранное
    def test_add_book_in_favorites(self):
        self.collector.add_new_book("Гарри Коттер")
        self.collector.add_book_in_favorites("Гарри Коттер")
        assert "Гарри Коттер" in self.collector.get_list_of_favorites_books()

    # Тест удаления книги из избранного
    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("Властелин котец")
        self.collector.add_book_in_favorites("Властелин котец")
        self.collector.delete_book_from_favorites("Властелин котец")
        assert "Властелин котец" not in self.collector.get_list_of_favorites_books()

    # Тест получения списка избранных книг
    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book("Маленький котенок")
        self.collector.add_book_in_favorites("Маленький котенок")
        favorites = self.collector.get_list_of_favorites_books()
        assert favorites == ["Маленький котенок"]
