from django.test import TestCase
from movies.models import Movie


class MovieModelTest(TestCase):
    def test_title_properties(self):
        expected = 127
        result = Movie._meta.get_field("title").max_length
        msg = f"Verifique se a propriedade `max_length` de `title` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Movie._meta.get_field("title").null
        msg = f"Verifique se o atributo `title` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_duration_properties(self):
        expected = 10
        result = Movie._meta.get_field("duration").max_length
        msg = f"Verifique se a propriedade `max_length` de `duration` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Movie._meta.get_field("duration").default
        msg = f"Verifique se o atributo `duration` foi definido com o valor padrão None"
        self.assertIsNone(result, msg)

    def test_rating_properties(self):
        expected = 20
        result = Movie._meta.get_field("rating").max_length
        msg = f"Verifique se a propriedade `max_length` de `rating` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = Movie._meta.get_field("rating").choices
        expected_choices = ["G", "PG", "PG-13", "R", "NC-17"]
        msg = f"Verifique se todos os atributos de `rating` foi definido conforme a lista informada {expected_choices}"
        result_choices = [choice[0] for choice in result]

        for choice in expected_choices:
            self.assertIn(choice, result_choices, msg)

    def test_synopsis_properties(self):
        result = Movie._meta.get_field("synopsis").default
        msg = f"Verifique se o atributo `synopsis` foi definido com o valor padrão None"
        self.assertIsNone(result, msg)
