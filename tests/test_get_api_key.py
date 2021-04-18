from api import PetFriends
from settings import all_params_for_mail, all_params_for_pass, v_em, v_pas
import pytest

pf = PetFriends()


class TestGetApiKey:
    @pytest.mark.parametrize("email", [i for i in all_params_for_mail.keys()],
                             ids=[i for i in all_params_for_mail.values()])
    @pytest.mark.parametrize("password", [i for i in all_params_for_pass.keys()],
                             ids=[i for i in all_params_for_pass.values()])
    def test_get_api_key(self, email, password):
        """
        Tests getting user api key with invalid user email and valid password
        """

        result = pf.get_api_key(email, password)

        if email == v_em[0] and password == v_pas[0]:
            assert result.status_code == 200
        else:
            assert result.status_code == 403
