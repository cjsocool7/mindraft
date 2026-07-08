from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Edge:
    id: str
    source_id: str
    target_id: str