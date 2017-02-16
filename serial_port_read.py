# -*- coding: latin1 -*-
# Códido para ler a porta serial e fazer um log em txt
# do que foi feito no arduino
def arduino():
    import serial
    import sys
    import time



    port = '/dev/ttyACM0' 					#configuração da serial
    baud_rate = 9600
    ser = serial.Serial (port, baud_rate) 	# Abrindo a porta
    temp_1= open('arquivo.txt','w')			# Cria um aquivo.txt

    print"========================================================"
    print"============ DIGITE 1 PARA TENSAO ======================"
    print"============ DIGITE 2 PARA VALOR ======================="
    print"============ DIGITE 3  PARA BUGAR ======================"
    print"========================================================"

    while True:
        while True:
            try:
                number = int(raw_input("Por favor, informe um numero: "))
                if number == 2 or number == 1:
                    break
                else:
                    raise ValueError
            except ValueError:
                print "Oops!  Nao foi um numero valido.  Tente novamente "
                print"========================================================"
                print"============ DIGITE 1 PARA TENSAO ======================"
                print"============ DIGITE 2 PARA VALOR ======================="
                print"============ DIGITE 3  PARA BUGAR ======================"
                print"========================================================"
        #number = raw_input("digite 1 para ligar \ndigite 2 para desligar\n")
        ser = serial.Serial (port, baud_rate)

        ser.write(str(number))					# escrevendo na Serial

        
        resposta = ser.readline()			#ler uma linha da string na serial
        print ("Arduíno disse: %s"%resposta)# escreve o log no console
        ser.close()							# Fechando a Serial
       	
        temp_1= open('arquivo.txt','r')		# abre o aquivo texto em modo leitura
        temp_2 = temp_1.readlines()			# Armazena todo o texto em forma de uma única string 
        temp_2.append("Arduíno disse: %s"%resposta) # adciona o log no final do arquivo texto
        temp_1 = open('arquivo.txt','w') 	# abre o Aquivo texto em modo escrita
        temp_1.writelines(temp_2) 			# Escreve o log atualizado no arquivo texto
        temp_1.close() 						#fecha o arquivo texto
