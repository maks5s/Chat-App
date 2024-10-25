from pydantic import BaseModel, Field


class MessageRead(BaseModel):
    id: int = Field(..., description="Message ID")
    sender_id: int = Field(..., description="Sender`s ID")
    recipient_id: int = Field(..., description="Recipient`s ID")
    content: str = Field(..., description="Message content")


class MessageCreate(BaseModel):
    recipient_id: int = Field(..., description="Recipient`s ID")
    content: str = Field(..., description="Message content")
