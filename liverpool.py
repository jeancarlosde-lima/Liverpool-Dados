class Academia:
    def __init__(self, localizacao, campos, ginasios, instalacoes_reabilitacao):
        self.localizacao = localizacao
        self.campos = campos
        self.ginasios = ginasios
        self.instalacoes_reabilitacao = instalacoes_reabilitacao
    
    def mostrar_informacoes(self):
        print(f"Localização: {self.localizacao}")
        print(f"Campos de Treinamento: {self.campos}")
        print(f"Ginásios: {self.ginasios}")
        print(f"Instalações de Reabilitação: {self.instalacoes_reabilitacao}")

class FilosofiaDeTreinamento:
    def __init__(self, estilo_jogo, uso_dados, desenvolvimento_holistico):
        self.estilo_jogo = estilo_jogo
        self.uso_dados = uso_dados
        self.desenvolvimento_holistico = desenvolvimento_holistico
    
    def mostrar_informacoes(self):
        print(f"Estilo de Jogo: {self.estilo_jogo}")
        print(f"Uso de Dados: {self.uso_dados}")
        print(f"Desenvolvimento Holístico: {self.desenvolvimento_holistico}")

class ProgramaDeDesenvolvimento:
    def __init__(self, estrutura, transicao, consistencia_estilo):
        self.estrutura = estrutura
        self.transicao = transicao
        self.consistencia_estilo = consistencia_estilo
    
    def mostrar_informacoes(self):
        print(f"Estrutura: {self.estrutura}")
        print(f"Transição para o Profissional: {self.transicao}")
        print(f"Consistência na Filosofia de Jogo: {self.consistencia_estilo}")

class CasoDeSucesso:
    def __init__(self, nome, desenvolvimento, impacto):
        self.nome = nome
        self.desenvolvimento = desenvolvimento
        self.impacto = impacto
    
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Desenvolvimento: {self.desenvolvimento}")
        print(f"Impacto no Time Principal: {self.impacto}")

def main():
    # Instância da Academia
    academia = Academia(
        localizacao="Kirkby",
        campos="Grama natural e artificial",
        ginasios="Equipados com tecnologia de ponta",
        instalacoes_reabilitacao="Recuperação e reabilitação avançadas"
    )
    
    # Instância da Filosofia de Treinamento
    filosofia_treinamento = FilosofiaDeTreinamento(
        estilo_jogo="Gegenpressing",
        uso_dados="Análise de desempenho avançada",
        desenvolvimento_holistico="Técnico, físico e mental"
    )
    
    # Instância do Programa de Desenvolvimento
    programa_desenvolvimento = ProgramaDeDesenvolvimento(
        estrutura="Categorias de base até o time principal",
        transicao="Treinamento e jogos menores com o time principal",
        consistencia_estilo="Filosofia de jogo unificada"
    )
    
    # Exemplos de Casos de Sucesso
    trent = CasoDeSucesso(
        nome="Trent Alexander-Arnold",
        desenvolvimento="Desenvolvido desde a academia do Liverpool",
        impacto="Um dos melhores laterais do mundo"
    )
    
    curtis = CasoDeSucesso(
        nome="Curtis Jones",
        desenvolvimento="Progrediu através das categorias de base",
        impacto="Peça importante no meio-campo do time principal"
    )
    
    # Exibir Informações
    print("Academia de Treinamento:")
    academia.mostrar_informacoes()
    print("\nFilosofia de Treinamento:")
    filosofia_treinamento.mostrar_informacoes()
    print("\nPrograma de Desenvolvimento de Jovens Talentos:")
    programa_desenvolvimento.mostrar_informacoes()
    print("\nCasos de Sucesso:")
    trent.mostrar_informacoes()
    curtis.mostrar_informacoes()

if __name__ == "__main__":
    main()
