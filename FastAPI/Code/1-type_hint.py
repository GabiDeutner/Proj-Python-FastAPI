# Sem Type Hint
def hello(name):
    return f'Olá {name}'

# Com Type Hint
def hello2(name: str) -> str:
    return f'Olá {name}'

# Sem Type Hint
list_users = [
    "Fulano", "Sicrano"
]

# Com Type Hint
list_users2: list[str] = [
    "Fulano", "123"
]

# Sem Type Hint
dict_users = {
    1: "FUlano",
    2: "Sicrano"
}

# Com TYpe Hint
dict_users2: dict[str, str] = {
    "1": "Fulano",
    "2": "Sicrano"
} 

print(hello2('Rodrigo'))
print(list_users2)
print(dict_users2)
