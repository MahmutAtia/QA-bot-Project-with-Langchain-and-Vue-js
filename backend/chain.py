
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from store import get_store




model_name = "gpt-3.5-turbo"

def get_chain( prompt_template):
    store = get_store()
    retriever = store.as_retriever()
    llm = ChatOpenAI(model_name=model_name) 


    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=retriever,
                                       return_source_documents=True,
                                       chain_type_kwargs={"prompt": prompt_template}

                                       )
    
    return qa_chain

