import pytest
from api import PetFriends
from settings import (positive_param_for_age, positive_param_for_pet_name, positive_param_for_anim_type,
                      negative_param_for_pet_name, negative_param_for_age, negative_param_for_anim_type, w_pet_id)

pf = PetFriends()


class TestUpdateOwnPet:
    @pytest.mark.pos
    @pytest.mark.parametrize("age", [i for i in positive_param_for_age.keys()],
                             ids=[i for i in positive_param_for_age.values()])
    @pytest.mark.parametrize("name", [i for i in positive_param_for_pet_name.keys()],
                             ids=[i for i in positive_param_for_pet_name.values()])
    @pytest.mark.parametrize("animal_type", [i for i in positive_param_for_anim_type.keys()],
                             ids=[i for i in positive_param_for_anim_type.values()])
    def test_positive(self, get_api_key_for_test, name, animal_type, age):
        """
        Tests if it's possible to update own pet's info with valid data
        """

        result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        if len(result.json()['pets']) == 0:
            pf.add_new_pet(get_api_key_for_test, "Фунтик1", "Siam cat", "5", "images/cat.jpg")
            result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        pet_id = result.json()['pets'][0]['id']

        result = pf.update_pet(get_api_key_for_test, pet_id, name, animal_type, age)
        my_pets = pf.get_list_of_pets(get_api_key_for_test, "my_pets").json()['pets']

        assert name in my_pets[0].values()
        assert result.status_code == 200

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    @pytest.mark.parametrize("age", [i for i in negative_param_for_age.keys()],
                             ids=[i for i in negative_param_for_age.values()])
    @pytest.mark.parametrize("name", [i for i in negative_param_for_pet_name.keys()],
                             ids=[i for i in negative_param_for_pet_name.values()])
    @pytest.mark.parametrize("animal_type", [i for i in negative_param_for_anim_type.keys()],
                             ids=[i for i in negative_param_for_anim_type.values()])
    def test_negative_wrong_age_name_type(self, get_api_key_for_test, name, animal_type, age):
        """
        Tests if it's possible to update own pet's info with valid data
        """

        result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        if len(result.json()['pets']) == 0:
            pf.add_new_pet(get_api_key_for_test, "Фунтик1", "Siam cat", "5", "images/cat.jpg")
            result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        pet_id = result.json()['pets'][0]['id']

        result = pf.update_pet(get_api_key_for_test, pet_id, name, animal_type, age)
        my_pets = pf.get_list_of_pets(get_api_key_for_test, "my_pets").json()['pets']

        assert name in my_pets[0].values()
        assert result.status_code == 200

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_negative_wrong_pet_id(self, get_api_key_for_test, name='Фунтик2', animal_type='Siam catt', age=4):
        """
        Tests if it's possible to update own pet's info with valid data
        """

        result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        if len(result.json()['pets']) > 0:
            pet_id = w_pet_id
            result = pf.update_pet(get_api_key_for_test, pet_id, name, animal_type, age)
            assert result.status_code == 400
        else:
            raise Exception("There is no my pets")
