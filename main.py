class No:
    def __init__(self, nome):
        self.nome = nome
        self.esquerda = None
        self.direita = None

class ArvoreFamiliaAnimais:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome):
        def _inserir(no, nome):
            if no is None:
                return No(nome)
            if nome < no.nome:
                no.esquerda = _inserir(no.esquerda, nome)
            elif nome > no.nome:
                no.direita = _inserir(no.direita, nome)
            return no
        self.raiz = _inserir(self.raiz, nome)

    def remover(self, nome):
        def _remover(no, nome):
            if no is None:
                return None
            if nome < no.nome:
                no.esquerda = _remover(no.esquerda, nome)
            elif nome > no.nome:
                no.direita = _remover(no.direita, nome)
            else:
                if no.esquerda is None and no.direita is None:
                    return None
                if no.esquerda is None:
                    return no.direita
                if no.direita is None:
                    return no.esquerda
                sucessor = no.direita
                while sucessor.esquerda:
                    sucessor = sucessor.esquerda
                no.nome = sucessor.nome
                no.direita = _remover(no.direita, sucessor.nome)
            return no
        self.raiz = _remover(self.raiz, nome)

    def listar_em_ordem(self):
        def _em_ordem(no):
            if no:
                _em_ordem(no.esquerda)
                print(no.nome)
                _em_ordem(no.direita)
        print("\nElementos em ordem:")
        _em_ordem(self.raiz)

    def exibir_estrutura(self):
        print("\nEstrutura da árvore:")
        self._exibir(self.raiz)

    def _exibir(self, no, prefixo="", eh_esquerda=True):
        if no is not None:
            if no.direita:
                novo_prefixo = prefixo + ("│   " if eh_esquerda else "    ")
                self._exibir(no.direita, novo_prefixo, False)
            print(prefixo + ("└── " if eh_esquerda else "┌── ") + no.nome)
            if no.esquerda:
                novo_prefixo = prefixo + ("    " if eh_esquerda else "│   ")
                self._exibir(no.esquerda, novo_prefixo, True)

# Menu interativo
if __name__ == "__main__":
    arvore = ArvoreFamiliaAnimais()

    # Lista inicial de animais
    animais_iniciais = [
        "Macaco", "Baleia", "Abelha", "Avestruz",
        "Cachorro", "Rinoceronte", "Ornitorrinco", "Zebra"
    ]
    for animal in animais_iniciais:
        arvore.inserir(animal)

    print("Árvore inicial criada com animais pré-definidos.")

    while True:
        print("\n--- MENU ---")
        print("1. Inserir animal")
        print("2. Remover animal")
        print("3. Listar animais em ordem alfabética")
        print("4. Exibir estrutura da árvore")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do animal: ")
            arvore.inserir(nome)
            print(f"'{nome}' inserido na árvore.")
        elif opcao == "2":
            nome = input("Digite o nome do animal a remover: ")
            arvore.remover(nome)
            print(f"'{nome}' removido da árvore (se existia).")
        elif opcao == "3":
            arvore.listar_em_ordem()
        elif opcao == "4":
            arvore.exibir_estrutura()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
