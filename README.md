# FastAPI SQL Query Generator

This project is a **FastAPI-based backend application** that interprets user instructions in natural language, extracts intent using AI, and dynamically generates SQL queries to interact with a PostgreSQL database. It uses LangChain or Llama for intent recognition and query generation.

## Features

- Parses natural language instructions to identify the intent (e.g., 'add_student', 'get_student', 'get_scores', 'add_score', 'get_student_subjects', 'summarizing_data', etc etc.).
- Dynamically generates SQL queries based on the provided database schema.
- Interacts with PostgreSQL to execute the generated queries.

---

## Database Schema

The application works with the following schema:

### **`students` Table**
| Column      | Type    | Constraints       |
|-------------|---------|-------------------|
| `id`        | SERIAL  | PRIMARY KEY       |
| `name`      | TEXT    | NOT NULL          |
| `student_id`| TEXT    | UNIQUE, NOT NULL  |

### **`scores` Table**
| Column       | Type    | Constraints                                |
|--------------|---------|--------------------------------------------|
| `id`         | SERIAL  | PRIMARY KEY                                |
| `student_id` | TEXT    | FOREIGN KEY REFERENCES `students.student_id`, NOT NULL |
| `subject`    | TEXT    | NOT NULL                                   |
| `score`      | INTEGER | NOT NULL                                   |

**Relationships**:
- `scores.student_id` references `students.student_id`.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fastapi-sql-generator.git
   cd fastapi-sql-generator

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Create a new virtual environment**:
   ```bash
   python3 -m venv .venv

4. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate

5. **Add environment variables**:
   ```bash
   AZURE_ENDPOINT = "https://xxxx.openai.azure.com/"

   AZURE_OPENAI_DEPLOYMENT = "gpt-**"

   OPENAI_API_VERSION = "******"

   OPENAI_API_KEY = "78**" 

6. **Run the application**:
   ```bash
   uvicorn main:app --port 8080 --reload

7. **Access the API**:
   ```bash
   http://localhost:8080
   ```

---