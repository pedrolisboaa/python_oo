from enum import Enum, auto


class Direcao(Enum):
    norte = auto()
    sul = auto()
    leste = auto()
    oeste = auto()


def move(direction):
    if not isinstance(direction, Direcao):
        raise ValueError('Não é possível mover nessa direção')

    return f'Movendo {direction.name}'


if __name__ == '__main__':
    print(move(Direcao.sul))
    print(move(Direcao.norte))