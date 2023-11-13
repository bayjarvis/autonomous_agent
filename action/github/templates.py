template = """
Repo: {repo_name} URL: ({github_url}) | Conversation: {conversation_history} | Docs: {numbered_documents} | Q: {question} | FileCount: {file_type_counts} | FileNames: {filenames}

Instructions:
1. Answer truthfully based on context/docs.
2. Focus on repo/code.
3. Be specific:
   a. Purpose/features - describe.
   b. Functions/code - provide details/samples.
   c. Setup/usage - give instructions.
4. Say "I am not sure" if you are not sure.

Answer:
"""