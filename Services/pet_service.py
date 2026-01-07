
import requests
class PetService:
    def __init__(self, base_url, headers=None,timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session= requests.Session()
        if headers:
            self.session.headers.update(headers)

    def add_pet(self, payload):
        return self.session.post(
            url=f"{self.base_url}/pet",
            json=payload,
            timeout=self.timeout
        )
    def get_pet_by_id (self, pet_id):
        return self.session.get(
            url=f"{self.base_url}/pet/{pet_id}",
            timeout = self.timeout
        )

    def delete_pet(self, pet_id: int):
        """
        Delete a pet by ID using DELETE /pet/{petId}
        """
        url = f"{self.base_url}/pet/{pet_id}"
        response = self.session.delete(
            url,
            timeout=self.timeout
        )
        return response


    # update_pet service
    def update_pet(self, payload):
            return self.session.put(
                url=f"{self.base_url}/pet",
                json=payload,
                timeout=self.timeout
                )
