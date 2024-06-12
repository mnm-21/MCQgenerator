import os
import PyPDF2
import json
import traceback
from src.mcqgenerator.logger import logging

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
            
        except Exception as e:
            logging.error(f"Error in reading pdf file {e}")
            raise Exception("error reading the PDF file")
            
    
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("unsupported file format only pdf and text file supported")
    

def get_table_data(quiz_str):
    try:
        if not quiz_str:
            raise ValueError("The quiz string is empty")
        quiz_dict=json.loads(quiz_str)
        # Debug: Check the contents of quiz_dict
        # print("Quiz Dictionary:", quiz_dict)

        quiz_table_data=[]
        
        for key,value in quiz_dict.items():
            mcq = value["mcq"]
            options = " | ".join([f"{option}: {option_value}" for option, option_value in value["options"].items()])
            correct = value["correct"]
            quiz_table_data.append({"Question no.":key,"MCQ": mcq, "Choices": options, "Correct": correct})
        
        # Debug: Check the structure of quiz_table_data
        # print("Quiz Table Data:", quiz_table_data)
        
        return quiz_table_data
    
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding error: {e}")
        return None
       
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
    
