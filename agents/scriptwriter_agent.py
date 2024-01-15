import autogen
from utilities.local_content_manager import LocalContentManager

class ExtendedScriptwriterAgent(autogen.AssistantAgent):
    def __init__(self, name, llm_config):
        super().__init__(name, llm_config)
        self.content_manager = LocalContentManager()

    # Add custom methods here for the scriptwriter's functionalities
