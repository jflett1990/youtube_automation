# video_editor_agent.py
import autogen
from utilities.youtube_video_creator import YouTubeVideoCreator

class VideoEditorAgent(autogen.AssistantAgent):
    def __init__(self, name, llm_config, play_ht_api_key, play_ht_user_id):
        super().__init__(name, llm_config, system_message="Responsible for video editing and production, turning scripts and ideas into engaging video content.")
        self.video_creator = YouTubeVideoCreator(play_ht_api_key, play_ht_user_id)
        # Additional methods for the Video Editor Agent
    # Example method: Create a video from a script
    def create_video(self, script):
        # Generate images for the script
        images = generate_and_save_images(script)
        # Create a video with these images
        audio_url = self.video_creator.convert_text_to_speech(script, "en-US-MichelleNeural")
        output_file = "output_video.mp4"
        self.video_creator.create_video(images, audio_url, 5, output_file)
        return output_file
