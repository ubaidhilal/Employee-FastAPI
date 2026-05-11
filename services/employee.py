from repo.employee import get_user_by_email,register_repo,get_all_employee_repo, get_employee_by_id, delete_employee_repo
from fastapi import  HTTPException,status
from core.security import create_token, verify_password



def register_employee_service(db, employee ):
    existing = get_user_by_email(db, employee.email)
    if existing:
        raise HTTPException(status_code=409, detail="Email already exists")
    db_employee = register_repo(db, employee)   
    return {
        "success": True,
        "message": "Employee registered successfully",
        "data": {
            "id": db_employee.id,
            "name": db_employee.name,
            "email": db_employee.email,
            "role": db_employee.role
        }
    } 
    
def register_login_service(db,form_data):
    db_user = get_user_by_email(db, form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"user_id": db_user.id, "user_email": db_user.email, "role" : db_user.role})
    return {
            "access_token": token,
            "message": "Login successful"
    }

def get_all_employee_service(db):
    employee = get_all_employee_repo(db)
    if not employee:
        raise HTTPException(status_code=404, detail="No employee found")
    return employee

def delete_employee_by_id_service(db, employee_id,current_user):
    if current_user.get("role") != "admin":
          raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only admin can delete employees")
    db_employee = get_employee_by_id(db, employee_id)   
    if not db_employee:raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    delete_employee_repo(db, db_employee)
    return {"message" : "Employee deleted successfully"}

    


    

