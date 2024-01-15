# video_editor_agent.py
import autogen
from utilities.youtube_video_creator import YouTubeVideoCreator

class VideoEditorAgent(autogen.AssistantAgent):
    def __init__(self, name, llm_config, play_ht_api_key, play_ht_user_id):
        super().__init__(name, llm_config, system_message="Responsible for video editing and production, turning scripts and ideas into engaging video content.")
        self.video_creator = YouTubeVideoCreator(play_ht_api_key, play_ht_user_id)
        # Additional methods for the Video Editor Agent
