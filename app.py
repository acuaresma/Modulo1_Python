import streamlit as st
import numpy as np
import pandas as pd
from libreria_funciones_proyecto1 import calcular_imc
from libreria_clases_proyecto1 import Empleado

# ─────────────────────────────────────────
# Configuración de la página
# ─────────────────────────────────────────
st.set_page_config(page_title="Proyecto 1 - Python Fundamentals", layout="centered")

# Menú lateral
pagina = st.sidebar.selectbox(
    "Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ─────────────────────────────────────────
# HOME
# ─────────────────────────────────────────
if pagina == "Home":
    st.title("📘 Proyecto 1 – Python Fundamentals")
    st.subheader("Especialización en Python for Analytics")

    st.markdown("---")

    st.write("**Nombre del estudiante:** Angel Eduardo Cuaresma Tineo")
    st.write("**Módulo:** Módulo 1 – Python Fundamentals")
    st.write("**Año:** 2026")

    st.markdown("---")

    st.markdown("### 📝 Descripción del proyecto")
    st.write(
        "Esta aplicación fue desarrollada como parte del Proyecto 1 del Módulo 1. "
        "Integra conceptos básicos de Python como listas, NumPy, funciones y clases "
        "dentro de una interfaz interactiva hecha con Streamlit."
    )

    st.markdown("### 🛠️ Tecnologías utilizadas")
    st.write("- Python")
    st.write("- Streamlit")
    st.write("- NumPy")
    st.write("- Pandas")

# ─────────────────────────────────────────
# EJERCICIO 1 – Flujo de caja con listas
# ─────────────────────────────────────────
elif pagina == "Ejercicio 1":
    st.title("Ejercicio 1 – Flujo de Caja")

    st.markdown("""
    En este ejercicio se registran movimientos financieros (ingresos y gastos)
    en una lista. Al final se calcula el saldo y se indica si el flujo está a favor o en contra.
    """)

    # Inicializar lista en session_state
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    st.markdown("### Agregar movimiento")

    concepto = st.text_input("Concepto", placeholder="Ej: Pago de arriendo")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=1.0)

    if st.button("➕ Agregar movimiento"):
        if concepto.strip() == "":
            st.error("Por favor escribe un concepto.")
        elif valor <= 0:
            st.error("El valor debe ser mayor a 0.")
        else:
            st.session_state.movimientos.append({
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            })
            st.success(f"Movimiento '{concepto}' agregado correctamente.")

    st.markdown("---")

    if len(st.session_state.movimientos) > 0:
        st.markdown("### Lista de movimientos")
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df, use_container_width=True)

        total_ingresos = sum(
            m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso"
        )
        total_gastos = sum(
            m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto"
        )
        saldo = total_ingresos - total_gastos

        st.markdown("### Resumen")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Ingresos", f"${total_ingresos:,.2f}")
        col2.metric("Total Gastos", f"${total_gastos:,.2f}")
        col3.metric("Saldo Final", f"${saldo:,.2f}")

        if saldo >= 0:
            st.success("✅ El flujo de caja está a FAVOR.")
        else:
            st.error("❌ El flujo de caja está en CONTRA.")

        if st.button("🗑️ Limpiar movimientos"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("Todavía no hay movimientos registrados.")

# ─────────────────────────────────────────
# EJERCICIO 2 – Registro con NumPy y DataFrame
# ─────────────────────────────────────────
elif pagina == "Ejercicio 2":
    st.title("Ejercicio 2 – Registro de Productos con NumPy")

    st.markdown("""
    En este ejercicio se registran productos usando arreglos de NumPy.
    Cada vez que se agrega un producto, los datos se guardan en arrays
    y se convierten en un DataFrame para mostrarlo en pantalla.
    """)

    # Inicializar arrays en session_state
    if "nombres" not in st.session_state:
        st.session_state.nombres = []
        st.session_state.categorias = []
        st.session_state.precios = []
        st.session_state.cantidades = []

    st.markdown("### Formulario de producto")

    nombre_prod = st.text_input("Nombre del producto", placeholder="Ej: Cuaderno")
    categoria_prod = st.selectbox("Categoría", ["Papelería", "Electrónica", "Alimentos", "Ropa", "Otro"])
    precio_prod = st.number_input("Precio unitario", min_value=0.0, step=0.5)
    cantidad_prod = st.number_input("Cantidad", min_value=0, step=1)

    if st.button("➕ Agregar producto"):
        if nombre_prod.strip() == "":
            st.error("Por favor escribe el nombre del producto.")
        elif precio_prod <= 0:
            st.error("El precio debe ser mayor a 0.")
        elif cantidad_prod <= 0:
            st.error("La cantidad debe ser mayor a 0.")
        else:
            st.session_state.nombres.append(nombre_prod)
            st.session_state.categorias.append(categoria_prod)
            st.session_state.precios.append(precio_prod)
            st.session_state.cantidades.append(cantidad_prod)
            st.success(f"Producto '{nombre_prod}' agregado.")

    st.markdown("---")

    if len(st.session_state.nombres) > 0:
        # Convertir a arrays de NumPy
        arr_precios = np.array(st.session_state.precios)
        arr_cantidades = np.array(st.session_state.cantidades)
        arr_totales = arr_precios * arr_cantidades

        # Crear DataFrame
        df_productos = pd.DataFrame({
            "Producto": st.session_state.nombres,
            "Categoría": st.session_state.categorias,
            "Precio": arr_precios,
            "Cantidad": arr_cantidades,
            "Total": arr_totales
        })

        st.markdown("### Tabla de productos")
        st.dataframe(df_productos, use_container_width=True)

        st.metric("Total general", f"${arr_totales.sum():,.2f}")

        if st.button("🗑️ Limpiar productos"):
            st.session_state.nombres = []
            st.session_state.categorias = []
            st.session_state.precios = []
            st.session_state.cantidades = []
            st.rerun()
    else:
        st.info("Todavía no hay productos registrados.")

# ─────────────────────────────────────────
# EJERCICIO 3 – Función calcular_imc
# ─────────────────────────────────────────
elif pagina == "Ejercicio 3":
    st.title("Ejercicio 3 – Calculadora de IMC")

    st.markdown("""
    En este ejercicio se usa la función **calcular_imc** de la librería externa.
    Se ingresa el peso y la altura de una persona, se ejecuta la función
    y se guarda el resultado en un historial.
    
    > **Función usada:** `calcular_imc` — Área: Salud  
    > **¿Por qué?** Es fácil de entender. Solo necesita 2 datos y el resultado es claro para cualquier persona.
    """)

    # Inicializar historial
    if "historial_imc" not in st.session_state:
        st.session_state.historial_imc = []

    st.markdown("### Ingresar datos")

    nombre_paciente = st.text_input("Nombre de la persona", placeholder="Ej: Juan Pérez")
    peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, step=0.5)
    altura = st.number_input("Altura (metros)", min_value=0.5, max_value=2.5, step=0.01)

    if st.button("📊 Calcular IMC"):
        if nombre_paciente.strip() == "":
            st.error("Por favor escribe el nombre.")
        else:
            try:
                resultado = calcular_imc(peso, altura)
                st.success(f"IMC calculado: **{resultado['imc']}** — Clasificación: **{resultado['clasificacion']}**")

                st.session_state.historial_imc.append({
                    "Nombre": nombre_paciente,
                    "Peso (kg)": peso,
                    "Altura (m)": altura,
                    "IMC": resultado["imc"],
                    "Clasificación": resultado["clasificacion"]
                })
            except ValueError as e:
                st.error(f"Error: {e}")

    st.markdown("---")

    if len(st.session_state.historial_imc) > 0:
        st.markdown("### Historial de resultados")
        df_imc = pd.DataFrame(st.session_state.historial_imc)
        st.dataframe(df_imc, use_container_width=True)

        if st.button("🗑️ Limpiar historial"):
            st.session_state.historial_imc = []
            st.rerun()
    else:
        st.info("Todavía no hay cálculos registrados.")

