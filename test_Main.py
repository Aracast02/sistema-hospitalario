import unittest
from queue import Queue

from Main import main, Paciente, AsignadorRecursos

class TestMain(unittest.TestCase):
    def test_main(self):
        cola_registro = Queue()
        cola_diagnostico = Queue()
        cola_criticos = Queue()
        cola_estables = Queue()

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


if __name__ == '__main__':
    unittest.main()