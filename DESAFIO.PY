"""Simulação de inscrição em concurso público (atividade de condicionais)."""

print("=" * 45)
print("     FORMULÁRIO DE INSCRIÇÃO - CONCURSO")
print("=" * 45)

nome = input("Nome completo: ").strip()
try:
    idade = int(input("Idade: "))
except ValueError:
    idade = -1

if idade < 18:
    print("\nInscrição não permitida: é necessário ter pelo menos 18 anos.")
    print("Nome:", nome if nome else "Não informado")
    print("Status: INSCRIÇÃO COM PENDÊNCIAS")
else:
    cpf = input("CPF (11 números, sem pontos ou traço): ").strip()

    print("\nESCOLARIDADE")
    print("1 - Ensino Médio")
    print("2 - Ensino Superior")
    print("3 - Pós-graduação")
    opcao_escolaridade = input("Escolha uma opção: ").strip()
    if opcao_escolaridade == "1":
        escolaridade = "Ensino Médio"
    elif opcao_escolaridade == "2":
        escolaridade = "Ensino Superior"
    elif opcao_escolaridade == "3":
        escolaridade = "Pós-graduação"
    else:
        escolaridade = "Opção inválida"

    sexo = input("\nSexo (M ou F): ").strip().upper()
    if sexo == "M":
        documento = "Certificado de Reservista"
        print("Será necessário apresentar o Certificado de Reservista.")
    elif sexo == "F":
        documento = "Documento militar não necessário"
        print("Não é necessário apresentar documento militar.")
    else:
        documento = "Sexo inválido: não foi possível definir o documento"
        print("Valor inválido para sexo. Digite M ou F.")

    print("\nÁREA PROFISSIONAL")
    print("1 - Administração")
    
    print("2 - Tecnologia da Informação")
    print("3 - Educação")
    opcao_area = input("Escolha uma opção: ").strip()
    if opcao_area == "1":
        area = "Administração"
        cargo = "Analista Administrativo"
    elif opcao_area == "2":
        area = "Tecnologia da Informação"
        cargo = "Analista de Sistemas"
    elif opcao_area == "3":
        area = "Educação"
        cargo = "Professor"
    else:
        area = "Opção inválida"
        cargo = "Não definido"

    cpf_valido = len(cpf) == 11 and cpf.isdigit()
    if not cpf_valido:
        print("\nCPF inválido: digite exatamente 11 números.")

    if (nome != "" and cpf_valido and
            escolaridade != "Opção inválida" and
            sexo in ("M", "F") and area != "Opção inválida"):
        status = "INSCRIÇÃO APROVADA"
    else:
        status = "INSCRIÇÃO COM PENDÊNCIAS"

    print("\n" + "=" * 45)
    print("RESUMO DA INSCRIÇÃO")
    print("Nome:", nome if nome else "Não informado")
    print("CPF:", cpf)
    print("Idade:", idade)
    print("Escolaridade:", escolaridade)
    print("Área profissional:", area)
    print("Cargo:", cargo)
    print("Documento adicional:", documento)
    print("Status:", status)
    print("=" * 45)
