import os
import json

class LocalContentManager:
    def __init__(self):
        self.base_path = 'agent_content'
        self.ensure_base_path()

    def ensure_base_path(self):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

    def save_content(self, content_type, file_name, content):
        path = os.path.join(self.base_path, content_type, file_name)
        with open(path, 'w') as file:
            if content_type =='articles' or content_type == 'scripts':
file.write(content)
else:
file.write(json.dumps(content))

def get_content(self, content_type, file_name):
    path = os.path.join(self.base_path, content_type, file_name)
    with open(path, 'r') as file:
        if content_type == 'articles' or content_type == 'scripts':
            return file.read()
        else:
            return json.loads(file.read())
