import autogen
import yfinance as yf

def get_stock_price(ticker):
    data = yf.Ticker(ticker).history(period="1mo").iloc[-1].Close
    return str(data)

def get_config_list(env_or_file="OAI_CONFIG_LIST"):
    # Setting configurations for autogen
    config_list = autogen.config_list_from_json(
        env_or_file=env_or_file,
        file_location=".",
        filter_dict={
            "model": {
                "gpt-4",
                "gpt4",
                "gpt-4-32k",
                "gpt-4-32k-0314",
                "gpt-4-32k-v0314",
                "gpt-3.5-turbo",
                "gpt-3.5-turbo-16k",
                "gpt-3.5-turbo-0301",
                "gpt-3.5-turbo-0613i",
                "chatgpt-35-turbo-0301",
                "gpt-35-turbo-v0301",
                "gpt",
            }
        }
    )
    return config_list

if __name__ == "__main__":
    config_list = get_config_list()
    print(config_list)
    prices = get_stock_price("AAPL")
    print(prices)