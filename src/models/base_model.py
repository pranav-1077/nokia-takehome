from abc import ABC, abstractmethod


class BaseModel(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def forward(self, x):
        raise NotImplementedError