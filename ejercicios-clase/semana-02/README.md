# Laboratorio 02 — Configuración del entorno de trabajo

## Entorno virtual

El entorno virtual se creó con `python -m venv venv` dentro de `ejercicios-clase/semana-02/`.
En Windows PowerShell se activó mediante `.\venv\Scripts\Activate.ps1` y se verificó el prefijo `(venv)`.
La carpeta `venv/` se encuentra incluida en `.gitignore` para evitar versionarla en Git.

## Dependencias

Se instaló `matplotlib` con `pip install matplotlib`.
Las dependencias del entorno se registraron mediante `pip freeze > requirements.txt`.
Para reproducir el entorno, se debe crear y activar un nuevo `venv` y ejecutar `pip install -r requirements.txt`.

## Ejecución

Los scripts del laboratorio se ejecutan con `python refactor_pep8.py` y `python clasificador_anios.py`.
