from google import genai
from google.genai import types
from fields.hardcoded_fields import base_fields
from model.prompt import Prompt

class GeminiApiModel:
    def __init__(self, API_KEY: str, image_path: str):
        self.API_KEY = API_KEY
        self.IMAGE_PATH = image_path
    
    def _initialize_client(self):
        client = genai.Client(api_key=self.API_KEY)
        return client
    
    def _read_image(self) -> bytes:
        with open(self.IMAGE_PATH, 'rb') as f:
            image_bytes = f.read()
        return image_bytes
    
    def process_ID_image(self):

        from fields.hardcoded_fields import base_fields

        schema = base_fields.model_json_schema()
        
        client = self._initialize_client()
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(
                    data=self._read_image(),
                    mime_type='image/png',
            ),
            Prompt.prompt
            ],
            config={
                "response_mime_type": "application/json",
                "response_schema": schema,
            },
        )

        return response.parsed