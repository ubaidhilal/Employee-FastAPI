from models.employee import Employee
from core.security import hash_password

def get_user_by_email(db, email:str):
    return db.query(Employee).filter(Employee.email == email).first()

def register_repo(db, employee):
    new_employee = Employee(
        name= employee.name,
        email= employee.email,
        password= hash_password(employee.password),
        role = employee.role
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return (new_employee)
    

def get_all_employee_repo(db):
    return db.query(Employee).all()   


def get_employee_by_id(db,employee_id:int):
   return db.query(Employee).filter(Employee.id == employee_id).first()     

def delete_employee_repo(db, db_employee):
    db.delete(db_employee)
    db.commit()

def update_employee_repo(db, db_employee):
    db.commit()
    db.refresh(db_employee)


   