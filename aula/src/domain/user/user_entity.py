from uuid import UUID, uuid4


class User:
    id: UUID
    name: str

    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name
        self.validade()

    def validate(self):
        if not isinstance(self.id, UUID):
            raise Exception('id must be an UUID')

        if not isinstance(self.name, str) or len(self.name) == 0:
            raise Exception('name is reaquired')

# usuario_1 = User(id=uuid4(), name='Vitória')
# usuario_2 = User(id=uuid4(), name='Alexandre')
# usuario_2.validate()
#
# usuario_3 = User(id=4, name='I am an invalid user')
# usuario_3.validate()
