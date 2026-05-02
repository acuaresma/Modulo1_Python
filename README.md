# Proyecto 1 – Python Fundamentals

Aplicación interactiva desarrollada en **Streamlit** como parte del Módulo 1 de la **Especialización en Python for Analytics**.

## 👤 Información del estudiante

- **Nombre:** Angel Eduardo Cuaresma Tineo
- **Módulo:** Módulo 1 – Python Fundamentals
- **Año:** 2026

## 📝 Descripción

Esta aplicación integra los conceptos fundamentales de Python aprendidos durante el módulo: variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO). Todo dentro de una interfaz interactiva construida con Streamlit.

## 🧩 Estructura de la aplicación

La app cuenta con un menú lateral (`st.sidebar.selectbox`) con las siguientes secciones:

- **Home:** presentación del proyecto y datos del estudiante.
- **Ejercicio 1 – Flujo de caja con listas:** registro de movimientos financieros (ingresos/gastos) usando listas, con cálculo de saldo final.
- **Ejercicio 2 – Registro con NumPy y DataFrame:** formulario para registrar productos, almacenamiento en arrays de NumPy y visualización en un DataFrame.
- **Ejercicio 3 – Función externa (Calculadora de IMC):** uso de la función `calcular_imc` desde una librería externa, con histórico de resultados.
- **Ejercicio 4 – CRUD con clase Empleado:** uso de la clase `Empleado` desde una librería externa, implementando operaciones Crear, Leer, Actualizar y Eliminar.

## 🛠️ Tecnologías utilizadas

- Python 3
- Streamlit
- NumPy
- Pandas

## 🚀 Cómo ejecutar la aplicación localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/TU-USUARIO/proyecto1-python-fundamentals.git
   cd proyecto1-python-fundamentals
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## 📂 Estructura del repositorio

```
proyecto1-python-fundamentals/
│
├── app.py                              # Aplicación principal
├── libreria_funciones_proyecto1.py     # Librería de funciones externas
├── libreria_clases_proyecto1.py        # Librería de clases externas
├── requirements.txt                    # Dependencias del proyecto
└── README.md                           # Este archivo
```

## 🌐 Demo

La aplicación está desplegada en Streamlit Cloud:
👉 *(Aquí irá el enlace una vez desplegada)*

---

*Proyecto desarrollado como parte de la Especialización en Python for Analytics – DMC Institute.*
