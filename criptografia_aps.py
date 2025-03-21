def fix_characters(acceptables, warning, character_amount, boolean):
    message = input(f"{warning}: ")
    while all(c in acceptables for c in message) == False or (len(message) == character_amount) == boolean:
        message = input(f"A mensagem possui caracteres inválidos, aqui estão os caracteres aceitaveis: {acceptables}\nDigite novamente a sua mensagem: ")
    return message

def replace_character(message_to_check, message_characters, characters_to_replace, order_to_move):
    new_message = ''
    i = 0
    while i < len(message_to_check):
        l = 0
        while l < len(message_characters):
            if message_to_check[i] == message_characters[l]:
                j = (l + i * order_to_move) % len(characters_to_replace)
                new_message += characters_to_replace[j]
                break
            l += 1
        i += 1
    return new_message

acceptable_characters = [
    'a', 'á', 'à', 'â', 'ã', 'ä', 'b', 'c', 'ç', 'd', 'e', 'é', 'è', 'ê', 'ë', 'f',
    'g', 'h', 'i', 'í', 'ì', 'î', 'ï', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'ó', 'ò',
    'ô', 'õ', 'ö', 'p', 'q', 'r', 's', 't', 'u', 'ú', 'ù', 'û', 'ü', 'v', 'w', 'x',
    'y', 'ý', 'ÿ', 'z', 'A', 'Á', 'À', 'Â', 'Ã', 'Ä', 'B', 'C', 'Ç', 'D', 'E', 'É',
    'È', 'Ê', 'Ë', 'F', 'G', 'H', 'I', 'Í', 'Ì', 'Î', 'Ï', 'J', 'K', 'L', 'M', 'N',
    'Ñ', 'O', 'Ó', 'Ò', 'Ô', 'Õ', 'Ö', 'P', 'Q', 'R', 'S', 'T', 'U', 'Ú', 'Ù', 'Û',
    'Ü', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ',', '.', '!', '?', ';', ':', ' ']

special_characters = [
    ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%',
    '¨', '&', 'E', '(', ')', '-', '_', '¹', '²', '³', '£', '¢', '¬', '§', '=', '+',
    'U', '*', '/', '?', '´', '`', '[', '{', 'ª', '~', '^', ']', '}', ',', '<', '.',
    '>', ';', ':', '|', 'ë', 'Ë', 'ü', 'Ü', 'ï', 'Ï', 'ö', 'Ö', 'ä', 'Ä', 'ç', 'Ç',
    '₢', 'º', 'q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F',
    'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '"', "'", 'â', 'ê',
    'î', 'ô', 'û', 'ã', 'õ', 'á', 'é']

archive = open('message.txt')
options = ''
user_message = ''
message_to_encrypt = []
while True:
    options = fix_characters('''
0
1
2
3''', '''
Digite
> 0 para parar o programa
> 1 para escrever uma mensagem
> 2 para criptografar a mensagem
> 3 para descriptografar a atual mensagem\n''', 1, False)
    if options == '0':
        break
    if options == '1':
        user_message = fix_characters(acceptable_characters, 'Digite aqui a sua mensagem', 0, True)
        message_to_encrypt += list(user_message)
        message_to_encrypt.append(';')
        message_to_encrypt.append(' ')
        user_message = ''
    if options == '2':
        archive = open('message.txt', 'w')
        encrypted_message = ''
        if message_to_encrypt == []:
            print('Você não tem mensagem para criptografar, volte e digite alguma mensagem')
            continue
        else:
            encrypted_message = replace_character(message_to_encrypt, acceptable_characters, special_characters, 1)
            archive.write(encrypted_message)
            print(encrypted_message)
            archive.close()
            message_to_encrypt = []
    if options == '3':
        archive = open('message.txt', 'r')
        if archive.read() == '':
            print('Você não tem mensagens para descriptografar, por favor, volte e digite alguma mensagem')
        else:
            message_to_decrypt = str(open('message.txt', 'r').read())
            user_message = replace_character(message_to_decrypt, special_characters, acceptable_characters, -1)
            archive = open('message.txt', 'w')
            archive.close()
            print(user_message)