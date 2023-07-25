from django.test import TestCase
from movies.models import MovieOrder


class MovieOrderModelTest(TestCase):
    def test_buyed_at_properties(self):
        result = MovieOrder._meta.get_field("buyed_at").auto_now_add
        msg = f"Verifique se a propriedade `auto_now_add` de `buyed_at` foi definida"
        self.assertTrue(result, msg)

    def test_price_properties(self):
        expected = 8
        result = MovieOrder._meta.get_field("price").max_digits
        msg = f"Verifique se a propriedade `max_digits` de `price` foi definida corretamente"
        self.assertEqual(expected, result, msg)

        expected = 2
        result = MovieOrder._meta.get_field("price").decimal_places
        msg = f"Verifique se a propriedade `decimal_places` de `price` foi definida corretamente"
        self.assertEqual(expected, result, msg)
