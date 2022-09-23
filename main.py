from acess_api_suap import Api_suap

acess_token = "AON3dxIssJFn"

if __name__ == '__main__' :
    suap = Api_suap(token=acess_token,type_token="Bearer")
    while True:
        try:
            op = suap.menu_principal()
            if op == "1":
                suap.api_eu()
            elif op == "2":
                suap.api_meus_dados()
            elif op == "3":
                suap.api_priodos_letivos()
            elif op == "4":
                ano = input("digite o ano letivo:")
                periodo = input("digite o periodo:")
                suap.api_boletim(ano,periodo)
            elif op == "5":
                suap.campi()
            elif op == "6":
                break
        except KeyboardInterrupt:
            print("\nFinalizando.")
            break
        except Exception as ex:
            print(f"error {ex}")