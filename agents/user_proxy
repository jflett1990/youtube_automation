# Define the UserProxyAgent for your input
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin providing topics and feedback.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="TERMINATE"
)
