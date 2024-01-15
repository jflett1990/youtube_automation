import autogen
from agents.researcher_agent import ExtendedResearcherAgent
from agents.scriptwriter_agent import ExtendedScriptwriterAgent
from agents.video_editor_agent import ExtendedVideoEditorAgent
from utilities.local_content_manager import LocalContentManager
from utilities.youtube_video_creator import YouTubeVideoCreator

# Configure the LLM for all agents
llm_config = {"config_list": config_list_gpt4, "cache_seed": 42}

# Define the UserProxyAgent for user input
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin providing topics and feedback.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="TERMINATE"
)

researcher = ExtendedResearcherAgent("Researcher", llm_config)
scriptwriter = ExtendedScriptwriterAgent("Scriptwriter", llm_config)
video_editor = VideoEditorAgent("Video_Editor", llm_config, "play_ht_api_key", "play_ht_user_id")
expert_youtuber = ExpertYoutuberAgent("Expert_Youtuber", llm_config)
quality_control = QualityControlAgent("Quality_Control", llm_config)

agents = [user_proxy, expert_youtuber, researcher, scriptwriter, video_editor, quality_control]
groupchat = autogen.GroupChat(agents=agents, messages=[], max_round=12)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

if name == "main":
# Example script generation process
script_gen = YouTubeScriptGenerator()
script_gen.add_script_part("Introduction: Discussing the latest in AI technology.")
script_gen.add_script_part("Body: Detailed exploration of GPT-4 capabilities.")
script_gen.add_script_part("Conclusion: The future of AI and its implications.")
complete_script = script_gen.generate_script()
print(complete_script)




# Define the Expert Youtuber Agent (example initialization)
expert_youtuber = autogen.AssistantAgent(
    name="Expert_Youtuber",
    system_message="Specialized in YouTube content creation and management.",
    llm_config=llm_config
)

# Instantiate the custom agents
researcher = ExtendedResearcherAgent("Researcher", llm_config)
scriptwriter = ExtendedScriptwriterAgent("Scriptwriter", llm_config)
video_editor = ExtendedVideoEditorAgent(
    "Video_Editor", llm_config, "d9376dda21724639bb7d1b4096f22ae5", "4JUdPRe2mSPa37h1UJqp8AzEXuU2"
)

# Define the Quality Control Agent (example initialization)
quality_control = autogen.AssistantAgent(
    name="Quality_Control",
    system_message="Ensures the final video meets all quality standards.",
    llm_config=llm_config
)

# Set up the GroupChat for collaboration
agents = [user_proxy, expert_youtuber, researcher, scriptwriter, video_editor, quality_control]
groupchat = autogen.GroupChat(agents=agents, messages=[], max_round=12)

# Define the GroupChat Manager
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

if __name__ == "__main__":
    # Code to run the AutoGen system
    # This can be further elaborated based on how you want to interact with the system
