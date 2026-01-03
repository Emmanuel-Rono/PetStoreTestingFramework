
import requests
class PetService:
    def __init__(self, base_url, headers, timeout):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    def add_pet(self, payload):
        return requests.post(
            url=f"{self.base_url}/pet",
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )
    def get_pet_by_id (self, pet_id):
        return requests.get(
            url=f"{self.base_url}/pet/{pet_id}",
            headers = self.headers,
            timeout = self.timeout
        )

    def update_pet(self, payload):
        return requests.put(
            url=f"{self.base_url}/pet",
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )
#delete pet service
    def delete_pet(self, pet_id):
        return requests.delete(
            url=f"{self.base_url}/pet/{pet_id}",
            headers=self.headers,
            timeout=self.timeout
        )
