def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica de origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum dígito nemérico"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua número neste campo'


def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se data de ida é maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de ida não pode ser maior que data de volta'
