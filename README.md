# Sistema Hospitalario

Este proyecto simula el flujo de pacientes en un sistema hospitalario automatizado usando programación concurrente y paralela. 
El sistema modela eventos reales como el registro, diagnóstico mediante IA, asignación de recursos limitados (doctores y camas), y el proceso de alta médica.

## Requisitos

dirigase al archivo requirements.txt para saber más al respecto.

## Instalación

1. Clona el repositorio.
2. Ejecuta `npm install` para instalar las dependencias.
3. Configura las variables de entorno en el archivo `.env`.
4. Ejecuta `npm start` para iniciar la aplicación.

## Uso

La simulación crea varios pacientes que pasan por estas etapas:

1. Registro: Se colocan en una cola común.
2. Diagnóstico: Se usa un modelo de IA preentrenado (distilbert-base-uncased-finetuned-sst-2-english) para evaluar síntomas.
3. Asignación de recursos:
    - Pacientes **críticos** reciben atención prioritaria.
    - Pacientes **estables** esperan hasta que no haya pacientes críticos.
4. Seguimiento y alta: Se simula su recuperación y salida del hospital.

## Ejemplo de Salida Espereda

Paciente 0 registrándose...
Paciente 0 diagnosticado como CRÍTICO.
Paciente 0 recibió doctor y cama.
Paciente 0 ha sido dado de alta.

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios necesarios y realiza commits (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube los cambios a tu repositorio remoto (`git push origin feature/nueva-funcionalidad`).
5. Abre un pull request en este repositorio.

## Licencia

Indica la licencia bajo la cual se distribuye tu proyecto.

