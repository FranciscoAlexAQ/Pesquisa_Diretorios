import os

class Pesquisa:
    def pesquisar(self, dados, tipo='Arquivo'):
        self.encontrado = 0 
        lista = []
        if tipo == 'Pasta':
            for self.diretorios, self.pastas, self.Arquivos in os.walk(r'C:\\'):
                if dados in self.pastas:
                    self.encontrado += 1
                    for pasta in self.pastas:
                        if pasta == dados:
                            self.nome = pasta 
                            self.tamanho = os.path.getsize(self.diretorios + '\\' + pasta)
                            self.caminho = self.diretorios
                            lista.append([self.nome, self.tamanho, self.caminho])

            if self.encontrado == 0:
                return ''
            return lista
         
        else:
            for self.diretorios, self.pastas, self.Arquivos in os.walk(r'C:\\'):
                if dados in self.Arquivos:
                    self.encontrado += 1
                    for arquivo in self.Arquivos:
                        if arquivo == dados:
                            self.nome = arquivo
                            self.tamanho = os.path.getsize(self.diretorios + '\\' + arquivo)
                            self.caminho = self.diretorios
                            lista.append([self.nome, self.tamanho, self.caminho])

            if self.encontrado == 0:
                return ''
            return lista


if __name__ == '__main__':
    dado = Pesquisa()

    print(dado.pesquisar('teste1.txt'))
