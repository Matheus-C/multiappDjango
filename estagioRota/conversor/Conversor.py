def conv(romano):# função que verifica e converte o número romano que foi dado na entrada
    valid = True

    arab = []# lista de números arábicos
    for i in range(len(romano)):
        if not valid:# se valid for False encerra o loop
            break
        if romano[i] == 'I' or romano[i] == 'i':
            arab.append(1)
        elif romano[i] == 'V' or romano[i] == 'v':
            arab.append(5)
        elif romano[i] == 'X' or romano[i] == 'x':
            arab.append(10)
        elif romano[i] == 'L' or romano[i] == 'l':
            arab.append(50)
        elif romano[i] == 'C' or romano[i] == 'c':
            arab.append(100)
        elif romano[i] == 'D' or romano[i] == 'd':
            arab.append(500)
        elif romano[i] == 'M' or romano[i] == 'm':
            arab.append(1000)
        else:# se existir algum caractere na entrada que não seja válido 
            valid = False

    for i in range(len(arab)-1, -1, -1):# verifica as posições dos algarismos romanos verifica se são válidos, se não interrompe
        if valid == False:
            break
        if i != 0:
            if arab[i] > arab[i-1]:
                if arab[i] == 5:
                    if arab[i-1] != 1:
                        valid = False
                if arab[i] == 10:
                    if arab[i-1] != 1:
                        valid = False
                if arab[i] == 50:
                    if arab[i-1] != 10:
                        valid = False
                if arab[i] == 100:
                    if arab[i-1] != 10:
                        valid = False
                if arab[i] == 500:
                    if arab[i-1] != 100:
                        valid = False
                if arab[i] == 1000:
                    if arab[i-1] != 100:
                        valid = False

    if valid:
        result = 0
        ignore = False
        for i in range(len(arab)-1, -1, -1):
            if not ignore:
                if i != 0:# soma e subtrai os algarismos baseado na localização dos mesmos
                    if arab[i] > arab[i-1]:
                        result = result + (arab[i] - arab[i-1])
                        ignore = True
                    else:
                        result = result + arab[i]
                else:
                    result = result + arab[i]
            else:
                ignore = False

        return result
    else:
        return "entrada inválida"