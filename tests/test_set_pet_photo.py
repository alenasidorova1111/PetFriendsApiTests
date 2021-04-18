from api import PetFriends
import pytest
import os

pf = PetFriends()


class TestSetPetPhoto:
    @pytest.mark.xfail(raises=Exception, reason="Server connection error")
    @pytest.mark.pos
    def test_set_pet_photo_with_valid_data(self, get_api_key_for_test, pet_photo='images/cat.jpg'):
        """
        Tests if it's possible to set pet's photo with valid data:
        :param pet_photo: 'images/cat.jpg'
        :return: status check result
        """

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        if len(result.json()['pets']) == 0:
            pf.create_pet_simple(get_api_key_for_test, "Суперкот", "кот", "3")
            result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        pet_id = result.json()['pets'][0]['id']
        result = pf.set_pet_photo(get_api_key_for_test, pet_id, pet_photo)

        assert result.status_code == 200
