from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage
import retriever
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

def get_response(user_query):
    context = retriever.retrieve_from_pinecone(user_query)[:5]
    print(context)
    st.session_state.context_log = [context]
    
    llm = ChatOllama(model="llama3.2", temperature=0)
    
    template = """
        Answer the question below according to your knowledge in a way that will be helpful to students asking the question.
        The following context is your only source of knowledge to answer from.
        Context: {context}
        User question: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "context": context,
        "user_question": user_query
    })
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("Alemeno Assignment using Langchain, Pinecone, LLama3.2, Streamlit")
if "context_log" not in st.session_state:
    st.session_state.context_log = ["Retrieved context will be displayed here"]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [AIMessage(content="Hi, I'm a PDF assistant. How can I help you?")]
result = st.toggle("Toggle Context")
if result:
    st.write(st.session_state.context_log)


for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)


user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query)
    
    with st.chat_message("AI"):
        response = st.write_stream(get_response(user_query))
    
    st.session_state.chat_history.append(AIMessage(content=response))