import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from streamlit_option_menu import option_menu
from src.mcqgenerator.MCQgenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging
from langchain_community.callbacks.manager import get_openai_callback

with open('Response.json','r') as file:
    RESPONSE_JSON = json.load(file)
with st.sidebar:
    selection = option_menu('Menu',
                            
                            ['🏠 Home Page',
                             '📝 MCQ generator'],
                            
                            icons = ['house-door-fill','capsule'],
                            
                            default_index = 0)
    
# Home page    
if selection == '🏠 Home Page':
    st.title('🚀 Welcome to the MCQ Generator using LangChain! 🌟')
    st.write("""
    Welcome to MCQ Generator - an end-to-end project for effortless quiz creation, powered by LangChain!
    
    Crafted by **Mayank Chandak** from **IIT Madras**, this project leverages the cutting-edge OpenAI model `gpt-3.5-turbo` via API to seamlessly generate multiple-choice questions from your text or PDF files.
    With a user-friendly interface and AI-driven intelligence, MCQ Generator streamlines the quiz creation process from start to finish.
    Whether you're a student, educator, or quiz enthusiast, unlock the power of AI for your quizzes today! 🚀📚
    """)


if selection == '📝 MCQ generator':
    st.title('📝 MCQ Generator')
    st.write("Fill in the details below to generate your quiz!")
    with st.form("User inputs"):
        # File upload
        uploaded_file = st.file_uploader("📄 Upload the PDF or text file")

        # No. of questions
        mcq_count = st.number_input("🔢 Number of MCQs", min_value=1, max_value= 20)

        # Subject
        subject = st.text_input("📚 Subject of the PDF/text file", max_chars=30)

        # Quiz tone
        tone = st.text_input("🎯 Difficulty level", max_chars=20, placeholder="Simple")

        # Submit button
        button = st.form_submit_button("Generate MCQs 🚀")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Generating your quiz... ⏳"):
            try:
                text = read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone" : tone,
                            "response_json" : json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error!!")

            else:
                logging.info(f"Total Tokens:{cb.total_tokens}\nPrompt Tokens:{cb.prompt_tokens}\nCompletion Tokens:{cb.completion_tokens}\nTotal Cost:{cb.total_cost}")
                #print(f"Prompt Tokens:{cb.prompt_tokens}")
                #print(f"Completion Tokens:{cb.completion_tokens}")
                #print(f"Total Cost:{cb.total_cost}")
                if isinstance(response, dict):
                    quiz = response.get("quiz",None)
                    if quiz is not None:
                        # Debug: Print the quiz string
                        #   print("Quiz String:", quiz)
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.set_index('Question no.', inplace=True)
                            st.table(df)
                            st.text_area("📊 Quiz Analysis",value=response["review"], height=150)
                            
                            # Download
                            csv = df.to_csv().encode('utf-8')
                            st.download_button(
                                label="📥 Download Quiz as CSV",
                                data=csv,
                                file_name='quiz.csv',
                                mime='text/csv'
                            )
                        else:
                            st.error("Error in generating table")
                    else:
                        st.error("Error in retrieving the quiz.")
                else:
                    st.write(response)
    
    st.warning("Please note that not all PDF files may be compatible. Complex or encrypted PDFs may not be processed correctly.")
