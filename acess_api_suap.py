from mensagens import Respostas
import requests
import json

class Api_suap(Respostas):
    def __init__(self,token=None,type_token="Bearer"):
        self.token = token
        self.type_token = type_token

    def api_eu(self):  # 100% funcional
        payload =  {"access_token":self.token,"token_type":self.type_token}
        r = requests.get("https://suap.ifrn.edu.br/api/eu/", params=payload)
        if r.status_code == 200:
            self.mostrar_eu(json.loads(r.content))
        else:
            print(f"error, verifique o token codigo HTTP {r.status_code}")
      

    def api_meus_dados(self):  # 100% funcional
        payload =  {"access_token":self.token,"token_type":self.type_token}
        r = requests.get("https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/", params=payload)
        if r.status_code == 200:
            self.meus_dados(json.loads(r.content))
        else:
            print(f"error, verifique o token codigo HTTP {r.status_code}")

    def api_participacao_projetos(self): 
        payload =  {"access_token":self.token,"token_type":self.type_token}
        r = requests.get("https://suap.ifrn.edu.br/api/v2/minhas-informacoes/participacoes-projetos/", params=payload)
        print(r.url)
        print(r.status_code)
        print(r.content)

    
    def api_boletim(self, ano_letivo, periodo_letivo): # 100% funcional
        payload =  {"access_token":self.token,"token_type":self.type_token}
        r = requests.get(f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/", params=payload)
        if r.status_code == 200:
            self.show_disciplinas(json.loads(r.content))
        else:
            print(f"error, verifique o token codigo HTTP {r.status_code}")

    def  api_priodos_letivos(self): # 100% funcional
        payload =  {"access_token":self.token,"token_type":self.type_token}
        r = requests.get(f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-periodos-letivos/", params=payload)
        if r.status_code == 200:
            self.periodos_letivos(json.loads(r.content))
        else:
            print(f"error, verifique o token codigo HTTP {r.status_code}")
        
    def campi(self): # 100% funcional
        payload =  {"access_token":self.token,"token_type":self.type_token}
        r = requests.get(f"https://suap.ifrn.edu.br/api/campi", params=payload)
        if r.status_code == 200:
            self.show_campis(json.loads(r.content))
        else:
            print(f"error, verifique o token codigo HTTP {r.status_code}")
   
    def api_dados_servidor(self):
        payload =  {"access_token":self.token,"token_type":self.type_token}
        r = requests.get(f"https://suap.ifrn.edu.br/edu/api/dados_servidor/", params=payload)
        print(r.url)
        print(r.status_code)
        print(r.content)

