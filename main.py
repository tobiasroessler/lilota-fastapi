from contextlib import asynccontextmanager
from fastapi import FastAPI
from lilota.core import Lilota
from models import ReportInput
from uuid import UUID


lilota = Lilota(
    db_url="sqlite:///tasks.db",
	script_path="tasks.py"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
	lilota.start()
	yield
	lilota.stop()


app = FastAPI(lifespan=lifespan)


@app.post("/reports")
def create_report(data: ReportInput):
    task_id = lilota.schedule("generate_report", data)
    return {
        "task_id": task_id
    }


@app.get("/tasks/{task_id}") 
def get_task(task_id: UUID): 
    task = lilota.get_task_by_id(task_id) 
    return { 
        "id": task.id, 
        "status": task.status
    }


@app.get("/tasks/{task_id}/result")
def get_result(task_id: UUID): 
    task = lilota.get_task_by_id(task_id)
    return { 
        "status": task.status, 
        "result": task.output
    }