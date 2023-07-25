from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):
    def test_email_properties(self):
        expected = 127
        result = User._meta.get_field("email").max_length
        msg = f"Verifique se a propriedade `max_length` de `email` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("email").unique
        msg = f"Verifique se o atributo `email` foi definido como unico"
        self.assertTrue(result, msg)

        result = User._meta.get_field("email").null
        msg = f"Verifique se o atributo `email` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_first_name_properties(self):
        expected = 50
        result = User._meta.get_field("first_name").max_length
        msg = f"Verifique se a propriedade `max_length` de `first_name` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("first_name").null
        msg = f"Verifique se o atributo `first_name` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_last_name_properties(self):
        expected = 50
        result = User._meta.get_field("last_name").max_length
        msg = f"Verifique se a propriedade `max_length` de `last_name` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("last_name").null
        msg = f"Verifique se o atributo `last_name` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_birthdate_properties(self):
        result = User._meta.get_field("birthdate").null
        msg = f"Verifique se o atributo `birthdate` foi definido como opcional"
        self.assertTrue(result, msg)

    def test_is_employee_properties(self):
        result = User._meta.get_field("is_employee").default
        msg = f"Verifique se o valor padrão de `is_employee` foi definido como `False`"
        self.assertFalse(result, msg)
