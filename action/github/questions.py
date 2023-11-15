# questions.py
from utils import format_documents
from file_processing import search_documents

class QuestionContext:
    def __init__(self, index, documents, llm_chain, model_name, repo_name, github_url, conversation_history, file_type_counts, filenames):
        self.index = index
        self.documents = documents
        self.llm_chain = llm_chain
        self.model_name = model_name
        self.repo_name = repo_name
        self.github_url = github_url
        self.conversation_history = conversation_history
        self.file_type_counts = file_type_counts
        self.filenames = filenames

    def ask_question(self, question):
        relevant_docs = search_documents(question, self.index, self.documents, n_results=5)
    
        numbered_documents = format_documents(relevant_docs)
        question_context = f"This question is about the GitHub repository '{self.repo_name}' available at {self.github_url}. The most relevant documents are:\n\n{numbered_documents}"
    
        answer_with_sources = self.llm_chain.run(
            model=self.model_name,
            question=question,
            context=question_context,
            repo_name=self.repo_name,
            github_url=self.github_url,
            conversation_history=self.conversation_history,
            numbered_documents=numbered_documents,
            file_type_counts=self.file_type_counts,
            filenames=self.filenames
        )
        return answer_with_sources