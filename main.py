import FreeSimpleGUI as sg
from controlador_principal import ControladorPrincipal

def main():
    try:
        controlador = ControladorPrincipal()
        controlador.iniciar_sistema()
    except Exception as e:
        sg.Popup(f"Erro fatal no sistema: {e}", title="Erro")

if __name__ == "__main__":
    main()