
import requests
import os
class PetService:
    def __init__(self, base_url, headers=None,timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session= requests.Session()
        if headers:
            self.session.headers.update(headers)

#add_pet service
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

    def find_pet_by_status(self, status:str):
        url= f"{self.base_url}/pet/findByStatus"
        response_of_find_by_status = self.session.get(
            url=url,
            params={'status':status},
            timeout=self.timeout
        )
        return  response_of_find_by_status

    def update_pet_form (self,pet_id:int,name: str= None, status: str= None):
        url = f"{self.base_url}/pet/{pet_id}"
        data = {}
        if name:
            data["name"] = name
        if status:
            data["status"] = status
        response =self.session.post(
            url,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=self.timeout
        )
        return response

    def upload_image(self, pet_id: int, image_path: str, metadata: str = None):
        """
        Upload an image for a pet using /pet/{petId}/uploadImage
        """
        url = f"{self.base_url}/pet/{pet_id}/uploadImage"
        data = {}
        if metadata:
            data["additionalMetadata"] = metadata
        self.session.headers.pop("Content-Type", None)

        # Detect MIME type based on extension
        ext = os.path.splitext(image_path)[1].lower()
        if ext == ".png":
            mime_type = "image/png"
        elif ext in [".jpg", ".jpeg"]:
            mime_type = "image/jpeg"
        else:
            raise ValueError("Unsupported image type. Use PNG or JPEG.")

        # Use `with open` to ensure file is closed safely (Windows-safe)
        with open(image_path, "rb") as f:
            files = {
                "file": (os.path.basename(image_path), f, mime_type)
            }
            response = self.session.post(
                url,
                files=files,
                data=data,
                timeout=self.timeout
            )
        return response





