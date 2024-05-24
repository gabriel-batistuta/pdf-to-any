import inquirer

def menu():
    options = [
        inquirer.List('option',
        message='Pra qual formato de arquivo deseja converter?',
        choices=['html', '.txt', 'xml', 'Sair'])
    ]

    response = inquirer.prompt(options)

    match(response):
        case 'html':
            resp = 'html'
        case 'txt':
            resp = 'txt'
        case 'xml':
            resp = 'xml'
        case 'Sair':
            quit()

    return resp