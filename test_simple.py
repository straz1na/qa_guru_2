import pytest

@pytest.fixture(scope='session', autouse=True)
def open_browser():
    """Эта фикстура вызывает один раз автоматически"""
    print('Я вызываюсь перед тестом')
    yield
    print('Я выполняюсь после теста')

@pytest.fixture()
def configure_mobile_browser():
    """Устанавливает мобильное соотношение сторон браузера"""
    print('Я мобильный бровзер')

@pytest.fixture()
def configure_desktop_browser():
    """Устанавливает десктопное соотношение сторон браузера"""
    print('Я десктопный бровзер')

@pytest.fixture()
def choose_user():
    # выбираем клиента
    user_id = 123
    yield user_id
    print('Удаляем пользователя 123')

# Авторизуемся в github.com
# Создаем репозиторий
# Открываем readme.md
def test_first(configure_mobile_browser):
    print(configure_mobile_browser)

def test_second(configure_desktop_browser):
    assert 1 == 1
    print(configure_desktop_browser)

def test_third(choose_user):
    assert choose_user == 123
    print(choose_user)

