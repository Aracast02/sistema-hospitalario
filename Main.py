from paciente import Paciente
from Recursos import AsignadorRecursos
import threading
import queue

def main():
    cola_registro = queue.Queue()
    cola_diagnostico = queue.Queue()
    cola_criticos = queue.Queue()
    cola_estables = queue.Queue()

    asignador_recursos = AsignadorRecursos(doctores=3, camas=2)

    pacientes = [Paciente(id_paciente=i,
                          cola_registro=cola_registro,
                          cola_diagnostico=cola_diagnostico,
                          cola_criticos=cola_criticos,
                          cola_estables=cola_estables,
                          asignador_recursos=asignador_recursos) for i in range(10)]

    for paciente in pacientes:
        paciente.start()

    for paciente in pacientes:
        paciente.join()

if __name__ == "__main__":
    main()
