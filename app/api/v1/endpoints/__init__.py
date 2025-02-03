from app.api.v1.endpoints.students import router as student_routes
from app.api.v1.endpoints.auth import router as auth_routes
from app.api.v1.endpoints.teachers import router as teacher_routes
from app.api.v1.endpoints.parents import router as parents_routes
from app.api.v1.endpoints.attendance import router as attendance_routes
from app.api.v1.endpoints.exams import router as exam_routes
from app.api.v1.endpoints.notifications import router as notification_routes
from app.api.v1.endpoints.fees import router as fee_routes


__all__ = [
    "student_routes",
    "auth_routes",
    "teacher_routes",
    "parents_routes",
    attendance_routes,
    exam_routes,
    notification_routes,
    fee_routes
]
