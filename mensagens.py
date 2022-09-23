
class Respostas():
    def show_disciplinas(self,dados):
        def menu(dados,posicao):
                    print("-"*50)
                    print("disciplina:",dados[posicao]["disciplina"])
                    print('codigo_diario:',dados[posicao]['codigo_diario'])
                    print("carga_horaria:",dados[posicao]["carga_horaria"])
                    print("carga_horaria_cumprida:",dados[posicao]["carga_horaria_cumprida"])
                    print("percentual_carga_horaria_frequentada:",dados[posicao]["percentual_carga_horaria_frequentada"])
                    print("numero_faltas:",dados[posicao]["numero_faltas"])
                    print("situação:",dados[posicao]["situacao"])
                    print("nota 1ºbimestre:",dados[posicao]["nota_etapa_1"]["nota"]," faltas:",dados[posicao]["nota_etapa_1"]["faltas"])
                    print("nota 2ºbimestre:",dados[posicao]["nota_etapa_1"]["nota"]," faltas:",dados[posicao]["nota_etapa_2"]["faltas"])
                    print("nota_avaliação_final:",dados[posicao]["nota_avaliacao_final"]["nota"]," faltas:",dados[posicao]["nota_avaliacao_final"]["nota"])
                    print("media_final_disciplita:",dados[posicao]["media_final_disciplina"])
                    print("media_disciplina:",dados[posicao]["media_disciplina"])
                    print("-"*50)        
        try:
            [ print( f"[ {i} ]", dados[i]['disciplina'] ) for i in range(len(dados)) ]
            print(f"[ {len(dados)} ]para lista todas digite all")
            var = input("qual disciplina deseja visualizar :")
            [menu(dados,i) for i in range(len(dados))] if int(var) == len(dados) else menu(dados,int(var))       
        except Exception as ex:
            print(f"um erro aconteceu, tente novamente!  error:{ex}")

    def show_campis(self,dados):
        def menu(dados,i):
            print(f"{'-':->15}",dados['results'][i]['nome'],f"{'-':-<15}")
            print("Nome:",f"{'':.<5}",dados['results'][i]['nome'],"| sigla:",dados['results'][i]['sigla'])
            print("endereço:",f"{'':.<1}",dados['results'][i]['endereco'])
            print("cep",f"{'':.<7}",dados['results'][i]['cep'])
            print("telefone",f"{'':.<1}",dados['results'][i]['telefone'])
            print("fax",f"{'':.<7}",dados['results'][i]['fax'])
            print("-"*50)
        try:
            [print(f"[ {i:<2} ]",dados['results'][i]['nome']) for i in range(len(dados['results']))]
            print(f"[ {len(dados['results'])} ] para lista todos.")
            var = int(input("qual disciplina deseja visualizar:"))
            [menu(dados,i) for i in range(len(dados['results']))] if var == len(dados['results']) else menu(dados,int(var))    
        except Exception as ex:
            print(f"um erro aconteceu, tente novamente!,  erro:{ex}")    

    def periodos_letivos(self,dados):
        print("------seus periodos letivos------")
        [print("| Ano:",i['ano_letivo'],"| periodo letivo:",i['periodo_letivo'],"|") for i in dados]
        print("-"*34)

    def mostrar_eu(self,dados):
        print("-"*60)
        print('identificacao/matricula:',dados['identificacao'])
        print('nome:',dados['nome'],'| campus:',dados['campus'])
        print('email:',dados['email_secundario'])
        print('email_escolar:',dados['email_google_classroom'])
        print('email_academico:',dados['email_academico'])
        print("-"*60)
    
    def meus_dados(self,dados):
        print("-"*16,"Meus dados","-"*16)
        print('matricula:',dados['matricula'],' | id:',dados['id'])
        print('nome_usual:',dados['nome_usual'])
        print('cpf:',dados['cpf'],'| rg:',dados['rg'])
        print('data_nascimento:',dados['data_nascimento'])
        print('naturalidade:',dados['naturalidade'])
        print('tipo_sanguineo:',dados['tipo_sanguineo'])
        print('email:',dados['email'])
        print('filiacao:',dados['filiacao'])
        print('tipo_vinculo:',dados['tipo_vinculo'])
        print("-"*16,"DADOS DO VINCULO:",dados['tipo_vinculo'],"-"*10)
        print('situacao_sistemica:',dados['vinculo']['situacao_sistemica'])
        print('curso:',dados['vinculo']['curso'])
        print('matricula:',dados['vinculo']['matricula'])
        print('nome:',dados['vinculo']['nome'])
        print('curriculo_lattes:',dados['vinculo']['curriculo_lattes'])
        print('situacao:',dados['vinculo']['situacao'],'| campus:',dados['vinculo']['campus'])
        print('matricula_regular:',dados['vinculo']['matricula_regular'])
        print('cota_sistec:',dados['vinculo']['cota_sistec'])
        print('cota_mec:',dados['vinculo']['cota_mec'])
        print('linha_pesquisa:',dados['vinculo']['linha_pesquisa'])
        print("-"*50)

    def primeiro_acesso(self,dados):
        for i in dados.keys():
             print(f"{i}: {dados[i]}")

    def menu_principal(self):
        menu = input("""----------------------- Menu Principal --------------
[1] - api/eu [resumo de informações simples sobre o user]
[2] - meus dados [ informações mais completas sobre o user ]
[3] - meus periodo letivo [ informa ano e peridos letivos do user]
[4] - Boletins [ informa boletim de um ano_letivo e periodo escolhido pelo user]
[5] - campus [ informações dos campus (endereço,numero)]
[6] - sair
Digite sua escolha:""")
        return menu