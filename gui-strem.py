import streamlit as st
from subprocess import run
import arabic_reshaper

def main():
    st.title("COMPILATEUR et TRADUCTEUR PYTHON DES PROVERBES AR / FR / ANG ")

    # Translation Direction Selection
    selected_translation = st.radio("CHOISIR VOTRE LANGUE:", ("Arabe vers Français", "Français vers Anglais"))

    # Define dropdown options based on the selected translation direction
    if selected_translation == "Arabe vers Français":
        options = ["motive", "optimiste", "égoïste"]
        selected_option = st.selectbox("CHOISIR VOTRE SITUATION:", options)

        # Button widget to validate the choice
        if st.button("Valider le choix"):
            if selected_option == "optimiste":
                st.write("Le proverbe est : شحال ما طال الليل كيطلع النهار")
            elif selected_option == "motive":
                st.write("Le proverbe est : أنا فران وقاد بحوما")
            elif selected_option == "égoïste":
                st.write("Le proverbe est : لي كيعيش أناني كيموت وحداني")

    elif selected_translation == "Français vers Anglais":
        options = ["Fidelite", "Concenter"]
        selected_option = st.selectbox("CHOISIR VOTRE SITUATION:", options)

        # Button widget to validate the choice
        if st.button("Valider le choix"):
            if selected_option == "Fidelite":
                st.write("Le proverbe est : On ne change jamais une équipe qui gagne")
            elif selected_option == "Concenter":
                st.write("Le proverbe est : Qui cherche la lune ne voit pas les étoiles")

    # Champ de saisie pour le texte
    data = st.text_input("Saisissez le proverbe en haut  (en arabe ou en français) :")

    # Bouton de validation
    if st.button("Valider"):
        # Affichage des valeurs pour le débogage
        print(f"Langue sélectionnée: {selected_translation}")
        print(f"Données saisies: {data}")

        # Appel du script Python externe pour traiter la variable data
        result = run(["python", "C:\\Users\\Zakaria\\OneDrive\\Desktop\\ply\\projetmoumen\\projet.py", data],
                     capture_output=True, text=True, shell=True,encoding='utf-8')

        # Affichage des éventuelles erreurs dans la sortie standard
        print(f"Erreurs (stderr): {result.stderr}")

        # Remise en forme du texte arabe
        if selected_translation == "Arabe vers Français":
            data_reshaped = arabic_reshaper.reshape(data)
        else:
            data_reshaped = data

        # Affichage du résultat dans l'interface
        st.write("Résultat du compilateur : \n")
        st.write(result.stdout)

    # Bouton pour ouvrir une nouvelle fenêtre avec le script du chatbot
    chatbot_button_clicked = st.button("BA SIDI / MON GARND-PERE")

    # Si le bouton "Chatbot" est cliqué, ouvrir une nouvelle fenêtre avec le script du chatbot
    if chatbot_button_clicked:
        chatbot_url = "http://localhost:8502/"  # Remplacez ceci par l'URL réel de votre script Chatbot
        chatbot_link = f"[Cliquez ici pour ouvrir le Chatbot]({chatbot_url})"
        st.markdown(chatbot_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
