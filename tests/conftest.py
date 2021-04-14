import pytest
from api import PetFriends
from settings import valid_email, valid_password
import functools


@pytest.fixture
def get_api_key_for_test():
    """
    Gets user's api key with valid email and password
    """
    pf = PetFriends()

    status = pf.get_api_key(valid_email, valid_password).status_code
    auth_key = pf.get_api_key(valid_email, valid_password).json()['key']

    assert status == 200
    assert len(auth_key) == 56

    yield auth_key

    # print('fixture teardown')


def test_log(func):
    """Выводит сигнатуру функции и возвращаемое значение"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        log_file = open('log.txt', 'a+')
        result = func(*args, **kwargs)
        headers = str(result.request.headers)
        req_url = str(result.request.url)
        body = str(result.request.body)
        status = str(result.status_code)
        text = str(result.text)
        return log_file.write(f"{func.__name__}\nHeaders:\n{headers}\nURL:\n{req_url}\nRequest body:\n{body}"
                              f"\n\nResponse status:\n{status}\nResponse body:\n{text}\n\n\n")
    return wrapper
