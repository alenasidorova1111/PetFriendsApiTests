from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """
    Tests getting user api key with valid user email and password
    """

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    """
    Tests getting user api key with invalid user email and valid password
    """

    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    """
    Tests getting user api key with valid user email and invalid password
    """

    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_get_all_pets_with_valid_key(filter=''):
    """
    Tests getting list of all pets with valid api key
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_get_all_pets_with_invalid_key(filter=''):
    """
    Tests getting list of all pets with invalid api key
    """

    auth_key = {"key": "ea7384646464646148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729"}
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403


def test_create_pet_simple_with_valid_data(name='Creature1', animal_type='Monster', age='2'):
    """
    Tests if it's possible to add new pet with valid data:
    :param name: pet's name
    :param animal_type: pet's type
    :param age: pet's age
    :return: 1) status check result
            2) new pet's name check result
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


def test_create_pet_simple_with_invalid_name(name=6789, animal_type='Monster', age='2'):
    """
    Tests if it's possible to add new pet with data:
    invalid: param name: pet's name
    valid :param animal_type: pet's type
    valid :param age: pet's age
    :return: status check result
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 400


def test_create_pet_simple_with_invalid_name_2(name="6789", animal_type='Monster', age='2'):
    """
    Tests if it's possible to add new pet with data:
    invalid: param name: pet's name
    valid :param animal_type: pet's type
    valid :param age: pet's age
    :return: status check result
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 400


def test_create_pet_simple_with_invalid_type(name='Creature1', animal_type=1516, age='2'):
    """
    Tests if it's possible to add new pet with data:
    valid : param name: pet's name
    invalid: param animal_type: pet's type
    valid : param age: pet's age
    :return: status check result
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 400


def test_create_pet_simple_with_invalid_type_2(name='Creature1', animal_type='1516', age='2'):
    """
    Tests if it's possible to add new pet with data:
    valid : param name: pet's name
    invalid: param animal_type: pet's type
    valid : param age: pet's age
    :return: status check result
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 400


def test_create_pet_simple_with_invalid_age_type(name='Creature1', animal_type='Monster', age=5):
    """
    Tests if it's possible to add new pet with data:
    valid :param name: pet's name
    valid :param animal_type: pet's type
    invalid: param age: pet's age
    :return: status check result
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert status == 400


def test_create_pet_simple_with_invalid_age_value(name='Creature1', animal_type='Monster', age='159'):
    """
    Tests if it's possible to add new pet with valid data:
    valid :param name: pet's name
    valid :param animal_type: pet's type
    invalid :param age: pet's age
    :return: status check result
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

    assert float(result['age']) < 30.0
    assert status == 400


def test_set_pet_photo_with_valid_data(pet_photo='images/cat.jpg'):
    """
    Tests if it's possible to set pet's photo with valid data:
    :param pet_photo: 'images/cat.jpg'
    :return: status check result
    """

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.create_pet_simple(auth_key, "Суперкот", "кот", "3")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.set_pet_photo(auth_key, pet_id, pet_photo)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200


def test_add_new_pet_with_valid_data(name='Фунтик1', animal_type='Siam cat',
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
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_api_key(name='Фунтик1', animal_type='Siam cat',
                                          age='5', pet_photo='images/cat.jpg'):
    """
    Tests if it's possible to add new pet with invalid api key
    """

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    auth_key = {"key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e877b0aewedwd729"}
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 403


def test_add_new_pet_with_invalid_name(name='24794', animal_type='Siam cat',
                                       age='5', pet_photo='images/cat.jpg'):
    """
    Tests if it's possible to add new pet with invalid pet's name value
    """

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400


def test_add_new_pet_with_invalid_params(name='Фунтик1', animal_type='Siam cat',
                                         age='7'):
    """
    Tests if it's possible to add new pet with invalid amount of parameters (no pet_photo)
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    try:
        pf.add_new_pet(auth_key, name, animal_type, age)
    except Exception as e:
        assert e.__class__.__name__ == 'TypeError'


def test_delete_own_pet_with_valid_data():
    """
    Tests if it's possible to delete own pet with valid data
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.delete_pet(auth_key, pet_id)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200
        assert pet_id not in my_pets.values()
    else:
        raise Exception("There is no my pets")


def test_delete_own_pet_with_invalid_pet_id():
    """
    Tests if it's possible to delete own pet with invalid pet_id
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        pet_id = "f1b2c449-a41b-43fe-a9f7-edwefbwefd5493e9dd911"
        status, _ = pf.delete_pet(auth_key, pet_id)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        assert pet_id not in my_pets.values()
        assert status == 400


def test_update_self_pet_with_valid_data(name='Фунтик2', animal_type='Siam catt',
                                         age=4):
    """
    Tests if it's possible to update own pet's info with valid data
    """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Фунтик1", "Siam cat", "5", "images/cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_pet(auth_key, pet_id, name, animal_type, age)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert result['name'] == name
    assert status == 200
