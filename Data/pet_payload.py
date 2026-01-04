import random


def pet_payload_factory(
    pet_id=None,
    name="doggie",
    status="available"
):
    return {
        "id": pet_id or random.randint(100000, 999999),
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": name,
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": status
    }
