from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.langchain_processor import process_instruction
from app.db import get_connection
from app.pydantic_model import InstructionRequest

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/process-instruction")
async def process_professor_instruction(request: InstructionRequest):
    instruction = request.instruction
    
    intent, query = await process_instruction(instruction)
    
    print("Intent:", intent)
    print("Query:", query)
    
    # Step 2: Route to the appropriate endpoint
    if intent == "add_student":
        return add_student(query)
    elif intent == "get_student":
        return get_student(query)
    elif intent == "add_score":
        return add_score(query)
    elif intent == "get_scores":
        return get_scores(query)
    elif intent == "get_student_subjects":
        return get_student_subjects(query)
    elif intent == "summarizing_data":
        return summarize_scores(query)
    else:
        raise HTTPException(status_code=400, detail="Unrecognized intent")

@router.post("/add_student")
def add_student(query: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:  
            cur.execute(query)
            conn.commit()  # Commit the transaction
            print("Student added successfully.")
        return JSONResponse(content="Student added successfully", status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get_student")
def get_student(query: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:  
            cur.execute(query)
            conn.commit()  # Commit the transaction
        return JSONResponse(content="Student retrieved successfully", status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/add_score")
def add_score(query: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:  
            cur.execute(query)
            conn.commit()  # Commit the transaction
        return JSONResponse(content="Scores for student added successfully", status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get_scores")
def get_scores(query: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:  
            cur.execute(query)
            conn.commit()  # Commit the transaction
        return JSONResponse(content="Scores retrieved successfully", status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get_student_subjects")
def get_student_subjects(query: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:  
            cur.execute(query)
            conn.commit()  # Commit the transaction
        return JSONResponse(content="Subjects retrieved successfully", status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/summarize_scores")
def summarize_scores(query: str):
    conn = get_connection()
    try:
        with conn.cursor() as cur:  
            cur.execute(query)
            conn.commit()  # Commit the transaction
        return JSONResponse(content="Scores summarized", status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))