from fastapi import APIRouter, Depends
from core.dependency import  db_dependency
from typing import List
from schemas.employee import EmployeeCreate,EmployeeOut
from fastapi.security import OAuth2PasswordRequestForm
from core .security import get_current_user
from services.employee import register_employee_service,register_login_service,get_all_employee_service, delete_employee_by_id_service




router = APIRouter(tags=["Employees"])


@router.post("/register")
async def register_employee(db:db_dependency,employee:EmployeeCreate):
    return register_employee_service(db, employee)


@router.post("/login")
async def login_employee(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    return register_login_service(db, form_data)



@router.get("/employee",response_model=List[EmployeeOut])
async def get_employees(db:db_dependency):
    return get_all_employee_service(db)


@router.delete("/employee/{employee_id}")
async def delete_employee_by_id(db:db_dependency,employee_id:int, current_user : dict = Depends(get_current_user)):
    return delete_employee_by_id_service(db, employee_id,current_user)
    
    


