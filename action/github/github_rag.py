# github_reader.py
import os
import tempfile
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from config import Config
from utils import format_user_question
from file_processing import clone_github_repo, load_and_index_files
from questions import QuestionContext
from templates import template

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    config = Config()
    github_url = input("Enter the GitHub URL of the repository: ")
    repo_name = github_url.split("/")[-1]
    print("Cloning the repository...")
    with tempfile.TemporaryDirectory() as local_path:
        if clone_github_repo(github_url, local_path):
            index, documents, file_type_counts, filenames = load_and_index_files(local_path)
            if index is None:
                print("No documents were found to index. Exiting.")
                exit()
            else:
                print(f"Found {len(documents)} documents to index.")

            print("Repository cloned. Indexing files...")
            llm = OpenAI(api_key=OPENAI_API_KEY, temperature=0.2)

            prompt = PromptTemplate(
                template=template,
                input_variables=["repo_name", "github_url", "conversation_history", "question", "numbered_documents", "file_type_counts", "filenames"]
            )

            llm_chain = LLMChain(prompt=prompt, llm=llm)

            conversation_history = ""
            question_context = QuestionContext(index, documents, llm_chain, config.MODEL, repo_name, github_url, conversation_history, file_type_counts, filenames)
            while True:
                try:
                    user_question = input("\n" + config.WHITE + "Ask a question about the repository (type 'exit()' to quit): " + config.RESET_COLOR)
                    if user_question.lower() == "exit()":
                        break
                    print('Thinking...')
                    user_question = format_user_question(user_question)
                    answer = question_context.ask_question(user_question)
                    print(config.GREEN + '\nANSWER\n' + answer + config.RESET_COLOR + '\n')
                    conversation_history += f"Question: {user_question}\nAnswer: {answer}\n"
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

        else:
            raise Exception("Failed to clone repository.")

if __name__ == '__main__':
    main()