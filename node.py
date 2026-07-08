from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Node:
    id: str
    label: str
    x: float
    y: float