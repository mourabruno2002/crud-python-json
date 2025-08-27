"""SISTEMA CRUD - RACIOCÍNIO COMPUTACIONAL
PRODUZIDO POR: BRUNO EDUARDO DE MOURA"""

# Importa o módulo json.
import json

# Definição das funções do algorítmo.
def escrever(lista, nome_arquivo):
    """
    Grava os dados de uma lista ou dicionário em um arquivo .JSON.

    :param lista: Lista ou dicionário que será armazenado no arquivo.
    :param nome_arquivo: Nome do arquivo no qual os dados serão armazenados.
    :return: Retorna "True" caso os dados sejam salvos com sucesso.
    """
    try:
        with open(nome_arquivo, 'w', encoding = 'utf-8') as arquivo:
            json.dump(lista, arquivo, ensure_ascii = False)
        return True
    except:
        print('Erro ao gravar o arquivo.')

def ler(nome_arquivo):
    """
    Lê e carrega um arquivo .JSON.

    :param nome_arquivo: Nome do arquivo no qual os dados serão lidos.
    :return: Retorna "True" caso os dados sejam lidos com sucesso ou uma lista vazia caso não encontre o arquivo.
    """
    try:
        with open(nome_arquivo, 'r', encoding = 'utf-8') as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []

def menu_principal():
    """
    Exibe o menu principal e retorna a opção digitada pelo usuário.

    :return: Recebe e retorna a opção digitada pelo usuário.
    """
    print('========== MENU PRINCIPAL ==========')
    print('[1] ESTUDANTES\n[2] PROFESSORES\n[3] DISCIPLINAS\n[4] TURMAS\n[5] MATRÍCULAS\n[0] SAIR')
    print('====================================')
    print()
    return input('Insira uma das opções acima: ')

def menu_secundario(nome_menu):
    """
    Exibe o menu secundário e retorna a opção digitada pelo usuário..

    :return: Recebe e retorna a opção digitada pelo usuário.
    """
    print('== MENU OPERACIONAL {} =='.format(nome_menu))
    print('[1] INCLUIR\n[2] LISTAR\n[3] ATUALIZAR\n[4] EXCLUIR\n[0] VOLTAR AO MENU PRINCIPAL')
    print('====================================')
    print()
    return input('Insira uma das opções acima: ')

def verificar_codigo_existente(lista, codigo_verificar,nome_dados,codigo_atual):
    """
    Verifica se o código informado pelo usuário já esta presente no "arquivo.json".

    :param lista: Arquivo .json a ser lido e verificado.
    :param codigo_verificar: Código a ser verificado.
    :param nome_dados: Exibe um nome de acordo com a opção selecionada previamente ['ESTUDANTE', 'PROFESSOR', 'DISCIPLINA', 'TURMA', 'MATRÍCULA'], para melhor compreensão do usuário.
    :param codigo_atual: Código atual do cadastro a ser verificado.
    :return: Retorna "False" no caso o código pertença a outro cadastro e "True" caso já pertença ao cadastro atual.
    """
    for dados in lista:
        if dados['codigo'] == codigo_verificar:
            if dados['codigo'] == codigo_atual:
                return True
            print(f'O código * {codigo_verificar} * já está vinculado a outro {nome_dados}, por favor tente novamente.')
            return False
    return True

