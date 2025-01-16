class Livro:
    def __init__(self, titulo, autor, genero, preco, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.preco = preco
        self.disponivel = disponivel
    
    def __str__(self):
        return f"{self.titulo} de {self.autor} ({self.genero}) - {'Disponível' if self.disponivel else 'Indisponível'}"

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.histórico = []
    
    def registrar_histórico(self, livro, ação):
        self.histórico.append((livro, ação))
    
    def visualizar_histórico(self):
        print(f"\nHistórico de {self.nome}:")
        for livro, ação in self.histórico:
            print(f"{livro.titulo} - {ação}")

class SistemaLivrariaBiblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def pesquisar_livro(self, termo):
        resultados = [livro for livro in self.livros if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower()]
        return resultados
    
    def reservar_livro(self, usuario, livro):
        if livro.disponivel:
            livro.disponivel = False
            usuario.registrar_histórico(livro, "Reservado")
            print(f"Livro '{livro.titulo}' reservado com sucesso!")
        else:
            print(f"O livro '{livro.titulo}' não está disponível para reserva.")
    
    def comprar_livro(self, usuario, livro):
        usuario.registrar_histórico(livro, "Comprado")
        print(f"Livro '{livro.titulo}' comprado com sucesso!")
    
    def exibir_livros_disponiveis(self):
        for livro in self.livros:
            print(livro)

sistema = SistemaLivrariaBiblioteca()

livro1 = Livro("O Alquimista", "Paulo Coelho", "Aventura", 30)
livro2 = Livro("1984", "George Orwell", "Distopia", 25)
livro3 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 50)

sistema.adicionar_livro(livro1)
sistema.adicionar_livro(livro2)
sistema.adicionar_livro(livro3)

usuario1 = Usuario("João", "joao@email.com")
sistema.cadastrar_usuario(usuario1)

print("Pesquisa por '1984':")
resultados = sistema.pesquisar_livro('1984')
for livro in resultados:
    print(livro)

sistema.reservar_livro(usuario1, livro2)
sistema.comprar_livro(usuario1, livro1)
usuario1.visualizar_histórico()

print("\nLivros Disponíveis:")
sistema.exibir_livros_disponiveis()

