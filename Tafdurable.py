import streamlit as st
import pandas as pd

# =========================================================
# CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AgriDurable",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ÉTAT DE L'APPLICATION
# =========================================================

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "page" not in st.session_state:
    st.session_state.page = "Accueil"

# =========================================================
# THÈME
# =========================================================

if st.session_state.dark_mode:
    bg = "#101418"
    card = "#1B2228"
    text = "#FFFFFF"
    muted = "#A7ADB4"
    border = "#303942"
else:
    bg = "#F4F7F4"
    card = "#FFFFFF"
    text = "#1F2937"
    muted = "#6B7280"
    border = "#E5E7EB"

# =========================================================
# DESIGN
# =========================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {bg};
    }}

    [data-testid="stSidebar"] {{
        background-color: {card};
    }}

    .main-title {{
        font-size: 38px;
        font-weight: 800;
        color: #35A853;
        margin-bottom: 0;
    }}

    .subtitle {{
        color: {muted};
        font-size: 16px;
        margin-top: 5px;
        margin-bottom: 25px;
    }}

    .slogan {{
        background-color: {card};
        border: 1px solid {border};
        border-radius: 18px;
        padding: 20px;
        margin: 20px 0 30px 0;
        text-align: center;
        font-size: 19px;
        font-weight: 600;
        color: #35A853;
    }}

    .card {{
        background-color: {card};
        border: 1px solid {border};
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 15px;
    }}

    .stat-icon {{
        font-size: 30px;
    }}

    .stat-title {{
        color: {muted};
        font-size: 14px;
        margin-top: 8px;
    }}

    .stat-value {{
        color: #35A853;
        font-size: 28px;
        font-weight: 800;
    }}

    .section-title {{
        color: {text};
        font-size: 25px;
        font-weight: 700;
        margin: 25px 0 15px 0;
    }}

    .info {{
        color: {text};
        font-size: 15px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR / NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;">
            <div style="font-size:45px;">🌱</div>
            <h1 style="color:#35A853;">AgriDurable</h1>
            <p>Agriculture intelligente</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    pages = [
        ("🏠", "Accueil"),
        ("🌾", "Cultures"),
        ("💧", "Eau"),
        ("🌱", "Sol"),
        ("📊", "Statistiques"),
        ("♻️", "Conseils"),
        ("👤", "Profil")
    ]

    for icon, page in pages:

        if st.button(
            f"{icon}  {page}",
            key=f"menu_{page}",
            use_container_width=True
        ):
            st.session_state.page = page
            st.rerun()

    st.divider()

    # Bouton thème
    if st.session_state.dark_mode:

        if st.button(
            "☀️  Mode clair",
            use_container_width=True
        ):
            st.session_state.dark_mode = False
            st.rerun()

    else:

        if st.button(
            "🌙  Mode sombre",
            use_container_width=True
        ):
            st.session_state.dark_mode = True
            st.rerun()

# =========================================================
# PAGE ACCUEIL
# =========================================================

if st.session_state.page == "Accueil":

    st.markdown(
        '<div class="main-title">🌱 AgriDurable</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Votre assistant pour une agriculture intelligente.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="slogan">
            🌱 « Cultiver aujourd’hui, préserver demain. »
        </div>
        """,
        unsafe_allow_html=True
    )

    # Statistiques
    col1, col2, col3, col4 = st.columns(4)

    statistiques = [
        ("🌾", "Cultures", "5"),
        ("💧", "Eau utilisée", "12 450 L"),
        ("📊", "Production", "3 200 kg"),
        ("🌱", "État du sol", "Bon")
    ]

    for col, (icon, title, value) in zip(
        [col1, col2, col3, col4],
        statistiques
    ):

        with col:

            st.markdown(
                f"""
                <div class="card">
                    <div class="stat-icon">{icon}</div>
                    <div class="stat-title">{title}</div>
                    <div class="stat-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">♻️ Conseil du jour</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card">
            <div class="info">
                💧 Utilisez une irrigation adaptée aux besoins
                de vos cultures afin de réduire le gaspillage d’eau.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# PAGE CULTURES
# =========================================================

elif st.session_state.page == "Cultures":

    st.markdown(
        '<div class="main-title">🌾 Mes cultures</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Gérez les cultures de votre exploitation.'
        '</div>',
        unsafe_allow_html=True
    )

    with st.expander("➕ Ajouter une culture"):

        nom = st.text_input("Nom de la culture")

        surface = st.number_input(
            "Surface en hectares",
            min_value=0.0,
            step=0.1
        )

        date = st.date_input(
            "Date de plantation"
        )

        if st.button("💾 Enregistrer la culture"):

            if nom:

                st.success(
                    f"🌱 La culture « {nom} » a été ajoutée."
                )

            else:

                st.warning(
                    "Veuillez saisir le nom de la culture."
                )

    cultures = pd.DataFrame({
        "Culture": [
            "🌽 Maïs",
            "🍅 Tomates",
            "🥕 Carottes",
            "🥬 Laitue"
        ],
        "Surface": [
            "2 ha",
            "1 ha",
            "0.5 ha",
            "0.3 ha"
        ],
        "État": [
            "Bon",
            "Excellent",
            "Bon",
            "Excellent"
        ]
    })

    st.markdown(
        '<div class="section-title">Cultures enregistrées</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        cultures,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# PAGE EAU
# =========================================================

elif st.session_state.page == "Eau":

    st.markdown(
        '<div class="main-title">💧 Gestion de l’eau</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Surveillez votre consommation d’eau.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">
                <div class="stat-title">
                    Consommation actuelle
                </div>

                <div class="stat-value">
                    12 450 L
                </div>

                <div class="info">
                    Objectif : 15 000 L
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">
                <div class="stat-title">
                    Gestion
                </div>

                <div class="stat-value">
                    Bonne
                </div>

                <div class="info">
                    Continuez à économiser l’eau.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.progress(
        0.83,
        text="83 % de l’objectif mensuel"
    )

# =========================================================
# PAGE SOL
# =========================================================

elif st.session_state.page == "Sol":

    st.markdown(
        '<div class="main-title">🌱 État du sol</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Surveillez la qualité de vos sols.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    sol = [
        ("💧", "Humidité", "68 %"),
        ("🌱", "Fertilité", "Bonne"),
        ("⚗️", "pH", "6.7"),
        ("♻️", "Matière organique", "Élevée")
    ]

    for col, (icon, title, value) in zip(
        [col1, col2, col3, col4],
        sol
    ):

        with col:

            st.markdown(
                f"""
                <div class="card">
                    <div class="stat-icon">{icon}</div>
                    <div class="stat-title">{title}</div>
                    <div class="stat-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# PAGE STATISTIQUES
# =========================================================

elif st.session_state.page == "Statistiques":

    st.markdown(
        '<div class="main-title">📊 Statistiques</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Analysez l’évolution de votre production.'
        '</div>',
        unsafe_allow_html=True
    )

    statistiques = pd.DataFrame({
        "Mois": [
            "Janvier",
            "Février",
            "Mars",
            "Avril",
            "Mai",
            "Juin"
        ],
        "Production": [
            1800,
            2100,
            1900,
            2500,
            2900,
            3200
        ]
    })

    st.line_chart(
        statistiques.set_index("Mois")
    )

    st.dataframe(
        statistiques,
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# PAGE CONSEILS
# =========================================================

elif st.session_state.page == "Conseils":

    st.markdown(
        '<div class="main-title">♻️ Conseils écologiques</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Des conseils pour une agriculture plus durable.'
        '</div>',
        unsafe_allow_html=True
    )

    conseils = [
        (
            "💧",
            "Économisez l’eau",
            "Adaptez l’irrigation aux besoins réels des cultures."
        ),
        (
            "🌱",
            "Protégez le sol",
            "Utilisez du compost et pratiquez la rotation des cultures."
        ),
        (
            "🐝",
            "Protégez la biodiversité",
            "Préservez les insectes utiles et les espaces naturels."
        ),
        (
            "♻️",
            "Réduisez les déchets",
            "Valorisez les déchets agricoles grâce au compostage."
        )
    ]

    for icon, title, text in conseils:

        st.markdown(
            f"""
            <div class="card">
                <h3>{icon} {title}</h3>
                <div class="info">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# PAGE PROFIL
# =========================================================

elif st.session_state.page == "Profil":

    st.markdown(
        '<div class="main-title">👤 Mon profil</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="card" style="text-align:center;">
            <div style="font-size:65px;">👨‍🌾</div>
            <h2>Agriculteur</h2>
            <p>Gestionnaire de l’exploitation</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    nom = st.text_input("Nom")

    exploitation = st.text_input(
        "Nom de l’exploitation"
    )

    if st.button("💾 Enregistrer le profil"):

        st.success(
            "Profil enregistré avec succès !"
        )

# =========================================================
# PIED DE PAGE
# =========================================================

st.markdown(
    """
    <br>
    <hr>

    <div style="text-align:center;">
        🌱 <b>AgriDurable</b><br>
        « Cultiver aujourd’hui, préserver demain. »
    </div>
    """,
    unsafe_allow_html=True
)
