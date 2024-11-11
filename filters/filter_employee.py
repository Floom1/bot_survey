from aiogram.filters import BaseFilter
from aiogram.types import Message
import os

class IsEmployeeFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        employee_id = int(os.getenv("EMPLOYEE_ID", "0"))
        return message.from_user.id == employee_id
