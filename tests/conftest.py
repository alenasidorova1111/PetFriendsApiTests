import pytest
from api import PetFriends
from settings import v_em, v_pas
import functools


@pytest.fixture
def get_api_key_for_test():
    """
    Gets user's api key with valid email and password
    """
    pf = PetFriends()

    result = pf.get_api_key(v_em[0], v_pas[0])

    assert result.status_code == 200
    assert len(result.json()['key']) == 56

    yield result.json()['key']


def test_log(func):
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
