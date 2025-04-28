class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.esquerda = None
        self.direita = None


class ArvoreFamiliaAnimais:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome):
        if self.raiz is None:
            self.raiz = Animal(nome)
        else:
            self._inserir_recursivo(nome, self.raiz)

    def _inserir_recursivo(self, nome, no_atual):
        if nome < no_atual.nome:
            if no_atual.esquerda is None:
                no_atual.esquerda = Animal(nome)
            else:
                self._inserir_recursivo(nome, no_atual.esquerda)
        elif nome > no_atual.nome:
            if no_atual.direita is None:
                no_atual.direita = Animal(nome)
            else:
                self._inserir_recursivo(nome, no_atual.direita)
        else:
            print(f"O animal {nome} já existe na árvore!")

    def remover(self, nome):
        self.raiz = self._remover_recursivo(nome, self.raiz)

    def _remover_recursivo(self, nome, no_atual):
        if no_atual is None:
            return no_atual

        if nome < no_atual.nome:
            no_atual.esquerda = self._remover_recursivo(nome, no_atual.esquerda)
        elif nome > no_atual.nome:
            no_atual.direita = self._remover_recursivo(nome, no_atual.direita)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            no_atual.nome = self._encontrar_minimo(no_atual.direita).nome
            no_atual.direita = self._remover_recursivo(no_atual.nome, no_atual.direita)

        return no_atual

    def _encontrar_minimo(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

    def listar_em_ordem(self):
        animais = []
        self._em_ordem_recursivo(self.raiz, animais)
        return animais

    def _em_ordem_recursivo(self, no, animais):
        if no is not None:
            self._em_ordem_recursivo(no.esquerda, animais)
            animais.append(no.nome)
            self._em_ordem_recursivo(no.direita, animais)

    def buscar(self, nome):
        return self._buscar_recursivo(nome, self.raiz)

    def _buscar_recursivo(self, nome, no_atual):
        if no_atual is None:
            return False
        if nome == no_atual.nome:
            return True
        elif nome < no_atual.nome:
            return self._buscar_recursivo(nome, no_atual.esquerda)
        else:
            return self._buscar_recursivo(nome, no_atual.direita)


def menu():
    arvore = ArvoreFamiliaAnimais()

    # Só colocando alguns animais inicialmente
    animais_iniciais = ["Leão", "Girafa", "Elefante", "Zebra", "Macaco"]
    for animal in animais_iniciais:
        arvore.inserir(animal)

    while True:
        print("\n=== MENU - ÁRVORE DE ANIMAIS ===")
        print("1. Visualizar todos os animais")
        print("2. Inserir novo animal")
        print("3. Remover animal")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            animais = arvore.listar_em_ordem()
            if animais:
                print("\nAnimais na árvore:")
                for i, animal in enumerate(animais, 1):
                    print(f"{i}. {animal}")
            else:
                print("\nA árvore está vazia!")

        elif opcao == "2":
            novo_animal = input("\nDigite o nome do animal a ser inserido: ").strip().capitalize()
            if novo_animal:
                if arvore.buscar(novo_animal):
                    print(f"O animal {novo_animal} já existe na árvore!")
                else:
                    arvore.inserir(novo_animal)
                    print(f"Animal {novo_animal} inserido com sucesso!")
            else:
                print("Nome inválido!")

        elif opcao == "3":
            animais = arvore.listar_em_ordem()
            if not animais:
                print("\nA árvore está vazia, não há animais para remover!")
                continue

            print("\nAnimais disponíveis para remoção:")
            for i, animal in enumerate(animais, 1):
                print(f"{i}. {animal}")

            try:
                escolha = input("\nDigite o número ou nome do animal a ser removido: ")
                # Verifica se o usuário digitou um número
                if escolha.isdigit():
                    indice = int(escolha) - 1
                    if 0 <= indice < len(animais):
                        animal_remover = animais[indice]
                    else:
                        print("Número inválido!")
                        continue
                else:
                    animal_remover = escolha.strip().capitalize()

                if arvore.buscar(animal_remover):
                    arvore.remover(animal_remover)
                    print(f"Animal {animal_remover} removido com sucesso!")
                else:
                    print(f"Animal {animal_remover} não encontrado na árvore!")
            except ValueError:
                print("Entrada inválida!")

        elif opcao == "4":
            print("\nSaindo do programa...")
            break

        else:
            print("\nOpção inválida! Por favor, escolha uma opção de 1 a 4.")


if __name__ == "__main__":
    menu()