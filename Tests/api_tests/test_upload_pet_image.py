import pytest
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def choose_image_file():
    root = Tk()
    root.withdraw()  # Hide main Tk window
    file_path = askopenfilename(
        title="Select an image to upload",
        filetypes=[("JPEG Images", "*.jpg *.jpeg"), ("PNG Images", "*.png"), ("All files", "*.*")]
    )
    root.destroy()
    return file_path

def test_upload_pet_image(pet_service, created_pet):
    pet_id = created_pet["id"]

    # Let the user pick an image
    image_path = choose_image_file()
    assert image_path, "No file selected!"

    response = pet_service.upload_image(
        pet_id=pet_id,
        image_path=image_path,
        metadata="profile picture"
    )

    assert response.status_code == 200
    body = response.json()
    assert "message" in body
