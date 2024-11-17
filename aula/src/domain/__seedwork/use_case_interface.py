from abc import ABC, abstractmethod
from typing import Any


class UserCaseInterface(ABC):

    @abstractmethod
    def execute(self, input: Any) -> Any:
        raise NotImplementedError
