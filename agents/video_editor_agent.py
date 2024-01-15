import autogen
from utilities.youtube_video_creator import YouTubeVideoCreator

class ExtendedVideoEditorAgent(autogen.AssistantAgent):
    def __init__(self, name, llm_config, play_ht_api_key, play_ht_user_id):
        super().__init__(name, llm_config)
        self.video_creator = YouTubeVideoCreator(play_ht_api_key, play_ht_user_id)

    # Add custom methods here for the video editor's functionalities
