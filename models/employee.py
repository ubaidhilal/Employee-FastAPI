from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import  String, Boolean, Enum as SqlEnum
from enum import Enum
from core.database import Base



class UserRole(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"


class Employee(Base):
    __tablename__="employees"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    role: Mapped[UserRole] = mapped_column(SqlEnum(UserRole),default=UserRole.EMPLOYEE)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    