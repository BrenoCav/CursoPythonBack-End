def cadastro_alunos():
    """Programa de cadastro de Alunos Simplificado"""
    alunos = []
    
    print("=" * 30)
    print("SISTEMA DE CADASTRO DE ALUNOS")
    print("=" * 30)
    
    while True:
    
        print("\n" + "-" * 30)
        print("MENU PRINCIPAL")
        print("-" * 30)
        print("1 - Cadastrar novo Aluno")
        print("2 - Listar Alunos Cadastrados")
        print("3 - Sair")
        print("-" * 30)
    
        opcao = input("Digite a opção desejada (1-3): ")
    
        if opcao == "1":
            print("\n-- CADASTRAR NOVO ALUNO--")
        
            try:
                nome = input("Digite o nome do aluno: ")
                matricula_input = input("Digite o número da matrícula: ")
                matricula = int(matricula_input)
                curso = input("Digite o curso do aluno: ")
                
                matricula_existente = False
                for aluno in alunos:
                    if aluno["matricula"] == matricula:
                        matricula_existente = True
                        break
                if matricula_existente:
                    print(" Erro: Matrícula já cadastrada!")
                else:
                   
                    novo_aluno = {
                        "nome": nome,
                        "matricula": matricula,
                        "curso": curso
                    }
                    alunos.append(novo_aluno)
                    print("Aluno cadastrado com sucesso!")


            except ValueError:
                print("Erro: A matrícula deve ser um número!")
        
        
        elif opcao == "2":
            print("\n-- LISTA DE ALUNOS CADASTRADOS --")
            if not alunos:
                print("Nenhum aluno cadastrado")
    
            else:
                for i, aluno in enumerate(alunos, 1):
                    print(f"{i}. Nome:{aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}")
        
        elif opcao == "3":
            print("\nObrigado por usar o Sistema de Cadastro de Alunos, até logo")
            print("Encerrando o programa...")
            break
        else:
                                        print("\n Opção inválinda! Digite um número entre 1 e 3.")
    
if __name__ == "__main__":
    cadastro_alunos()