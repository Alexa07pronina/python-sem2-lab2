from src.models import Task
from typing import List

class FakeApiSource:
    """API заглушка"""
    def __init__(self,url:str):
        self.url = url
        self._tasks = [
            Task(payload={"role": "admin", "ip": "255.255.255.255"},priority=5),
            Task(payload={"role": "user"},priority=2),
            Task(payload={"role":"user", "error": 500})
        ]
    def get_tasks(self) -> List[Task]:
        return self._tasks
