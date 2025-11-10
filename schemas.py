"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Social app schemas

class Profile(BaseModel):
    """Minimal user profile for the social grid"""
    handle: str = Field(..., description="Unique username/handle")
    display_name: str = Field(..., description="Public display name")
    avatar_url: Optional[str] = Field(None, description="Avatar image URL")
    bio: Optional[str] = Field(None, description="Short bio")

class Post(BaseModel):
    """Lightweight post for the activity feed"""
    author_handle: str = Field(..., description="Handle of the author")
    text: str = Field(..., max_length=280, description="Post content")
    image_url: Optional[str] = Field(None, description="Optional image")
    likes: int = Field(0, ge=0, description="Like count")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp; set automatically if missing")

class Follow(BaseModel):
    follower: str = Field(..., description="Follower handle")
    following: str = Field(..., description="Following handle")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
