from api import PetFriends
from settings import (positive_param_for_filter, negative_param_for_filter, w_key)
import pytest

pf = PetFriends()


class TestGetAllPets:
    @pytest.mark.pos
    @pytest.mark.parametrize("filter_", [i for i in positive_param_for_filter.keys()],
                             ids=[i for i in positive_param_for_filter.values()])
    def test_positive_filter_and_key(self, get_api_key_for_test, filter_):
        """
        Tests getting list of all pets with valid api key
        """

        result = pf.get_list_of_pets(get_api_key_for_test, filter_)

        assert result.status_code == 200
        assert len(result.json()['pets']) > 0

    @pytest.mark.neg
    @pytest.mark.parametrize("filter_", [i for i in positive_param_for_filter.keys()],
                             ids=[i for i in positive_param_for_filter.values()])
    @pytest.mark.parametrize("auth_key", [w_key[0]], ids=[w_key[1]])
    def test_positive_filter_and_wrong_key(self, auth_key, filter_):

        result = pf.get_list_of_pets(auth_key, filter_)

        assert result.status_code == 403

    @pytest.mark.neg
    @pytest.mark.parametrize("filter_", [i for i in negative_param_for_filter.keys()],
                             ids=[i for i in negative_param_for_filter.values()])
    def test_negative_filter_and_valid_key(self, get_api_key_for_test, filter_):
        """
        Tests getting list of all pets with invalid filter params
        """

        result = pf.get_list_of_pets(get_api_key_for_test, filter_)

        assert result.status_code == 403
