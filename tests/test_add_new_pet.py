from api import PetFriends
from settings import (positive_param_for_age, positive_param_for_pet_name, positive_param_for_anim_type,
                      negative_param_for_pet_name, negative_param_for_age, negative_param_for_anim_type, w_key)
import pytest
import os

pf = PetFriends()


class TestAddNewPet:
    @pytest.mark.pos
    @pytest.mark.parametrize("age", [i for i in positive_param_for_age.keys()],
                             ids=[i for i in positive_param_for_age.values()])
    @pytest.mark.parametrize("name", [i for i in positive_param_for_pet_name.keys()],
                             ids=[i for i in positive_param_for_pet_name.values()])
    @pytest.mark.parametrize("animal_type", [i for i in positive_param_for_anim_type.keys()],
                             ids=[i for i in positive_param_for_anim_type.values()])
    def test_positive(self, get_api_key_for_test, name, animal_type, age, pet_photo='images/cat.jpg'):
        """
        Tests if it's possible to add new pet with valid data:
        :param name: name of new pet
        :param animal_type: animal type of new pet
        :param age: age of new pet
        :param pet_photo: photo of new pet
        :return: 1) status check result
                 2) name check result
        """

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        result = pf.add_new_pet(get_api_key_for_test, name, animal_type, age, pet_photo)

        assert result.status_code == 200
        assert result.json()['name'] == name
        assert result.json()['age'] == age or result.json()['age'] == str(age)
        assert result.json()['animal_type'] == animal_type
        assert result.json()['pet_photo'].startswith('images/cat.jpg')

        return result

    @pytest.mark.neg
    @pytest.mark.parametrize("age", [i for i in positive_param_for_age.keys()],
                             ids=[i for i in positive_param_for_age.values()])
    @pytest.mark.parametrize("name", [i for i in positive_param_for_pet_name.keys()],
                             ids=[i for i in positive_param_for_pet_name.values()])
    @pytest.mark.parametrize("animal_type", [i for i in positive_param_for_anim_type.keys()],
                             ids=[i for i in positive_param_for_anim_type.values()])
    @pytest.mark.parametrize("auth_key", [w_key[0]], ids=[w_key[1]])
    def test_positive_params_and_wrong_key(self, auth_key, name, animal_type, age, pet_photo='images/cat.jpg'):

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

        assert result.status_code == 403

    @pytest.mark.neg
    @pytest.mark.parametrize("age", [i for i in negative_param_for_age.keys()],
                             ids=[i for i in negative_param_for_age.values()])
    @pytest.mark.parametrize("name", [i for i in negative_param_for_pet_name.keys()],
                             ids=[i for i in negative_param_for_pet_name.values()])
    @pytest.mark.parametrize("animal_type", [i for i in negative_param_for_anim_type.keys()],
                             ids=[i for i in negative_param_for_anim_type.values()])
    def test_negative_params(self, get_api_key_for_test, name, animal_type, age, pet_photo='images/cat.jpg'):

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        result = pf.add_new_pet(get_api_key_for_test, name, animal_type, age, pet_photo)

        assert result.status_code == 400

        return result
