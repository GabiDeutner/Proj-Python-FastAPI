# user = {
#     "nome": "Fulano",
#     "idade": 25,
#     "email": "fulano@email.com"
# }
# print(user)

from pydantic import BaseModel, validator

class User(BaseModel):
    nome: str
    idade: int
    email: str
    
    @validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('E-mail está inválido')
        return value
    
user1 = User(
    nome='Fulano',
    idade=25,
    email='fulano@email.com'
)
user2 = User(
    nome='Sicrano',
    idade=21,
    email='sicrano@email.com'
)

print(user1)
