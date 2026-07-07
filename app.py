import streamlit as st
import random
# Configuración inicial de la pestaña del navegador
st.set_page_config(page_title="Ahorcado Alemán", page_icon="🇩🇪", layout="centered")
# Base de datos de verbos
verbos_db = [
    {"espanol": "Hornear", "infinitivo": "backen", "perfecto": "gebacken"},
    {"espanol": "Empezar / Comenzar", "infinitivo": "beginnen", "perfecto": "begonnen"},
    {"espanol": "Ofrecer", "infinitivo": "bieten", "perfecto": "geboten"},
    {"espanol": "Pedir / Rogar", "infinitivo": "bitten", "perfecto": "gebeten"},
    {"espanol": "Quedarse", "infinitivo": "bleiben", "perfecto": "geblieben"},
    {"espanol": "Asar / Freir", "infinitivo": "braten", "perfecto": "gebraten"},
    {"espanol": "Traer / Llevar", "infinitivo": "bringen", "perfecto": "gebracht"},
    {"espanol": "Pensar", "infinitivo": "denken", "perfecto": "gedacht"},
    {"espanol": "Comer", "infinitivo": "essen", "perfecto": "gegessen"},
    {"espanol": "Conducir / Ir (en vehículo)", "infinitivo": "fahren", "perfecto": "gefahren"},
    {"espanol": "Caer", "infinitivo": "fallen", "perfecto": "gefallen"},
    {"espanol": "Atrapar / Coger", "infinitivo": "fangen", "perfecto": "gefangen"},
    {"espanol": "Encontrar", "infinitivo": "finden", "perfecto": "gefunden"},
    {"espanol": "Volar", "infinitivo": "fliegen", "perfecto": "geflogen"},
    {"espanol": "Dar", "infinitivo": "geben", "perfecto": "gegeben"},
    {"espanol": "Ir", "infinitivo": "gehen", "perfecto": "gegangen"},
    {"espanol": "Disfrutar", "infinitivo": "genießen", "perfecto": "genossen"},
    {"espanol": "Ganar", "infinitivo": "gewinnen", "perfecto": "gewonnen"},
    {"espanol": "Tener", "infinitivo": "haben", "perfecto": "gehabt"},
    {"espanol": "Sostener / Parar", "infinitivo": "halten", "perfecto": "gehalten"},
    {"espanol": "Estar colgado", "infinitivo": "hängen", "perfecto": "gehangen"},
    {"espanol": "Colgar algo", "infinitivo": "hängen", "perfecto": "gehängt"},
    {"espanol": "Llamarse", "infinitivo": "heißen", "perfecto": "geheißen"},
    {"espanol": "Ayudar", "infinitivo": "helfen", "perfecto": "geholfen"},
    {"espanol": "Conocer", "infinitivo": "kennen", "perfecto": "gekannt"},
    {"espanol": "Venir", "infinitivo": "kommen", "perfecto": "gekommen"},
    {"espanol": "Dejar", "infinitivo": "lassen", "perfecto": "gelassen"},
    {"espanol": "Correr / Andar", "infinitivo": "laufen", "perfecto": "gelaufen"},
    {"espanol": "Leer", "infinitivo": "lesen", "perfecto": "gelesen"},
    {"espanol": "Estar tumbado / Ubicado", "infinitivo": "liegen", "perfecto": "gelegen"},
    {"espanol": "Fracasar / Salir mal", "infinitivo": "misslingen", "perfecto": "misslungen"},
    {"espanol": "Tomar / Coger", "infinitivo": "nehmen", "perfecto": "genommen"},
    {"espanol": "Nombrar/Llamar", "infinitivo": "nennen", "perfecto": "genannt"},
    {"espanol": "Aconsejar / Adivinar", "infinitivo": "raten", "perfecto": "geraten"},
    {"espanol": "Montar a caballo", "infinitivo": "reiten", "perfecto": "geritten"},
    {"espanol": "Correr (rápido)", "infinitivo": "rennen", "perfecto": "gerannt"},
    {"espanol": "Llamar (a gritos)", "infinitivo": "rufen", "perfecto": "gerufen"},
    {"espanol": "Crear / Lograr", "infinitivo": "schaffen", "perfecto": "geschaffen"},
    {"espanol": "Dormir", "infinitivo": "schlafen", "perfecto": "geschlafen"},
    {"espanol": "Cerrar", "infinitivo": "schließen", "perfecto": "geschlossen"},
    {"espanol": "Cortar", "infinitivo": "schneiden", "perfecto": "geschnitten"},
    {"espanol": "Escribir", "infinitivo": "schreiben", "perfecto": "geschrieben"},
    {"espanol": "Nadar", "infinitivo": "schwimmen", "perfecto": "geschwommen"},
    {"espanol": "Ver", "infinitivo": "sehen", "perfecto": "gesehen"},
    {"espanol": "Ser/ Estar", "infinitivo": "sein", "perfecto": "gewesen"},
    {"espanol": "Enviar", "infinitivo": "senden", "perfecto": "gesandt"},
    {"espanol": "Cantar", "infinitivo": "singen", "perfecto": "gesungen"},
    {"espanol": "Estar sentado", "infinitivo": "sitzen", "perfecto": "gesessen"},
    {"espanol": "Hablar", "infinitivo": "sprechen", "perfecto": "gesprochen"},
    {"espanol": "Saltar", "infinitivo": "springen", "perfecto": "gesprungen"},
    {"espanol": "Estar de pie", "infinitivo": "stehen", "perfecto": "gestanden"},
    {"espanol": "Subir/Escalar", "infinitivo": "steigen", "perfecto": "gestiegen"},
    {"espanol": "Morir", "infinitivo": "sterben", "perfecto": "gestorben"},
    {"espanol": "Llevar (puesto) / Cargar", "infinitivo": "tragen", "perfecto": "getragen"},
    {"espanol": "Encontrar(se)", "infinitivo": "treffen", "perfecto": "getroffen"},
    {"espanol": "Beber", "infinitivo": "trinken", "perfecto": "getrunken"},
    {"espanol": "Hacer", "infinitivo": "tun", "perfecto": "getan"},
    {"espanol": "Olvidar", "infinitivo": "vergessen", "perfecto": "vergessen"},
    {"espanol": "Perder", "infinitivo": "verlieren", "perfecto": "verloren"},
    {"espanol": "Crecer", "infinitivo": "wachsen", "perfecto": "gewachsen"},
    {"espanol": "Lavar", "infinitivo": "waschen", "perfecto": "gewaschen"},
    {"espanol": "Llegar a ser / Convertirse", "infinitivo": "werden", "perfecto": "geworden"},
    {"espanol": "Saber", "infinitivo": "wissen", "perfecto": "gewusst"},
    {"espanol": "Tirar/Mudar(se)", "infinitivo": "ziehen", "perfecto": "gezogen"}
]
etapas_ahorcado = [
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
  =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========
    """,
    """
    +---+
    |   |

O |
| :--- |
|
| <br> ========= <br> """, <br> """ <br> +---+
| :--- | <br> O   |
|
|
| <br> ========= <br> """, <br> """ <br> +---+
| :--- |
|
|
|
|

  =========
    """
]
# Inicialización de la memoria web (Session State)
if 'juego_activo' not in st.session_state:
    st.session_state.racha = 0
    st.session_state.verbo_actual = random.choice(verbos_db)
    st.session_state.modo = random.choice(["infinitivo", "perfecto"])
    st.session_state.letras_adivinadas = set()
    st.session_state.intentos = 6
    st.session_state.juego_activo = True
    st.session_state.mensaje = ""
    st.session_state.tipo_mensaje = ""
def reiniciar_juego():
    st.session_state.verbo_actual = random.choice(verbos_db)
    st.session_state.modo = random.choice(["infinitivo", "perfecto"])
    st.session_state.letras_adivinadas = set()
    st.session_state.intentos = 6
    st.session_state.juego_activo = True
    st.session_state.mensaje = ""
    st.session_state.tipo_mensaje = ""
# --- INTERFAZ VISUAL ---
st.title("🇩🇪 Ahorcado Alemán A1")
if st.session_state.racha >= 1:
    st.warning(f"★ **STREAK: {st.session_state.racha}** ★")
# Crear dos columnas para diseño
col1, col2 = st.columns([1, 2])
with col1:
    st.code(etapas_ahorcado[st.session_state.intentos], language="text")
with col2:
    objetivo_texto = "INFINITIVO" if st.session_state.modo == "infinitivo" else "PERFECTO (PARTIZIP II)"
    st.write(f"**OBJETIVO:** {objetivo_texto}")
    st.write(f"**Significado:** {st.session_state.verbo_actual['espanol']}")
    
    palabra_objetivo = st.session_state.verbo_actual[st.session_state.modo].lower()
    
    palabra_mostrada = ""
    for char in palabra_objetivo:
        if char in st.session_state.letras_adivinadas or char in [' ', '/']:
            palabra_mostrada += char + " "
        else:
            palabra_mostrada += "_ "
            
    st.markdown(f"### {palabra_mostrada.strip()}")
# Mensajes dinámicos
if st.session_state.mensaje:
    if st.session_state.tipo_mensaje == "exito":
        st.success(st.session_state.mensaje)
    elif st.session_state.tipo_mensaje == "error":
        st.error(st.session_state.mensaje)
    else:
        st.info(st.session_state.mensaje)
# Lógica del formulario de entrada
if st.session_state.juego_activo:
    with st.form("entrada_form", clear_on_submit=True):
        entrada = st.text_input("Ingresa una letra o la palabra completa:").strip().lower()
        enviado = st.form_submit_button("Verificar")
        
        if enviado and entrada:
            if len(entrada) > 1:
                if entrada == palabra_objetivo:
                    st.session_state.letras_adivinadas.update(list(palabra_objetivo))
                    st.session_state.juego_activo = False
                    st.session_state.racha += 1
                    st.session_state.mensaje = "¡Excelente! Adivinaste la palabra de una vez."
                    st.session_state.tipo_mensaje = "exito"
                else:
                    st.session_state.intentos -= 1
                    st.session_state.mensaje = f"Palabra incorrecta. Te quedan {st.session_state.intentos} intentos."
                    st.session_state.tipo_mensaje = "error"
            else:
                if not entrada.isalpha() and entrada not in ['ä', 'ö', 'ü', 'ß']:
                    st.session_state.mensaje = "Ingresa un carácter válido."
                    st.session_state.tipo_mensaje = "info"
                elif entrada in st.session_state.letras_adivinadas:
                    st.session_state.mensaje = "Esa letra ya la usaste."
                    st.session_state.tipo_mensaje = "info"
                else:
                    st.session_state.letras_adivinadas.add(entrada)
                    if entrada not in palabra_objetivo:
                        st.session_state.intentos -= 1
                        st.session_state.mensaje = f"Letra incorrecta. Te quedan {st.session_state.intentos} intentos."
                        st.session_state.tipo_mensaje = "error"
                    else:
                        st.session_state.mensaje = "¡Bien hecho!"
                        st.session_state.tipo_mensaje = "exito"
            # Verificar condiciones de victoria o derrota letra a letra
            letras_faltantes = [c for c in palabra_objetivo if c not in st.session_state.letras_adivinadas and c not in [' ', '/']]
            
            if not letras_faltantes and st.session_state.juego_activo:
                st.session_state.juego_activo = False
                st.session_state.racha += 1
                st.session_state.mensaje = "¡Excelente! Verbo resuelto."
                st.session_state.tipo_mensaje = "exito"
            elif st.session_state.intentos <= 0 and st.session_state.juego_activo:
                st.session_state.juego_activo = False
                st.session_state.racha = 0
                st.session_state.mensaje = f"Sin intentos. La palabra era: {palabra_objetivo.upper()}"
                st.session_state.tipo_mensaje = "error"
            st.rerun()
# Revelación de contra-verbo y botón de Siguiente
if not st.session_state.juego_activo:
    infinitivo = st.session_state.verbo_actual['infinitivo']
    perfecto = st.session_state.verbo_actual['perfecto']
    
    st.markdown("---")
    if st.session_state.modo == "infinitivo":
        st.info(f"**Base:** {infinitivo} ➔ **Perfecto:** {perfecto}")
    else:
        st.info(f"**Perfecto:** {perfecto} ➔ **Infinitivo:** {infinitivo}")
        
    st.button("Siguiente Verbo ➔", on_click=reiniciar_juego, type="primary")
