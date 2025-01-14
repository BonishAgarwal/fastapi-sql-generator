import json
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from typing import Tuple
from dotenv import load_dotenv

load_dotenv()

llm=AzureChatOpenAI(
                azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
                deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT"),
                openai_api_version = os.getenv("OPENAI_API_VERSION"),
                openai_api_key = os.getenv("OPENAI_API_KEY"),
            )

PROMPT_TEMPLATE = """
You are an SQL expert. Analyze the following user instruction and generate the appropriate SQL query.
Refer to the schema provided below while generating the query.

Schema:
    Tables:
    - students: id (SERIAL, Primary Key), name (TEXT, Not Null), student_id (TEXT, Unique, Not Null)
    - scores: id (SERIAL, Primary Key), student_id (TEXT, Not Null, Foreign Key), subject (TEXT, Not Null), score (INTEGER, Not Null)

    Relationships:
    - scores.student_id references students.student_id

Instruction: {instruction}

Return the output in the following JSON format:
{{
    "intent": "<intent>",  // The type of operation: 'add_student', 'get_student', 'get_scores', 'add_score', 'get_student_subjects', 'summarizing_data', etc
    "sql_query": "<sql_query>"  // The corresponding SQL query based on the instruction
}}
"""

async def process_instruction(instruction: str) -> Tuple[str, dict]:
    prompt = PromptTemplate(
                            template=PROMPT_TEMPLATE, 
                            input_variables=["instruction"]
                        )
    response = llm(prompt.format(instruction=instruction))
    res = json.loads(response.content)

    return res["intent"], res["sql_query"]