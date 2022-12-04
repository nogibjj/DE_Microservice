""" Import Necessary Library """
from typing import Optional
from pydantic import BaseModel


class AuthorRequest(BaseModel):
    """AuthorRequest Class"""

    likes: Optional[int] = None
    shares: Optional[int] = None
    comments: Optional[int] = None
    plays: Optional[int] = None


class TrendingVideoRequest(BaseModel):
    """TrendingVideoRequest Class"""

    likes: Optional[int] = None
    shares: Optional[int] = None
    comments: Optional[int] = None
    plays: Optional[int] = None


class FilterVideoRequest(BaseModel):
    """FilterVideoRequest Class"""

    desc: Optional[str] = None
