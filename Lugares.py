import streamlit as st
import random

# Configuración inicial de la pestaña del navegador
st.set_page_config(page_title="Ahorcado Alemán - Lugares", page_icon="🏙️", layout="centered")

# Base de datos de lugares de la ciudad
lugares_db = [
    {"espanol": "la iglesia", "singular": "die Kirche", "plural": "die Kirchen"},
    {"espanol": "el castillo / el palacio", "singular": "das Schloss", "plural": "die Schlösser"},
    {"espanol": "el parque", "singular": "der Park", "plural": "die Parks"},
    {"espanol": "la fuente", "singular": "der Brunnen", "plural": "die Brunnen"},
    {"espanol": "el ayuntamiento", "singular": "das Rathaus", "plural": "die Rathäuser"},
    {"espanol": "la tienda / el negocio", "singular": "das Geschäft", "plural": "die Geschäfte"},
    {"espanol": "el mercado", "singular": "der Markt", "plural": "die Märkte"},
    {"espanol": "el casco antiguo / ciudad vieja", "singular": "die Altstadt", "plural": "die Altstädte"},
    {"espanol": "el zoológico", "singular": "der Zoo", "plural": "die Zoos"},
    {"espanol": "la plaza / el lugar", "singular": "der Platz", "plural": "die Plätze"},
    {"espanol": "el parque infantil / zona de juegos", "singular": "der Spielplatz", "plural": "die Spielplätze"},
    {"espanol": "el puerto", "singular": "der Hafen", "plural": "die Häfen"},
    {"espanol": "el lago", "singular": "der See", "plural": "die Seen"},
    {"espanol": "la calle", "singular": "die Straße", "plural": "die Straßen"},
    {"espanol": "la estación de tren", "singular": "der Bahnhof", "plural": "die Bahnhöfe"},
    {"espanol": "el museo", "singular": "das Museum", "plural": "die Museen"},
    {"espanol": "el puente", "singular": "die Brücke", "plural": "die Brücken"},
    {"espanol": "la torre", "singular": "der Turm", "plural": "die Türme"},
    {"espanol": "la biblioteca", "singular": "die Bibliothek", "plural": "die Bibliotheken"},
    {"espanol": "el hospital", "singular": "das Krankenhaus", "plural": "die Krankenhäuser"},
    {"espanol": "la farmacia", "singular": "die Apotheke", "plural": "die Apotheken"},
    {"espanol": "el supermercado", "singular": "der Supermarkt", "plural": "die Supermärkte"},
    {"espanol": "el banco", "singular": "die Bank", "plural": "die Banken"}
]

# Diseño clásico del ahorcado
etapas_ahorcado = [
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",  # 0 intentos (Derrota)
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # 1 intento
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # 2 intentos
    "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  # 3 intentos
    "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  # 4 intentos
    "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",  # 5 intentos
    "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="   # 6 intentos (Inicio)
]

# Inicialización de la memoria web (Session State)
if 'juego_activo' not in st.session_state:
    st.session_state.racha = 0
    st.session_state.lugar_actual = random.choice(lugares_db)
    st.session_state.modo = random.choice(["singular", "plural"])
    st.session_state.letras_adivinadas = set()
    st.session_state.intentos = 6
    st.session_state.juego_activo = True
    st.session_state.mensaje = ""
    st.session_state.tipo_mensaje = ""

def reiniciar_juego():
    st.session_state.lugar_actual = random.choice(lugares_db)
    st.session_state.modo = random.choice(["singular", "plural"])
    st.session_state.letras_adivinadas = set()
    st.session_state.intentos = 6
    st.session_state.juego_activo = True
    st.session_state.mensaje = ""
    st.session_state.tipo_mensaje = ""

# --- INTERFAZ VISUAL ---
st.title("🏙️ Ahorcado Alemán: La Ciudad")

if st.session_state.racha >= 1:
    st.warning(f"★ **STREAK: {st.session_state.racha}** ★")

# Crear dos columnas para diseño
col1, col2 = st.columns([1, 2])

with col1:
    st.code(etapas_ahorcado[st.session_state.intentos], language="text")

with col2:
    objetivo_texto = "SINGULAR (CON ARTÍCULO)" if st.session_state.modo == "singular" else "PLURAL (CON ARTÍCULO)"
    st.write(f"**OBJETIVO:** {objetivo_texto}")
    st.write(f"**Significado:** {st.session_state.lugar_actual['espanol']}")
    
    palabra_objetivo = st.session_state.lugar_actual[st.session_state.modo].lower()
    
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
        entrada = st.text_input("Ingresa una letra o la frase completa:").strip().lower()
        enviado = st.form_submit_button("Verificar")
        
        if enviado and entrada:
            if len(entrada) > 1:
                if entrada == palabra_objetivo:
                    st.session_state.letras_adivinadas.update(list(palabra_objetivo))
                    st.session_state.juego_activo = False
                    st.session_state.racha += 1
                    st.session_state.mensaje = "¡Excelente! Adivinaste la frase completa."
                    st.session_state.tipo_mensaje = "exito"
                else:
                    st.session_state.intentos -= 1
                    st.session_state.mensaje = f"Incorrecto. Te quedan {st.session_state.intentos} intentos."
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

            # Verificar condiciones de victoria o derrota
            letras_faltantes = [c for c in palabra_objetivo if c not in st.session_state.letras_adivinadas and c not in [' ', '/']]
            
            if not letras_faltantes and st.session_state.juego_activo:
                st.session_state.juego_activo = False
                st.session_state.racha += 1
                st.session_state.mensaje = "¡Excelente! Lugar resuelto."
                st.session_state.tipo_mensaje = "exito"
            elif st.session_state.intentos <= 0 and st.session_state.juego_activo:
                st.session_state.juego_activo = False
                st.session_state.racha = 0
                st.session_state.mensaje = f"Sin intentos. La respuesta era: {palabra_objetivo}"
                st.session_state.tipo_mensaje = "error"

            st.rerun()

# Revelación de contra-palabra y botón de Siguiente
if not st.session_state.juego_activo:
    singular_texto = st.session_state.lugar_actual['singular']
    plural_texto = st.session_state.lugar_actual['plural']
    
    st.markdown("---")
    if st.session_state.modo == "singular":
        st.info(f"**Singular:** {singular_texto} ➔ **Plural:** {plural_texto}")
    else:
        st.info(f"**Plural:** {plural_texto} ➔ **Singular:** {singular_texto}")
        
    st.button("Siguiente Lugar ➔", on_click=reiniciar_juego, type="primary")
