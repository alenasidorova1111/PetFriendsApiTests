from api import PetFriends
from settings import (positive_param_for_age, positive_param_for_pet_name, positive_param_for_anim_type,
                      negative_param_for_pet_name, negative_param_for_age, negative_param_for_anim_type)
import pytest

pf = PetFriends()


class TestCreatePetSimple:
    @pytest.mark.pos
    @pytest.mark.parametrize("age", [i for i in positive_param_for_age.keys()],
                             ids=[i for i in positive_param_for_age.values()])
    @pytest.mark.parametrize("name", [i for i in positive_param_for_pet_name.keys()],
                             ids=[i for i in positive_param_for_pet_name.values()])
    @pytest.mark.parametrize("animal_type", [i for i in positive_param_for_anim_type.keys()],
                             ids=[i for i in positive_param_for_anim_type.values()])
    def test_positive(self, get_api_key_for_test, name, animal_type, age):
        """
        Tests if it's possible to add new pet with valid data:
        :param name: pet's name
        :param animal_type: pet's type
        :param age: pet's age
        :return: 1) status check result
                2) new pet's name check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert result.status_code == 200
        assert result.json()['name'] == name
        assert result.json()['age'] == age or result.json()['age'] == str(age)
        assert result.json()['animal_type'] == animal_type

        return result

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    @pytest.mark.parametrize("age", [i for i in negative_param_for_age.keys()],
                             ids=[i for i in negative_param_for_age.values()])
    @pytest.mark.parametrize("name", [i for i in negative_param_for_pet_name.keys()],
                             ids=[i for i in negative_param_for_pet_name.values()])
    @pytest.mark.parametrize("animal_type", [i for i in negative_param_for_anim_type.keys()],
                             ids=[i for i in negative_param_for_anim_type.values()])
    def test_negative(self, get_api_key_for_test, name, animal_type, age):
        """
        Tests if it's possible to add new pet with valid data:
        :param name: pet's name
        :param animal_type: pet's type
        :param age: pet's age
        :return: 1) status check result
                2) new pet's name check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert result.status_code == 400

        return result
