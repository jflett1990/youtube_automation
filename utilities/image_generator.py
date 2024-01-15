import requests
import uuid
from pathlib import Path

class ImageGenerator:
    def __init__(self, openai_key):
        self.openai_key = openai_key
        self.dalle_api_url = "https://api.openai.com/v1/images/generations"

    def generate_and_save_images(self, prompt: str, image_size: str = "1024x1024", n: int = 1):
        headers = {
            'Authorization': f'Bearer {self.openai_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': 'dall-e-3',
            'prompt': prompt,
            'n': n,
            'size': image_size
        }

        response = requests.post(self.dalle_api_url, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Failed to generate images: {response.text}")

        image_data = response.json()

        saved_files = []
        for img_info in image_data.get('data', []):
            img_url = img_info.get('url')
            if img_url:
                file_name = str(uuid.uuid4()) + ".png"
                file_path = Path('images/') / file_name
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(file_path, "wb") as img_file:
                        img_file.write(img_response.content)
                        saved_files.append(str(file_path))
                else:
                    print(f"Failed to download the image from {img_url}")

        return saved_files

        # Example usage
        if __name__ == "__main__":
    openai_key = "OpenAI_API_KEY"  # Replace with your actual API key
    image_generator = ImageGenerator(openai_key)

    # Generate and save images
    images = image_generator.generate_and_save_images("A cute baby sea otter")
    for image in images:
        print(f"Saved image: {image}")

