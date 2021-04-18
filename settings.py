v_em = ("lalala@mail.ru", 'valid_email')
v_pas = ("12345", 'valid_password')
w_em = ("lalala1111@mail.ru", 'wrong_email')
w_pas = ("123456", 'wrong_password')
sym = ("|!@#$%^&*()-_=+`~?№;:[]{}", 'special symbols - ' + str(len('|!@#$%^&*()-_=+`~?№;:[]{}')) + ' symbols')
numb = (5, 'int number (5)')
big_num = (100, 'int number (100)')
v_big_num = (2147483648, 'wong int number (2147483648)')
zer_num = (0, 'zero')
neg_num = (-1, 'negative number(-1)')
min_num = (1, 'minimum number(1)')
float_num = (1.5, 'float number(1.5)')
eng_str_1 = ('f' * 256, 'string of 256 english letters')
eng_str_2 = ('h' * 15, 'string of 15 english letters')
eng_str_3 = ('f' * 1001, 'string of 1001 english letters')
rus_str_1 = ('ф' * 256, 'string of 256 russian letters')
rus_str_2 = ('п' * 15, 'string of 15 russian letters')
chin_str_1 = ('在' * 256, 'string of 256 chinese letters')
chin_str_2 = ('在' * 15, 'string of 15 chinese letters')
emp_str = ('', 'empty string')
w_sp_str = ('   ', 'string with 3 whitespaces')
my_pets_filter = ('my_pets', 'filter: string "my_pets"')
v_key = ("5443d6fd57e7a9be02debe78c2b41055e0e74c093afbef6d22d32685", "valid auth key")
w_key = ("ea7384646464646148a1f19838e1c5d1413877f3691a3731380e733e877b0ae729", "not existing auth key")
w_pet_id = "e01e8042-9e03-4bf3-be97-54796c87bec4"

positive_param_for_filter = dict((x, y) for x, y in (emp_str, my_pets_filter))
negative_param_for_filter = dict((x, y) for x, y in (numb, eng_str_2, w_sp_str))

positive_param_for_age = dict((x, y) for x, y in (numb, min_num, float_num))
negative_param_for_age = dict((x, y) for x, y in (big_num, v_big_num, zer_num,
                                                  neg_num, eng_str_2, emp_str,
                                                  sym, rus_str_2, chin_str_2,
                                                  w_sp_str))

positive_param_for_pet_name = dict((x, y) for x, y in (eng_str_2, rus_str_2, chin_str_2))
negative_param_for_pet_name = dict((x, y) for x, y in (sym, numb, eng_str_1,
                                                       eng_str_3, emp_str, w_sp_str))

positive_param_for_anim_type = dict((x, y) for x, y in (eng_str_2, rus_str_2, chin_str_2))
negative_param_for_anim_type = dict((x, y) for x, y in (sym, numb, eng_str_1,
                                                        eng_str_3, emp_str, w_sp_str))

all_params_for_mail = dict((x, y) for x, y in (v_em, w_em))
all_params_for_pass = dict((x, y) for x, y in (v_pas, w_pas))



