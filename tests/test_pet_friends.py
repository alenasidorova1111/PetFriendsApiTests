from api import PetFriends
from settings import v_em, v_pas, w_pas, w_em
import os
import pytest
from tests.conftest import test_log


pf = PetFriends()


class TestGetApiKey:
    @pytest.mark.pos
    @test_log
    def test_get_api_key_for_valid_user(self, email=v_em[0], password=v_pas[0]):
        """
        Tests getting user api key with valid user email and password
        """

        result = pf.get_api_key(email, password)

        assert result.status_code == 200
        assert len(result.json()['key']) == 56

    @pytest.mark.neg
    def test_get_api_key_for_invalid_user(self, email=w_em[0], password=v_pas[0]):
        """
        Tests getting user api key with invalid user email and valid password
        """

        result = pf.get_api_key(email, password)

        assert result.status_code == 403

    @pytest.mark.neg
    def test_get_api_key_for_invalid_password(self, email=v_em[0], password=w_pas[0]):
        """
        Tests getting user api key with valid user email and invalid password
        """

        result = pf.get_api_key(email, password)

        assert result.status_code == 403


class TestGetAllPets:
    @pytest.mark.pos
    def test_get_all_pets_with_valid_key(self, get_api_key_for_test, filter_=''):
        """
        Tests getting list of all pets with valid api key
        """

        result = pf.get_list_of_pets(get_api_key_for_test, filter_)

        assert result.status_code == 200
        assert len(result.json()['pets']) > 0

    @pytest.mark.neg
    def test_get_all_pets_with_invalid_key(self, filter_=''):
        """
        Tests getting list of all pets with invalid api key
        """

        auth_key = "ea7384646464646148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729"
        result = pf.get_list_of_pets(auth_key, filter_)

        assert result.status_code == 403


class TestCreatePetSimple:
    def test_create_pet_simple_with_valid_data(self, get_api_key_for_test, name, animal_type, age):
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

        return result

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_create_pet_simple_with_invalid_name(self, get_api_key_for_test, name=6789, animal_type='Monster', age='2'):
        """
        Tests if it's possible to add new pet with data:
        invalid: param name: pet's name
        valid :param animal_type: pet's type
        valid :param age: pet's age
        :return: status check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert result.status_code == 400

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_create_pet_simple_with_invalid_name_2(self, get_api_key_for_test, name="6789", animal_type='Monster',
                                                   age='2'):
        """
        Tests if it's possible to add new pet with data:
        invalid: param name: pet's name
        valid :param animal_type: pet's type
        valid :param age: pet's age
        :return: status check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert result.status_code == 400

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_create_pet_simple_with_invalid_type(self, get_api_key_for_test, name='Creature1', animal_type=1516,
                                                 age='2'):
        """
        Tests if it's possible to add new pet with data:
        valid : param name: pet's name
        invalid: param animal_type: pet's type
        valid : param age: pet's age
        :return: status check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert result.status_code == 400

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_create_pet_simple_with_invalid_type_2(self, get_api_key_for_test, name='Creature1', animal_type='1516',
                                                   age='2'):
        """
        Tests if it's possible to add new pet with data:
        valid : param name: pet's name
        invalid: param animal_type: pet's type
        valid : param age: pet's age
        :return: status check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert result.status_code == 400

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_create_pet_simple_with_invalid_age_type(self, get_api_key_for_test, name='Creature1',
                                                     animal_type='Monster', age=5):
        """
        Tests if it's possible to add new pet with data:
        valid :param name: pet's name
        valid :param animal_type: pet's type
        invalid: param age: pet's age
        :return: status check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert result.status_code == 400

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_create_pet_simple_with_invalid_age_value(self, get_api_key_for_test, name='Creature1',
                                                      animal_type='Monster', age='159'):
        """
        Tests if it's possible to add new pet with valid data:
        valid :param name: pet's name
        valid :param animal_type: pet's type
        invalid :param age: pet's age
        :return: status check result
        """

        result = pf.create_pet_simple(get_api_key_for_test, name, animal_type, age)

        assert float(result.json()['age']) < 30.0
        assert result.status_code == 400


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


class TestAddNewPet:
    @pytest.mark.pos
    def test_add_new_pet_with_valid_data(self, get_api_key_for_test, name='Фунтик1', animal_type='Siam cat',
                                         age='5', pet_photo='images/cat.jpg'):
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

    @pytest.mark.neg
    def test_add_new_pet_with_invalid_api_key(self, name='Фунтик1', animal_type='Siam cat',
                                              age='5', pet_photo='images/cat.jpg'):
        """
        Tests if it's possible to add new pet with invalid api key
        """

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        auth_key = "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0aewedwd729"
        result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

        assert result.status_code == 403

    @pytest.mark.xfail(raises=AssertionError)
    @pytest.mark.neg
    def test_add_new_pet_with_invalid_name(self, get_api_key_for_test, name='24794', animal_type='Siam cat',
                                           age='5', pet_photo='images/cat.jpg'):
        """
        Tests if it's possible to add new pet with invalid pet's name value
        """

        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        result = pf.add_new_pet(get_api_key_for_test, name, animal_type, age, pet_photo)

        assert result.status_code == 400

    @pytest.mark.neg
    def test_add_new_pet_with_invalid_amount_of_params(self, get_api_key_for_test, name='Фунтик1',
                                                       animal_type='Siam cat', age='7'):
        """
        Tests if it's possible to add new pet with invalid amount of parameters (no pet_photo)
        """

        try:
            pf.add_new_pet(get_api_key_for_test, name, animal_type, age)
        except Exception as e:
            assert e.__class__.__name__ == 'TypeError'


class TestDeleteOwnPet:
    @pytest.mark.pos
    def test_delete_own_pet_with_valid_data(self, get_api_key_for_test):
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

    @pytest.mark.skip(reason="Test is not ready yet")
    @pytest.mark.neg
    def test_delete_own_pet_with_invalid_pet_id(self, get_api_key_for_test):
        """
        Tests if it's possible to delete own pet with invalid pet_id
        """

        result = pf.get_list_of_pets(get_api_key_for_test, "my_pets")

        if len(result.json()['pets']) > 0:
            pet_id = "f1b2c449-a41b-43fe-a9f7-edwefbwefd5493e9dd911"
            result = pf.delete_pet(get_api_key_for_test, pet_id)

            assert result.status_code == 400

        else:
            raise Exception("There is no my pets")


class TestUpdateOwnPet:
    @pytest.mark.pos
    def test_update_own_pet_with_valid_data(self, get_api_key_for_test, name='Фунтик2', animal_type='Siam catt',
                                            age=4):
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
