def animal(bicho):
    animal = {
        'aguia' : ['vertebrado', 'ave', 'carnivoro'],
        'pomba' : ['vertebrado', 'ave', 'onivoro'],
        'homem' : ['vertebrado', 'mamifero', 'onivoro'],
        'vaca' : ['vertebrado', 'mamifero', 'herbivoro'],
        'pulga' : ['invertebrado', 'inseto', 'hematofago'],
        'lagarta' : ['invertebrado', 'inseto', 'herbivoro'],
        'sanguessuga' : ['invertebrado', 'anelideo', 'hematofago'],
        'minhoca' : ['invertebrado', 'anelideo', 'onivoro'],
    }
    for nome, ordem in animal.items():
        if bicho == ordem: return print(nome)

if __name__ == '__main__':
    entrada = [input(), input(), input()]
    animal(entrada)
