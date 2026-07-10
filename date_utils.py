from datetime import datetime


def normalizar_data(data_texto):
    data_texto = str(data_texto or "").strip()
    if data_texto.isdigit() and len(data_texto) == 8:
        return f"{data_texto[:2]}/{data_texto[2:4]}/{data_texto[4:]}"
    return data_texto


def parse_data(data_texto):
    return datetime.strptime(normalizar_data(data_texto), "%d/%m/%Y").date()
