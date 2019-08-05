from pydantic import BaseModel
from typing import List

class Package(BaseModel):
    package: str
    version: str = None
    licenses: List[str] = None

class Packages(BaseModel):
    packages: List[Package]
