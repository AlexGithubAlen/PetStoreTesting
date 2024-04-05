import unittest
import requests

# Alex-Alen Pugatsov (TA-21V)

class PetStoreAPITests(unittest.TestCase):
    base_url = "https://petstore.swagger.io/v2"
    
    def test_find_pets_by_status(self):
        statuses = ["available", "pending", "sold"]
        for status in statuses:
            response = requests.get(f"{self.base_url}/pet/findByStatus?status={status}")
            self.assertEqual(response.status_code, 200)
            pets = response.json()
            self.assertTrue(isinstance(pets, list))
            if pets:
                for pet in pets:
                    self.assertEqual(pet["status"], status)

    def test_get_pet_by_id(self):
        pet_id = 1
        response = requests.get(f"{self.base_url}/pet/{pet_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], pet_id)

    def test_get_non_existing_pet(self):
        invalid_pet_id = 42323452353
        response = requests.get(f"{self.base_url}/pet/{invalid_pet_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["message"], "Pet not found")

    def test_update_pet(self):
        pet = {
            "id": 1,
            "category": {"id": 1, "name": "Dogs"},
            "name": "Alex",
            "photoUrls": ["https://lol.com/", "https://kek.com/"],
            "tags": [{"id": 1, "name": "tag1"}],
            "status": "available"
        }
        response = requests.put(f"{self.base_url}/pet", json=pet)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Alex")
        self.assertEqual(response.json()["status"], "available")

    def test_update_pet_with_invalid_data(self):
        invalid_pet = {"id": "a", "name": ""}
        response = requests.put(f"{self.base_url}/pet", json=invalid_pet)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json()["message"], "something bad happened")

    def test_find_pets_by_invalid_status(self):
        rare_status = "available,not-a-real-status"
        response = requests.get(f"{self.base_url}/pet/findByStatus?status={rare_status}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_delete_non_existing_pet(self):
        non_existing_pet_id = 56356421
        response = requests.delete(f"{self.base_url}/pet/{non_existing_pet_id}")
        self.assertEqual(response.status_code, 404)

    def test_create_order(self):
        order = {
            "petId": 1,
            "quantity": 1,
            "shipDate": "2023-04-08T12:34:56.789Z",
            "status": "placed",
            "complete": True
        }
        response = requests.post(f"{self.base_url}/store/order", json=order)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["petId"], order["petId"])
        self.assertEqual(response.json()["quantity"], order["quantity"])
        self.assertEqual(response.json()["status"], order["status"])

    def test_create_order_with_invalid_data(self):
        invalid_order = {"petId": "!!!", "quantity": -7, "status": "unknown"}
        response = requests.post(f"{self.base_url}/store/order", json=invalid_order)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json()["message"], "something bad happened")


if __name__ == '__main__':
    unittest.main()
