from pydantic import BaseModel


class PaymentMethod(BaseModel):
    id: str
    saved: bool

class MetaData(BaseModel):
    telegram_id: int
    one_time: bool | None


class Object(BaseModel):
    payment_method: PaymentMethod
    metadata: MetaData


class YooKassaSchema(BaseModel):
    object: Object

