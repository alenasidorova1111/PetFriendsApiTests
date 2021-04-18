import pytest
from api import PetFriends
from settings import w_pet_id

pf = PetFriends()


class TestDeleteOwnPet:
    @pytest.mark.pos
    def test_positive(self, get_api_key_for_test):
        """
        Tests if it's possible to delete own pet with valid data
        """

        result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        if len(result.json()['pets']) > 0:
            pet_id = result.json()['pets'][0]['id']
            result = pf.delete_pet(get_api_key_for_test, pet_id)
            my_pets = pf.get_list_of_pets(get_api_key_for_test, "my_pets").json()['pets']

            assert result.status_code == 200
            assert pet_id not in my_pets[0].values()
        else:
            raise Exception("There is no my pets")

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_negative_wrong_pet_id(self, get_api_key_for_test):
        """
        Tests if it's possible to delete own pet with invalid pet_id
        """

        result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        if len(result.json()['pets']) > 0:
            pet_id = w_pet_id
            result = pf.delete_pet(get_api_key_for_test, pet_id)
            assert result.status_code == 400
        else:
            raise Exception("There is no my pets")