# ─────────────────────────────────────────
# EJERCICIO 4 – CRUD con clase Empleado
# ─────────────────────────────────────────
elif pagina == "Ejercicio 4":
    st.title("Ejercicio 4 – Gestión de Empleados (CRUD)")

    st.markdown("""
    En este ejercicio se usa la clase **Empleado** de la librería externa.
    Se pueden crear, ver, actualizar y eliminar empleados.
    
    > **Clase usada:** `Empleado` — Área: Administración / Recursos Humanos  
    > **¿Por qué?** Es muy intuitiva. Todo el mundo entiende los conceptos de salario, bono y descuento.
    """)

    # Inicializar lista de empleados
    if "empleados" not in st.session_state:
        st.session_state.empleados = []

    # ── CREAR ──
    st.markdown("### ➕ Crear empleado")

    nombre_emp = st.text_input("Nombre del empleado", placeholder="Ej: María García")
    salario_emp = st.number_input("Salario base ($)", min_value=1.0, step=50.0)
    bono_emp = st.number_input("Porcentaje de bono (%)", min_value=0.0, max_value=100.0, step=1.0)
    descuento_emp = st.number_input("Porcentaje de descuento (%)", min_value=0.0, max_value=100.0, step=1.0)

    if st.button("💾 Guardar empleado"):
        if nombre_emp.strip() == "":
            st.error("Por favor escribe el nombre del empleado.")
        else:
            # Verificar que no exista ya
            nombres_existentes = [e["nombre"] for e in st.session_state.empleados]
            if nombre_emp in nombres_existentes:
                st.error("Ya existe un empleado con ese nombre.")
            else:
                try:
                    emp = Empleado(nombre_emp, salario_emp, bono_emp, descuento_emp)
                    resumen = emp.resumen()
                    st.session_state.empleados.append(resumen)
                    st.success(f"Empleado '{nombre_emp}' guardado correctamente.")
                except ValueError as e:
                    st.error(f"Error: {e}")

    st.markdown("---")

    # ── LEER ──
    if len(st.session_state.empleados) > 0:
        st.markdown("### 📋 Lista de empleados")
        df_emp = pd.DataFrame(st.session_state.empleados)
        st.dataframe(df_emp, use_container_width=True)

        st.markdown("---")

        # ── ACTUALIZAR ──
        st.markdown("### ✏️ Actualizar empleado")

        nombres_lista = [e["nombre"] for e in st.session_state.empleados]
        nombre_actualizar = st.selectbox("Selecciona el empleado a actualizar", nombres_lista, key="upd")

        nuevo_salario = st.number_input("Nuevo salario base ($)", min_value=1.0, step=50.0, key="nuevo_sal")
        nuevo_bono = st.number_input("Nuevo bono (%)", min_value=0.0, max_value=100.0, step=1.0, key="nuevo_bono")
        nuevo_descuento = st.number_input("Nuevo descuento (%)", min_value=0.0, max_value=100.0, step=1.0, key="nuevo_desc")

        if st.button("🔄 Actualizar"):
            try:
                emp_actualizado = Empleado(nombre_actualizar, nuevo_salario, nuevo_bono, nuevo_descuento)
                nuevo_resumen = emp_actualizado.resumen()
                for i, e in enumerate(st.session_state.empleados):
                    if e["nombre"] == nombre_actualizar:
                        st.session_state.empleados[i] = nuevo_resumen
                        break
                st.success(f"Empleado '{nombre_actualizar}' actualizado.")
                st.rerun()
            except ValueError as e:
                st.error(f"Error: {e}")

        st.markdown("---")

        # ── ELIMINAR ──
        st.markdown("### 🗑️ Eliminar empleado")

        nombre_eliminar = st.selectbox("Selecciona el empleado a eliminar", nombres_lista, key="del")

        if st.button("❌ Eliminar"):
            st.session_state.empleados = [
                e for e in st.session_state.empleados if e["nombre"] != nombre_eliminar
            ]
            st.success(f"Empleado '{nombre_eliminar}' eliminado.")
            st.rerun()

    else:
        st.info("Todavía no hay empleados registrados.")
