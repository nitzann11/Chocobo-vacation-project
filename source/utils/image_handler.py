from pathlib import Path
from flask import current_app
from uuid import uuid4


class ImageHandler:
    @staticmethod
    def save_image(image):
        """ method to save image"""
        if not image : return None
        suffix = Path(image.filename).suffix
        image_name = str(uuid4())+suffix
        image_path = Path(current_app.root_path) / "static/images" / image_name
        image.save(image_path)
        return image_name

    @staticmethod
    def get_image_path(image_name : str):
        """method to get image path"""
        image_path = Path(current_app.root_path) / "static/images" / image_name
        if not image_path.exists():
            image_path = Path(current_app.root_path) / "static/images/no_image.png"
        return image_path

    @staticmethod
    def update_image(old_image_name : str, image):
        """ function to update image"""
        if not image.filename : return old_image_name
        image_name = ImageHandler.save_image(image)
        ImageHandler.delete_image(old_image_name)
        return image_name
    
    @staticmethod
    def delete_image(image_name : str) :
        """method to delete image"""
        if not image_name : return
        if image_name == "no_image.png":
            return
        image_path = Path(current_app.root_path) / "static/images" / image_name
        image_path.unlink(missing_ok = True)