def inclusao(opcao,nome_arquivo,nome_menu,nome_dados):
    """
    Recebe os dados do usuário e realiza os cadastros para todos os módulos.

    :param opcao: Opção digitada pelo usuário no menu secundário.
    :param nome_arquivo: Nome do arquivo no qual os dados serão lidos e gravados.
    :param nome_menu: Denomina o menu de inclusão de acordo com o módulo escolhido.
    :param nome_dados: Exibe um nome de acordo com a opção selecionada previamente ['ESTUDANTE', 'PROFESSOR', 'DISCIPLINA', 'TURMA', 'MATRÍCULA'], para melhor compreensão do usuário.
    """
    lista = ler(nome_arquivo)
    print('==== INCLUSÃO {} ==== '.format(nome_menu))
    print()
    inclusao_continuar = True
    codigo = 0
    while inclusao_continuar:
        try:
            if opcao in ['1','2']:
                codigo = int(input(f'Digite o código do {nome_dados}: '))

            elif opcao in ['3','4']:
                codigo = int(input(f'Digite o código da {nome_dados}: '))
            # Verifica se o código já esta cadastrado para outro usuário.
            encontrado = False
            for dados in lista:
                if dados['codigo'] == codigo:
                    encontrado = True
                    break

            if encontrado:
                while True:
                    if opcao in ['1','2']:
                        codigo_ja_existe = input(f'O código {codigo} já está cadastrado para outro {nome_dados}, deseja inserir outro código? (s/n): ').lower()
                    else:
                        codigo_ja_existe = input(
                            f'O código {codigo} já está cadastrado para outra {nome_dados}, deseja inserir outro código? (s/n): ').lower()

                    if codigo_ja_existe != 's' and codigo_ja_existe != 'n':
                        print('Valor inválido, por favor digite "s" para SIM ou "n" para NÃO.')
                    elif codigo_ja_existe == 's':
                        inclusao_continuar = True
                        break
                    elif codigo_ja_existe == 'n':
                        print()
                        inclusao_continuar = False
                        break

            else:
                if opcao == '1' or opcao == '2':
                    nome = input(f'Digite o nome do {nome_dados}: ')
                    cpf = input(f'Digite o CPF do {nome_dados}: ')

                    dict_dados = {
                        'codigo': codigo,
                        'nome': nome,
                        'cpf': cpf
                    }
                    lista.append(dict_dados)
                    print()
                    print(f'{nome_dados} incluido com sucesso.')
                    print()
                    escrever(lista,nome_arquivo)
                    inclusao_continuar = False
                elif opcao == '3':
                    nome = input(f'Digite o nome da {nome_dados}: ')

                    dict_dados = {
                        'codigo': codigo,
                        'nome': nome,
                    }
                    lista.append(dict_dados)
                    print()
                    print(f'{nome_dados} incluida com sucesso.')
                    print()
                    escrever(lista, nome_arquivo)
                    inclusao_continuar = False
                # Caso o módulo TURMAS seja escolhido pelo usuário, o sistema irá conferir se o PROFESSOR e a DISCIPLINA já estão cadastrados em seus devidos módulos, e só então permitirá a inclusão da TURMA.
                elif opcao == '4':
                    verificar_professor = ler('professores.json')
                    verificar_disciplina = ler('disciplinas.json')
                    validar1 = False
                    validar2 = False

                    codigo_prof = int(input(f'Digite o código do PROFESSOR: '))
                    for dados in verificar_professor:
                        if dados['codigo'] == codigo_prof:
                            validar1 = True
                    if validar1 is False:
                        print('Não encontramos o código do PROFESSOR em nosso sistema, cadastre-o e tente novamente.')
                        print()
                        break

                    codigo_disc = int(input(f'Digite o código da DISCIPLINA: '))
                    for dados in verificar_disciplina:
                        if dados['codigo'] == codigo_disc:
                            validar2 = True

                    if validar2 is False:
                        print('Não encontramos o código da DISCIPLINA em nosso sistema, cadastre-o e tente novamente.')
                        print()
                        break

                    elif validar1 and validar2:
                        dict_dados = {
                            'codigo': codigo,
                            'professor': codigo_prof,
                            'disciplina': codigo_disc
                        }
                        lista.append(dict_dados)
                        print()
                        print(f'{nome_dados} incluida com sucesso.')
                        print()
                        escrever(lista, nome_arquivo)
                        inclusao_continuar = False
                # Caso o módulo MATRÍCULAS seja escolhido pelo usuário, o sistema irá conferir se o ESTUDANTE e a TURMA já estão cadastrados em seus devidos módulos, e só então permitirá a inclusão da MATRÍCULA.
                elif opcao == '5':
                    verificar_estudante = ler('estudantes.json')
                    verificar_turma = ler('turmas.json')
                    validar1 = False
                    validar2 = False

                    codigo_turma = int(input(f'Digite o código da TURMA: '))
                    for dados in verificar_turma:
                        if dados['codigo'] == codigo_turma:
                            validar1 = True
                    if validar1 is False:
                        print('Não encontramos o código da TURMA em nosso sistema, cadastre-o e tente novamente.')
                        print()
                        break

                    codigo_est = int(input(f'Digite o código do ESTUDANTE: '))
                    for dados in verificar_estudante:
                        if dados['codigo'] == codigo_est:
                            validar2 = True
                    if validar2 is False:
                        print('Não encontramos o código do ESTUDANTE em nosso sistema, cadastre-o e tente novamente.')
                        print()
                        break
                    # Caso os dados da TURMA e do ESTUDANTE sejam encontrados no sistema, combina ambos e realiza a inclusão da matrícula como um número inteiro.
                    elif validar1 and validar2:
                        matricula = str(codigo_turma) + str(codigo_est)
                        matricula_inteiro = int(matricula)
                        matricula_existe = False

                        for dados in lista:
                            if dados['codigo'] == matricula_inteiro:
                                print('A matrícula referente ao estudante do código digitado já esta cadastrada em nosso sistema.')
                                print()
                                matricula_existe = True
                                inclusao_continuar = False
                                break

                        if not matricula_existe:
                            dict_dados = {
                                'codigo': matricula_inteiro,
                                'estudante': codigo_est
                            }
                            lista.append(dict_dados)
                            print()
                            print(f'{nome_dados} incluida com sucesso.')
                            print()
                            escrever(lista, nome_arquivo)
                            inclusao_continuar = False

        except ValueError:
            print('Valor inválido, tente novamente.')
        except KeyError as i:
            print(f'Valor da chave {str(i)} não encontrado.')
        except Exception as i:
            print(f'Erro! Ocorreu um erro inesperado: {str(i)}')

