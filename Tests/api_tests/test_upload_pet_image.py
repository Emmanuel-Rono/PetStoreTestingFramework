import pytest
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def choose_image_file():
    """Open a file picker dialog and return the selected file path."""
    root = Tk()
    root.withdraw()  # hide the main Tk window
    file_path = askopenfilename(
        title="Select an image to upload",
        filetypes=[("JPEG Images", "*.jpg *.jpeg"), ("PNG Images", "*.png")]
    )
    root.destroy()
    return file_path


def test_upload_pet_image(pet_service, created_pet):
    pet_id = created_pet["id"]

    # Let the user pick an image interactively
    image_path = choose_image_file()
    assert image_path, "No file selected!"

    response = pet_service.upload_image(
        pet_id=pet_id,
        image_path=image_path,
        metadata="profile picture"
    )

    # Check response
    assert response.status_code == 200, f"Upload failed: {response.status_code} - {response.text}"
    body = response.json()
    assert "message" in body
    print("Upload successful:", body["message"])
