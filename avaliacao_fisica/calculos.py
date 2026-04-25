def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def calcular_rcq(cintura, quadril):
    rcq = cintura / quadril
    return rcq

def calcular_densidade(soma, idade, sexo):
    if sexo =='M':
        densidade = 1.112 - (0.00043499 * soma) + (0.00000055 * (soma**2)) - (0.00028826 * idade)
    else:        densidade = 1.097 - (0.00046971 * soma) + (0.00000056 * (soma**2)) - (0.00012828 * idade)
    return densidade

def calcular_gordura(densidade):
    gordura = ((4.95 / densidade) - 4.5) * 100
    return gordura

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif  imc < 25.0:
        return "Peso normal"
    elif  imc < 30.0:
        return "Sobrepeso"
    elif  imc < 35.0:
        return "Obesidade I"
    elif  imc < 40.0:
        return "Obesidade II"
    else:
        return "Obesidade III"
    
def classificar_rcq(rcq, sexo):
    if sexo == 'M':
        if rcq < 0.90:
            return 'Baixo' 
        elif rcq < 0.95:
            return 'Moderado'
        elif rcq < 1.00:
            return 'Alto'
        else:
            return 'Muito Alto'
    else:
        if  rcq < 0.80:
            return 'Baixo'
        elif rcq < 0.85:
            return 'Moderado'
        elif rcq < 0.90:
            return 'Alto'
        else:
            return 'Muito Alto'
            
def classificar_gordura(gordura, sexo, idade):
    if sexo =='M':
        if idade <= 29:
            if gordura < 11:
                return 'Excelente'
            elif gordura < 13:
                return 'Muito Bom'
            elif gordura < 16:
                return 'Bom'
            elif gordura < 20:
                return 'Razoavel'
            elif gordura < 24:
                return 'Ruim'
            else:                
                return 'Muito Ruim'
        elif idade <= 39:
            if gordura < 13:
                return 'Excelente'
            elif gordura <15:
                return 'Muito Bom'
            elif gordura <18:
                return 'Bom'
            elif gordura <22:
                return 'Razoavel'
            elif gordura <26:
                return 'Ruim'
            else:
                return 'Muito Ruim'
        elif idade <= 49:
            if gordura < 15:
                return 'Excelente'
            elif gordura < 17:
                return 'Muito Bom'
            elif gordura <20:
                return 'Bom'
            elif gordura <24:
                return 'Razoavel'
            elif gordura <28:
                return 'Ruim'
            else:
                return 'Muito Ruim'
        elif idade >= 50:
            if gordura <17:
                return 'Excelente'
            elif gordura <19:
                return 'Muito Bom'
            elif gordura <22:
                return 'Bom'
            elif gordura <26:
                return 'Razoavel'
            elif gordura <30:
                return 'Ruim'
            else:
                return 'Muito Ruim'
    else:   
        if idade <= 29:
            if gordura < 16:
                return 'Excelente'
            elif gordura < 19:
                return 'Muito Bom'
            elif gordura < 22:
                return 'Bom'
            elif gordura < 27:
                return 'Razoavel'
            elif gordura < 32:
                return 'Ruim'
            else:
                return 'Muito Ruim'
        elif idade <= 39:
            if gordura < 17:
                return 'Excelente'
            elif gordura < 21:
                return 'Muito Bom'
            elif gordura < 24:
                return 'Bom'
            elif gordura < 29:
                return 'Razoavel'
            elif gordura <34:
                return 'Ruim'
            else:
                return 'Muito Ruim'
        elif idade <= 49:
            if gordura < 19:
                return 'Excelente'
            elif gordura < 23:
                return 'Muito Bom'
            elif gordura < 26:
                return 'Bom'
            elif gordura < 31:
                return 'Razoavel'
            elif gordura < 36:
                return 'Ruim' 
            else:
                return 'Muito Ruim'
        elif idade >= 50:
            if gordura < 21:
                return 'Excelente'
            elif gordura < 25:
                return 'Muito Bom'
            elif gordura < 29:
                return 'Bom'
            elif gordura < 33:
                return 'Razoavel'
            elif gordura < 38:
                return 'Ruim'
            else: 
                return 'Muito Ruim'