def listagem(opcao,nome_arquivo,nome_menu):
    """
    Lê e exibe os dados do arquivo descrito para cada módulo quando a opção "2 - listar" for selecionada.

    :param opcao: Opção digitada pelo usuário no menu secundário.
    :param nome_arquivo: Nome do arquivo no qual os dados serão lidos e carregados.
    :param nome_menu: Denomina o menu de inclusão de acordo com o módulo escolhido.
    :return: Retorna o valor booleano "None" demonstrando que a função não retorna um valor útil.
    """
    lista = ler(nome_arquivo)
    print('==== LISTAGEM {} ==== '.format(nome_menu))
    if not lista:
        if opcao == '1':
            print(f'Não há cadastros de estudantes em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '2':
            print(f'Não há cadastros de professores em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '3':
            print(f'Não há cadastros de disciplinas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '4':
            print(f'Não há cadastros de turmas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '5':
            print(f'Não há cadastros de matrículas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
    else:
        if opcao == '1' or opcao == '2':
            for dados in lista:
                print('CÓDIGO: {} - NOME: {} - CPF: {}'.format(dados['codigo'], dados['nome'], dados['cpf']))
        elif opcao == '3':
            for dados in lista:
                print('CÓDIGO: {} - DISCIPLINA: {}'.format(dados['codigo'], dados['nome']))
        elif opcao == '4':
            for dados in lista:
                print('TURMA: {} - PROFESSOR: {} - DISCIPLINA {}'.format(dados['codigo'],dados['professor'],dados['disciplina']))
        elif opcao == '5':
            for dados in lista:
                print('MATRÍCULA Nº {} - ESTUDANTE: {}'.format(dados['codigo'],dados['estudante']))
        print()
    return None

def atualizar(opcao,nome_arquivo,nome_menu,nome_dados):
    """
    Recebe os dados do usuáro e realiza a edição/atualização dos dados cadastrados para todos os módulos.

    :param opcao: Opção digitada pelo usuário no menu secundário.
    :param nome_arquivo: Nome do arquivo no qual os dados serão lidos e gravados.
    :param nome_menu: Denomina o menu de atualização de acordo com o módulo escolhido.
    :param nome_dados: Exibe um nome de acordo com a opção selecionada previamente ['ESTUDANTE', 'PROFESSOR', 'DISCIPLINA', 'TURMA', 'MATRÍCULA'], para melhor compreensão do usuário.
    """
    lista = ler(nome_arquivo)
    print('==== ATUALIZAÇÃO {} ==== '.format(nome_menu))
    if not lista:
        if opcao == '1':
            print(
                f'Não há cadastros de estudantes em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '2':
            print(
                f'Não há cadastros de professores em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '3':
            print(
                f'Não há cadastros de disciplinas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '4':
            print(
                f'Não há cadastros de turmas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '5':
            print(
                f'Não há cadastros de matrículas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
    else:
        atualizacao = True
        atualizar = 0
        while atualizacao:
            try:
                if opcao in ['1', '2']:
                    atualizar = int(input(f'Digite o código do {nome_dados} que deseja editar: '))

                elif opcao in ['3', '4','5']:
                    atualizar = int(input(f'Digite o código da {nome_dados} que deseja editar: '))

                # Verifica se o código já está cadastrado no sistema para prosseguir com a alteração.
                encontrado = False
                for dados in lista:
                    if dados['codigo'] == atualizar:
                        encontrado = dados
                        break
                if encontrado is False:
                    while True:
                        if opcao in ['1','2']:
                            nao_encontrado = input(f'O {nome_dados} de código {atualizar} não esta cadastrado em nosso sistema, gostaria de tentar novamente? (s/n): ').lower()
                        else:
                            nao_encontrado = input(f'A {nome_dados} de código {atualizar} não esta cadastrada em nosso sistema, gostaria de tentar novamente? (s/n): ').lower()

                        if nao_encontrado != 's' and nao_encontrado != 'n':
                            print('Valor inválido, por favor digite "s" para SIM ou "n" para NÃO.')
                        elif nao_encontrado == 's':
                            atualizacao = True
                            break
                        elif nao_encontrado == 'n':
                            print()
                            atualizacao = False
                            break
                else:
                    if opcao == '1' or opcao == '2':
                        while True:
                            codigo_novo = int(input('Digite o código novo: '))
                            if verificar_codigo_existente(lista,codigo_novo,nome_dados,codigo_atual = atualizar):
                                encontrado['codigo'] = codigo_novo
                                encontrado['nome'] = input('Digite o nome atualizado: ')
                                encontrado['cpf'] = input('Digite o CPF atualizado: ')
                                print()
                                print('Dados atualizados com sucesso!')
                                print()
                                escrever(lista, nome_arquivo)
                                atualizacao = False
                                break
                    elif opcao == '3':
                        while True:
                            codigo_novo = int(input('Digite o código novo: '))
                            if verificar_codigo_existente(lista, codigo_novo,nome_dados,codigo_atual = atualizar):
                                encontrado['codigo'] = codigo_novo
                                encontrado['nome'] = input('Digite o nome atualizado: ')
                                print()
                                print('Dados atualizados com sucesso!')
                                print()
                                escrever(lista, nome_arquivo)
                                atualizacao = False
                                break
                    # Caso o módulo TURMAS seja escolhido pelo usuário, o sistema irá conferir se o PROFESSOR e a DISCIPLINA já estão cadastrados em seus devidos módulos, e só então permitirá a atualização da TURMA.
                    elif opcao == '4':
                        verificar_professor = ler('professores.json')
                        verificar_disciplina = ler('disciplinas.json')
                        validar1 = False
                        validar2 = False

                        continuar = True
                        while continuar:
                            codigo_novo = int(input('Digite o código novo: '))

                            if verificar_codigo_existente(lista, codigo_novo, nome_dados, codigo_atual=atualizar):
                                professor_novo = int(input('Digite o código do professor atualizado: '))
                                # Verifica se o PROFESSOR está cadastrado no sistema.
                                for dados in verificar_professor:
                                    if dados['codigo'] == professor_novo:
                                        validar1 = True
                                        break

                                if not validar1:
                                    print('Não encontramos o código do PROFESSOR em nosso sistema, cadastre-o e tente novamente.')
                                    print()
                                    continuar = False
                                    atualizacao = False
                                    break

                                disciplina_novo = int(input('Digite o código da disciplina atualizado: '))
                                # Verifica se a DISCIPLINA está cadastrada no sistema.
                                for dados in verificar_disciplina:
                                    if dados['codigo'] == disciplina_novo:
                                        validar2 = True
                                        break

                                if not validar2:
                                    print('Não encontramos o código da DISCIPLINA em nosso sistema, cadastre-a e tente novamente.')
                                    print()
                                    continuar = False
                                    atualizacao = False
                                    break

                                if validar1 and validar2:
                                    encontrado['codigo'] = codigo_novo
                                    encontrado['professor'] = professor_novo
                                    encontrado['disciplina'] = disciplina_novo
                                    print()
                                    print('Dados atualizados com sucesso!')
                                    print()
                                    escrever(lista, nome_arquivo)
                                    atualizacao = False
                                    break
                    # Caso o módulo MATRÍCULAS seja escolhido pelo usuário, o sistema irá conferir se o ESTUDANTE e a TURMA já estão cadastrados em seus devidos módulos, e só então permitirá a atualização da MATRÍCULA.
                    elif opcao == '5':
                        verificar_turma = ler('turmas.json')
                        verificar_estudante = ler('estudantes.json')
                        validar1 = False
                        validar2 = False

                        while True:
                            codigo_turma = int(input('Digite o código da turma atualizado: '))
                            # Verifica se a TURMA está cadastrada no sistema.
                            for dados in verificar_turma:
                                if dados['codigo'] == codigo_turma:
                                    validar1 = True
                                    break

                            if not validar1:
                                print('Não encontramos o código da TURMA em nosso sistema, cadastre-a e tente novamente.')
                                print()
                                continuar = False
                                atualizacao = False
                                break

                            codigo_estudante = int(input('Digite o código do estudante atualizado: '))
                            # Verifica se o ESTUDANTE está cadastrado no sistema.
                            for dados in verificar_estudante:
                                if dados['codigo'] == codigo_estudante:
                                    validar2 = True
                                    break

                            if not validar2:
                                print('Não encontramos o código do ESTUDANTE em nosso sistema, cadastre-o e tente novamente.')
                                print()
                                continuar = False
                                atualizacao = False
                                break

                            if validar1 and validar2:
                                matricula = str(codigo_turma) + str(codigo_estudante)
                                matricula_inteiro = int(matricula)
                                matricula_existe = False

                                for dados in lista:
                                    if dados['codigo'] == matricula_inteiro:
                                        print(f'A {nome_dados} de código {matricula_inteiro} já está cadastrada em nosso sistema, por favor tente novamente.')
                                        matricula_existe = True
                                        atualizacao = False
                                        break
                                if not matricula_existe:
                                    encontrado['codigo'] = matricula_inteiro
                                    encontrado['estudante'] = codigo_estudante
                                    print()
                                    print('Dados atualizados com sucesso!')
                                    print()
                                    escrever(lista, nome_arquivo)
                                    atualizacao = False
                                    break
            except ValueError:
                print('Valor inválido, tente novamente.')
            except KeyError as i:
                print(f'Valor da chave {str(i)} não encontrado.')
            except Exception as i:
                print(f'Erro! Ocorreu um erro inesperado: {str(i)}')

def exclusao(opcao,nome_arquivo,nome_menu,nome_dados):
    """
    Recebe os dados do usuáro e realiza a exclusão dos dados cadastrados para todos os módulos.

    :param opcao: Opção digitada pelo usuário no menu secundário.
    :param nome_arquivo: Nome do arquivo no qual os dados serão lidos e gravados.
    :param nome_menu: Denomina o menu de exclusão de acordo com o módulo escolhido.
    :param nome_dados: Exibe um nome de acordo com a opção selecionada previamente ['ESTUDANTE', 'PROFESSOR', 'DISCIPLINA', 'TURMA', 'MATRÍCULA'], para melhor compreensão do usuário.
    :return: Retorna o valor booleano "None" demonstrando que a função não retorna um valor útil.
    """
    lista = ler(nome_arquivo)
    print('==== EXCLUSÃO {} ==== '.format(nome_menu))
    if not lista:
        if opcao == '1':
            print(
                f'Não há cadastros de estudantes em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '2':
            print(
                f'Não há cadastros de professores em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '3':
            print(
                f'Não há cadastros de disciplinas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '4':
            print(
                f'Não há cadastros de turmas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
        elif opcao == '5':
            print(
                f'Não há cadastros de matrículas em nosso sistema. Para incluir selecione a opção [1] no menu operacional.')
            print()
    else:
        exclusao = True
        excluir = 0
        while exclusao:
            try:
                if opcao in ['1', '2']:
                    excluir = int(input(f'Digite o código do {nome_dados} que deseja excluir: '))

                elif opcao in ['3', '4','5']:
                    excluir = int(input(f'Digite o código da {nome_dados} que deseja excluir: '))

                encontrado = False
                for dados in lista:
                    if dados['codigo'] == excluir:
                        encontrado = dados
                        break

                if encontrado is False:
                    while True:
                        if opcao in ['1', '2']:
                            nao_encontrado = input(
                                f'O {nome_dados} de código {excluir} não esta cadastrado em nosso sistema, gostaria de tentar novamente? (s/n): ').lower()
                        else:
                            nao_encontrado = input(
                                f'A {nome_dados} de código {excluir} não esta cadastrada em nosso sistema, gostaria de tentar novamente? (s/n): ').lower()

                        if nao_encontrado != 's' and nao_encontrado != 'n':
                            print('Valor inválido, por favor digite "s" para SIM ou "n" para NÃO.')
                        elif nao_encontrado == 's':
                            exclusao = True
                            break
                        elif nao_encontrado == 'n':
                            print()
                            exclusao = False
                            break
                else:
                    lista.remove(encontrado)
                    print()
                    if opcao in ['1','2']:
                        print(f'{nome_dados} excluído com sucesso!')
                        print()
                    else:
                        print(f'{nome_dados} excluída com sucesso!')
                        print()
                    escrever(lista, nome_arquivo)
                    exclusao = False
            except ValueError:
                print('Valor inválido, tente novamente.')
            except KeyError as i:
                print(f'Valor da chave {str(i)} não encontrado.')
            except Exception as i:
                print(f'Erro! Ocorreu um erro inesperado: {str(i)}')
        return None

def realizar_operacao(opcao_principal,opcao_secundaria,nome_menu,nome_opcoes,nome_arquivo):
    """
    Recebe o valor inserido pelo usuário nos menus principal e seundário e realiza a chama a função a ser realizada de acordo com a opção escolhida.

    :param opcao_principal:
    :param opcao_secundaria:
    :param nome_menu:
    :param nome_opcoes:
    :param nome_arquivo:
    :return:
    """
    try:
      if opcao_principal in nome_arquivo:
          if opcao_secundaria == '1':
              inclusao(opcao_principal,nome_arquivo[opcao_principal],nome_menu_secundario,nome_opcoes)
          elif opcao_secundaria == '2':
              listagem(opcao_principal,nome_arquivo[opcao_principal],nome_menu_secundario)
          elif opcao_secundaria == '3':
              atualizar(opcao_principal,nome_arquivo[opcao_principal],nome_menu_secundario,nome_elementos_escolares)
          elif opcao_secundaria == '4':
              exclusao(opcao_principal,nome_arquivo[opcao_principal],nome_menu_secundario,nome_elementos_escolares)
    except KeyError as i:
        print(f'Valor da chave {str(i)} não encontrado.')
    except Exception as i:
        print(f'Erro! Ocorreu um erro inesperado: {str(i)}')

# Dicionário responsável por nomear os arquivos nos quais os dados serão armazenados.
nome_arquivos = {
        '1': 'estudantes.json',
        '2': 'professores.json',
        '3': 'disciplinas.json',
        '4': 'turmas.json',
        '5': 'matriculas.json'
    }

# Enquanto verdade, realiza a chamada de todas as funções, fazendo com que o sistema funcione propriamente.
while True:
    try:
        # Exibe o menu principal ao usuário e solicita que o usuário escolha uma das opções do menu principal.
        opcao1 = menu_principal()

        # Verifica se a informação inserida é válida (1,2,3,4 ou 5) e retorna qual ação o usuário deseja realizar.
        if opcao1 in ['1', '2', '3', '4', '5']:
            print('Você escolheu a opção [{}]. '.format(opcao1))
            print()
            nome_menu_secundario = ['[ESTUDANTES]', '[PROFESSORES]', '[DISCIPLINAS]', '[TURMAS]', '[MATRÍCULAS]'][int(opcao1) - 1]
            nome_elementos_escolares = ['ESTUDANTE', 'PROFESSOR', 'DISCIPLINA', 'TURMA', 'MATRÍCULA'][int(opcao1) - 1]

            # Exibe o menu operacional.
            while True:
                opcao2 = menu_secundario(nome_menu_secundario)

                # Verifica se a informação inserida é válida (1,2,3,4 ou 0) e retorna qual ação o usuário digitou.
                if opcao2 in ['1', '2', '3', '4']:
                    print(f'Você escolheu a opção [{opcao2}].')
                    print()
                # Realiza as INCLUSÕES para todas as oções do menu principal.
                    realizar_operacao(opcao1,opcao2,nome_menu_secundario,nome_elementos_escolares,nome_arquivos)

                # Informa e refireciona o usuário ao MENU PRINCIPAL, caso a opção (0) seja escolhida.
                elif opcao2 == '0':
                    print('Voltando ao MENU PRINCIPAL...')
                    print()
                    break

                # Caso uma opção inválida seja digitada, exibe a mensagem ao usuário.
                else:
                    print('Você digitou uma opção INVÁLIDA, por favor tente novamente.')
                    print()
        # Verifica e finaliza o programa caso a condição abaixo seja verdadeira.
        elif opcao1 == '0':
            print('Você escolheu a opção [SAIR], até breve.')
            break

        # Caso uma opção inválida seja digitada, exibe a mensagem ao usuário.
        else:
            print('Você digitou uma opção INVÁLIDA.')
            print()

    except ValueError:
        print('Você digitou uma opção INVÁLIDA, por favor tente novamente!')
    except Exception as i:
        print(f'Erro! Ocorreu um erro inesperado: {str(i)}')

"""Ultima atualização 02/12/2024"""