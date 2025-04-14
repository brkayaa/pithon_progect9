import requests
from urllib.parse import urlencode

class YandexOAuth:
    """
    Класс для OAuth-авторизации в Яндексе.
    Получает токен для доступа к API.
    """
    AUTH_URL = "https://oauth.yandex.ru/authorize"
    TOKEN_URL = "https://oauth.yandex.ru/token"

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_auth_url(self):
        """Возвращает URL для запроса прав у пользователя."""
        params = {
            "response_type": "code",
            "client_id": self.client_id,
        }
        return f"{self.AUTH_URL}?{urlencode(params)}"

    def get_token(self, code):
        """Получает OAuth-токен по коду авторизации."""
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(self.TOKEN_URL, data=data)
        return response.json().get("access_token")

class YandexMetrikaAPI:
    """
    Базовый класс для работы с API Яндекс.Метрики.
    """
    API_URL = "https://api-metrika.yandex.net/management/v1/"

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"OAuth {self.token}",
            "Content-Type": "application/json",
        }

    def _make_request(self, method, endpoint, params=None, data=None):
        """Общий метод для API-запросов."""
        url = f"{self.API_URL}{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, params=params, json=data
        )
        response.raise_for_status()
        return response.json()

class YandexMetrikaReports(YandexMetrikaAPI):
    """
    Подкласс для работы с отчётами Яндекс.Метрики.
    """
    REPORTS_URL = "https://api-metrika.yandex.net/stat/v1/data"

    def get_visits(self, counter_id, date_from, date_to):
        """Получает статистику визитов."""
        params = {
            "ids": counter_id,
            "date1": date_from,
            "date2": date_to,
            "metrics": "ym:s:visits,ym:s:pageviews,ym:s:users",
        }
        return self._make_request("GET", "", params=params)

class YandexMetrikaManagement(YandexMetrikaAPI):
    """
    Подкласс для управления счётчиками Яндекс.Метрики.
    """
    def get_counters(self):
        """Получает список счётчиков."""
        return self._make_request("GET", "counters")

    def get_counter_info(self, counter_id):
        """Получает информацию о счётчике."""
        return self._make_request("GET", f"counter/{counter_id}")

# Пример использования
if __name__ == "__main__":
    # 1. Настройка OAuth (замените на свои client_id и client_secret)
    CLIENT_ID = "ваш_client_id"
    CLIENT_SECRET = "ваш_client_secret"
    yandex_oauth = YandexOAuth(CLIENT_ID, CLIENT_SECRET)

    # 2. Получение ссылки для авторизации (перейдите по ней в браузере)
    auth_url = yandex_oauth.get_auth_url()
    print("Перейдите по ссылке и разрешите доступ:", auth_url)

    # 3. Введите полученный код авторизации
    auth_code = input("Введите код авторизации: ")
    token = yandex_oauth.get_token(auth_code)
    print("Ваш токен:", token)

    # 4. Работа с API Метрики
    metrika = YandexMetrikaReports(token)
    counter_id = "ваш_id_счётчика"  # Замените на реальный ID

    # Получаем статистику за последние 7 дней
    stats = metrika.get_visits(counter_id, "7daysAgo", "today")
    print("Статистика визитов:", stats)

    # Управление счётчиками
    management = YandexMetrikaManagement(token)
    counters = management.get_counters()
    print("Список счётчиков:", counters)