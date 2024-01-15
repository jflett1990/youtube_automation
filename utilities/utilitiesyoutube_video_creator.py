import requests
import json
from moviepy.editor import ImageSequenceClip, AudioFileClip

class YouTubeVideoCreator:
    def __init__(self, play_ht_api_key, play_ht_user_id):
        self.play_ht_api_key = play_ht_api_key
        self.play_ht_user_id = play_ht_user_id

    def convert_text_to_speech(self, text, voice):
        url = "https://api.play.ht/api/v2/tts"
        payload = json.dumps({
            "voice": voice,
            "content": [text]
        })
        headers = {
            'Authorization': self.play_ht_api_key,
            'X-User-ID': self.play_ht_user_id,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 201:
            return response.json()['data']['url']
        else:
            raise Exception(f"Error in text-to-speech conversion: {response.text}")

    def create_video(self, images, audio_url, duration_per_image, output_file):
        audio = AudioFileClip(audio_url)
        clip = ImageSequenceClip(images, durations=[duration_per_image] * len(images))
        video = clip.set_audio(audio)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
