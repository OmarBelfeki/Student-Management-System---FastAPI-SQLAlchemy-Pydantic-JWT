from app.schemas.student import StudentResponse, StudentCreate, StudentUpdate
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.schemas.teacher import TeacherCreate, TeacherUpdate, TeacherResponse
from app.schemas.parent import ParentCreate, ParentUpdate, ParentResponse
from app.schemas.attendance import AttendanceResponse, AttendanceCreate
from app.schemas.exam import ExamResponse, ExamCreate
from app.schemas.fee import FeeCreate, FeeResponse
from app.schemas.notification import NotificationCreate, NotificationResponse

__all__ = [
    "UserCreate", "UserUpdate", "UserResponse",
    "StudentCreate", "StudentResponse", "StudentUpdate",
    TeacherCreate, TeacherUpdate, TeacherResponse,
    ParentCreate, ParentUpdate, ParentResponse,
    AttendanceResponse, AttendanceCreate,
    ExamResponse, ExamCreate,
    FeeCreate, FeeResponse,
    NotificationCreate, NotificationResponse
]
