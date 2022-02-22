logger_user = False
idade = 17
e_de_maior = (idade >= 18)

msg1 = 'Usuario Logado. ' if logger_user else 'Usuario precisa logar'
msg2 = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    
print(msg1)
print(msg2)