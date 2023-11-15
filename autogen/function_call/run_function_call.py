from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from utils import get_stock_price

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST") 

custom_function_list = [
            {
                "name": "get_stock_price",
                "description": "Get the ticker of a stock and returns the latest closing price",
                "parameters":{
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "The ticker symbol of the stock",
                        },
                    },
                    "required": ["ticker"],
                },
            }
        ]

assistant = AssistantAgent(
    "assistant",
    system_message="You are a stock trader.",
    llm_config={
        "model": "gpt-3.5-turbo-0613",
        #"config_list": config_list,
        "timeout": 60,
        "functions": custom_function_list
    }
)


user_proxy = UserProxyAgent(
    "user_proxy",
    code_execution_config={"work_dir": "coding"},
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="ALWAYS",
    function_map={"get_stock_price": get_stock_price}
)

user_proxy.initiate_chat(assistant, message="What is the latest price of Apple")