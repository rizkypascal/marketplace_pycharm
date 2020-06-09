from django.test.testcases import TestCase
from rest_framework import status
from .factories import ProductFactory

class Product (TestCase):

    def test_products(self):
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'product_list.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_create(self):
        response = self.client.post('/products/create', {'link': 'https://www.amazon.com'})
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_product_form(self):
        response = self.client.get('/products/form/')
        self.assertTemplateUsed(response, 'product_form.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail(self):
        product = ProductFactory()
        product.save()
        response = self.client.get('/products/%s/'%(product.id))
        self.assertTemplateUsed(response, 'product_detail.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail_not_found(self):
        response = self.client.get('/products/0/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)