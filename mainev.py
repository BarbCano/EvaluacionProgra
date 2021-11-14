
import EVPROJECT as mainev

nombreGerente = input('Ingrese nombre del gerente\n')
gerenton = mainev.Gerente(nombreGerente, 1.80, 'Formal', 'KStore', 'Gerente de surcursal')
gerenton.saludar()
gerenton.entrevistar('Andrea')
