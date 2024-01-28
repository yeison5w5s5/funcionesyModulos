from .validate import opcNo
def Cont():
    while True:
        opc= int(input("\n\t Quieres Continuar? \n\t     1-Si\n\t     0-No\n\t -"))
        match(opc):
            case(1):
                return True
                break   
            case(0):
                return False
                break
            case(_):
                opcNo()