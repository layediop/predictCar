# import streamlit as st
# import pandas as pd
# from PIL import Image
# import random
# import requests
# from io import BytesIO


# # Fonction pour charger l'image depuis une URL
# def load_image_from_url(url):
#     response = requests.get(url)
#     img = Image.open(BytesIO(response.content))
#     return img


# # Configuration de la page
# st.set_page_config(
#     page_title="Voiture de Sport ou Non",
#     page_icon="🚗",
#     layout="centered",
#     initial_sidebar_state="collapsed",
# )

# # Styles CSS pour personnalisation (ajout du header avec logo et titre sur la même ligne)
# st.markdown(
#     """
#     <style>
#         /* Corps de la page */
#         body {
#             background-color: #0e1117;
#             color: #ffffff;
#             font-family: 'Arial', sans-serif;
#         }

#         /* Header avec logo et titre sur la même ligne */
#         .header {
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#             background-color: #1e2228;
#             padding: 20px;
#             color: #ffffff;
#             font-weight: bold;
#             font-size: 22px;
#             border-radius: 8px;
#             margin-top: -70px;

#         }

#         .logo {
#             width: 50px;
#             margin-right: 20px;
#         }

#         .title {
#             font-size: 22px;
#         }

#         /* Sous-titre */
#         .subtitle {
#             text-align: center;
#             font-size: 18px;
#             margin-bottom: 50px;
#         }

#         /* Section d'upload */
#         .upload-section {
#             text-align: center;
#             margin-top: 20px;
#         }

#         /* Aligner le bouton "Predict" à droite */
#         .predict-btn {
#             display: flex;
#             justify-content: flex-end;
#         }
#     </style>
# """,
#     unsafe_allow_html=True,
# )

# # Header avec le logo, le titre "Groupe 2" et le titre principal
# st.markdown(
#     """
#     <div class="header">
#         <img src="https://th.bing.com/th?id=OIP._KDC62yggz2WJ4qnK5jDfQHaEK&w=333&h=187&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2" alt="Logo" class="logo">
#         <div class="title">Détection de Voiture de Sport 🚗</div>
#         <div class="title">Groupe 2</div>
#     </div>
# """,
#     unsafe_allow_html=True,
# )

# # Upload de l'image
# uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"])

# # Affichage de l'image uploadée et prédiction
# if uploaded_file is not None:
#     # Charger l'image téléchargée
#     image = Image.open(uploaded_file)

#     # Redimensionner l'image téléchargée
#     image = image.resize((image.width, 800))

#     # Afficher l'image téléchargée redimensionnée
#     st.image(image, caption=" ", use_column_width=True)

#     with st.markdown("<div class='predict-btn'>", unsafe_allow_html=True):
#         if st.button("Predict"):
#             # Simuler une prédiction
#             is_sports_car = random.choice([True, False])  # À remplacer par votre modèle
#             if is_sports_car:
#                 st.success("C'est une voiture de sport ! 🚗")
#             else:
#                 st.warning("Ce n'est pas une voiture de sport.")
#     st.markdown("</div>", unsafe_allow_html=True)
# else:
#     # Message lorsque aucune image n'est téléchargée
#     st.write("Veuillez charger une image pour activer la prédiction.")
# -----------------------------------------------------------------------------

# import streamlit as st
# import pandas as pd
# from PIL import Image
# import numpy as np
# import joblib

# # Charger le modèle scikit-learn
# model = joblib.load("votre_modele.pkl")

# # Fonction pour prétraiter l'image
# def preprocess_image(image):
#     image = image.resize((224, 224))  # Adaptez la taille à votre modèle
#     image_array = np.array(image).flatten()  # Applatir pour scikit-learn
#     return image_array.reshape(1, -1)  # Adapter au modèle

# # Configuration de la page
# st.set_page_config(
#     page_title="Voiture de Sport ou Non",
#     page_icon="🚗",
#     layout="centered",
#     initial_sidebar_state="collapsed",
# )

# st.markdown("<h1 style='text-align: center;'>Détection de Voiture de Sport 🚗</h1>", unsafe_allow_html=True)

# # Upload de l'image
# uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Image téléchargée", use_column_width=True)

#     if st.button("Predict"):
#         # Prétraiter l'image et faire une prédiction
#         image_array = preprocess_image(image)
#         prediction = model.predict(image_array)
#         is_sports_car = prediction[0]  # Sortie du modèle scikit-learn

#         # Afficher le résultat
#         if is_sports_car:
#             st.success("C'est une voiture de sport ! 🚗")
#         else:
#             st.warning("Ce n'est pas une voiture de sport.")
# else:
#     st.write("Veuillez charger une image pour activer la prédiction.")
# -------------------------------------------------------------------------


import streamlit as st
import pandas as pd
from PIL import Image
import random
import requests
from io import BytesIO


# Fonction pour charger l'image depuis une URL
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


# Configuration de la page
st.set_page_config(
    page_title="Voiture de Sport",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Styles CSS pour personnalisation
st.markdown(
    """
    <style>
        body {
            background-color: #0e1117;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #1e2228;
            padding: 20px;
            color: #ffffff;
            font-weight: bold;
            font-size: 22px;
            border-radius: 8px;
            margin-top: -70px;
        }
        .logo {
            width: 50px;
            margin-right: 20px;
        }
        .title {
            font-size: 22px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 50px;
        }
        .upload-section {
            text-align: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header avec le logo, le titre "Groupe 2" et le titre principal
st.markdown(
    """
    <div class="header">
        <img src="https://th.bing.com/th?id=OIP._KDC62yggz2WJ4qnK5jDfQHaEK&w=333&h=187&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2" alt="Logo" class="logo">
        <div class="title">Détection de Voiture de Sport 🚗</div>
        <div class="title">Groupe 2</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Upload de l'image
uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"])


# Fonction de prédiction simulée avec pourcentages
def predict_sports_car():
    sports_car_score = random.uniform(0, 1)
    not_sports_car_score = 1 - sports_car_score
    return sports_car_score, not_sports_car_score


# Affichage de l'image uploadée et prédiction
if uploaded_file is not None:
    # Charger l'image téléchargée
    image = Image.open(uploaded_file)

    # Redimensionner l'image téléchargée
    image = image.resize((image.width, 800))

    # Afficher l'image téléchargée redimensionnée
    st.image(image, caption=" ", use_column_width=True)

    # Bouton pour effectuer la prédiction
    if st.button("Predict"):
        # Obtenir les scores de prédiction
        sports_car_score, not_sports_car_score = predict_sports_car()

        # Afficher les résultats
        st.markdown(f"### Résultats de la prédiction :")
        st.write(
            f"- **Probabilité d'être une voiture de sport :** {sports_car_score * 100:.2f}%"
        )
        st.write(
            f"- **Probabilité de ne pas être une voiture de sport :** {not_sports_car_score * 100:.2f}%"
        )

        # Message de conclusion
        if sports_car_score > not_sports_car_score:
            st.success("C'est probablement une voiture de sport ! 🚗")
        else:
            st.warning("Ce n'est probablement pas une voiture de sport.")
else:
    # Message lorsque aucune image n'est téléchargée
    st.info("Veuillez charger une image pour activer la prédiction.")
