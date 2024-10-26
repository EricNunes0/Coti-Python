from modelo.medico import Medico
from modelo.paciente import Paciente

if __name__ == '__main__':
    med1 = Medico("Alberto", "Cardiologista")
    med2 = Medico("Ana", "Pediatra")
    med3 = Medico("Roberto", "Ortopedista")

    pac1 = Paciente("Isabella", "F", 24)
    pac2 = Paciente("Gabriel", "M", 20)
    pac3 = Paciente("Nathan", "M", 21)
    pac4 = Paciente("Assíria", "F", 19)

    # Relacionamento
    med1.pacientes = [pac1, pac4]
    med2.pacientes = [pac3]
    med3.pacientes = [pac1, pac2, pac3, pac4]

    pac1.medicos = [med1, med3]
    pac2.medicos = [med3]
    pac3.medicos = [med2, med3]
    pac4.medicos = [med1, med3]

    # Lista de médicsos
    medicos = [med1, med2, med3]
    for medico in medicos:
        print(medico)
        for i, paciente in enumerate(medico.pacientes):
            print(f'{i+1}º Paciente: {paciente}')
        print("\n")
    pass