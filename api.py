import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/'

    def get_api_key(self, email: str, password: str) -> json:
        """
        Method makes a get request to API server with parameters:
        :param email: user's email
        :param password: user's password
        :return: 1) status code of request
                 2) json file result with unique authorization user's api key
        """

        headers = {
            'email': email,
            'password': password,
        }

        result = requests.get(self.base_url + 'api/key', headers=headers)
        # status = res.status_code
        # result = ""

        # try:
        #    result = res.json()
        # except json.decoder.JSONDecodeError:
        #    result = res.text
        # return status, result
        return result

    def get_list_of_pets(self, auth_key: str, filter_: str = '') -> json:
        """
        Method makes a get request to API server with parameters:
        :param auth_key: user's api key
        :param filter_: 1) empty filter_ returns list and info about all pets
                       2) filter_ "my_pets" returns list and info about user's pets
        :return: 1) status code of request
                 2) json file result with list and info about all pets
        """

        filter_ = {'filter': filter_}
        headers = {'auth_key': auth_key}

        result = requests.get(self.base_url + 'api/pets', headers=headers, params=filter_)
        # status = res.status_code
        # result = ""

        # try:
        #    result = res.json()
        # except json.decoder.JSONDecodeError:
        #    result = res.text
        # return status, result
        return result

    def create_pet_simple(self, auth_key: str, name: str, animal_type: str, age=str) -> json:
        """
        Method makes a post request to API server with parameters:
        :param auth_key: user's api key
        :param name: new pet's name
        :param animal_type: new pet's animal type
        :param age: new pet's age
        :return: 1) status code of request
                2) json file result with info about created pet
        """

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key}

        result = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)

        return result

    def set_pet_photo(self, auth_key: str, pet_id: str, pet_photo: str) -> json:
        """
        Method makes a post request to API server with parameters:
        :param auth_key: user's api key
        :param pet_id: unique pet's id
        :param pet_photo: pet's photo
        :return: 1) status code of request
                 2) json file result with info about pet, which photo was set
        """

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key, 'Content-Type': data.content_type}

        result = requests.post(self.base_url + 'api/pets/set_photo' + pet_id, headers=headers, data=data)

        return result

    def add_new_pet(self, auth_key: str, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        """
        Method makes a post request to API server with parameters:
        :param auth_key: user's api key
        :param name: name of new pet
        :param animal_type: animal type of new pet
        :param age: new pet's age
        :param pet_photo: new pet's photo
        :return: 1) status code of request
                 2) json file result with info about created pet
        """

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key, 'Content-Type': data.content_type}

        result = requests.post(self.base_url + 'api/pets', headers=headers, data=data)

        return result

    def delete_pet(self, auth_key: str, pet_id: str):
        """
        Method makes a delete request to API server with parameters:
        :param auth_key: user's api key
        :param pet_id: unique pet's id
        :return: status code of request
        """
        headers = {'auth_key': auth_key}

        result = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)

        return result

    def update_pet(self, auth_key: str, pet_id: str, name: str, animal_type: str, age: str) -> json:
        """
        Method makes a put request to API server with parameters:
        :param auth_key: user's api key
        :param pet_id: unique id of a pet, whose parameters need to be changed
        :param name: new name of a pet, whose parameters need to be changed
        :param animal_type: new animal type of a pet, whose parameters need to be changed
        :param age: new age of a pet, whose parameters need to be changed
        :return: 1) status code of request
                 2) json file result with info about changed pet
        """

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key}

        result = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)

        return result
