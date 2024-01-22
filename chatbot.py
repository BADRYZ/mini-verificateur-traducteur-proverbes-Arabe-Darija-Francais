import streamlit as st
from nltk.chat.util import Chat, reflections

# Your pairs go here...
pairs = [
    ########## arabiya
    [########### salam
        r"salam jedi",
        ["salam waldi ! kif deyr m3a l9rya ?"]
    ],
    [
        r"salam ba sidi",
        ["salam benty ! kif deyras m3a l9rya ?"]
    ],
    ### en fr
    [
        r"Bonjour mon grand pere",
        ["ohh grand homme ! comment allez -vous "]
    ],
    [
        r"Bonjour mon pere",
        ["ohh ma fille ! comment allez -vous "]
    ],

    ############# so2ell
    [
        r"Bghit nssawlek ajedi 3la whd lmtal sme3too",
        ["ayeeeh aweldi , marhba !"]
    ],
    [
        r"Bghit nssawlek a ba sidi 3la whd lmtal sme3too",
        ["ayeeeh abenty , marhba !"]
    ],
    ##### jaawab
    #### proverbe 1 arab
    [
        r"شحال ما طال  الليل كيطلع النهار  achno kay3eni",
        ["had lmatal 9aloh nass zmaane bch lwahd myf9edch amal o diima ykoun mtfe2el b lmoste9baal , rah ttzeyer hta tzeyer o ftali yferejha rebi... o bach mat9olch jedek ma9arich, had lmatal kno ty9oloh lfrancawiyine  li kno khedmine m3aya b francais : Aussi longtemps que la nuit dure, le jour finira par se lever "]
    ],
    ##### proverbe 2 arabe
    [
        r"أنا فران  و قاد بحوما achno kay3eni",
        ["had lmatal 9aloh nass zmaane bch lwahd ybeyen lnass rah capable o9ed b chghalo o mayhtaj hta chi whd ydir fih lkhire...o bach mat9olch jedek ma9arich, had lmatal kno ty9oloh lfrancawiyine  li kno khedmine m3aya b francais :je suis capable du meilleur et du pire. "]
    ],
    ##### proverbe 3 arab
    [
         r"لي كيعيش أناني كيموت وحداني achno kay3eni",
        ["had lmatal 9aloh nass zmaane bch 3emer lwhd ybghi rire rasso o yfeker ghire fih, dima feker lnass o 3ewnhom rak whd nher tmot omatl9a li yaw9ef M3a nassek ...o bach mat9olch jedek ma9arich, had lmatal kno ty9oloh lfrancawiyine  li kno khedmine m3aya b francais :L'égoïsme, c'est la solitude qui se prépare à sa propre mort."]
    ],
    ####### proverbe 1 fr
    [
         r"j'ai entendu récemment on ne change jamais une equipe qui gagne Ça a du sens",
        ["c'est un proverbe intéressant, celui-là. Cela signifie que lorsque quelque chose fonctionne bien et donne de bons résultats, il est souvent judicieux de ne pas apporter de changements majeurs... les anglophones se traduisent ce proverbe en : Never change a winning team ."]
    ],
    ###### proverbe en 2 fr
    [
        r"j'ai entendu récemment  qui cherche la lune ne vit pas les etoiles Ça a du sens",
        ["c'est un proverbe sage. Cela signifie que parfois, lorsque tu vises quelque chose de très grand ou difficile, tu risques de passer à côté des petites merveilles qui se trouvent tout autour de toi...les anglophones se traduisent ce proverbe en :He who seeks the moon does not see the stars."]
    ],
    [
        r"Merci",
        [": De rien  Je suis content que ça ait du sens pour toi  Rappelez-vous  la vie est une aventure pleine de découvertes"]
    ],
    [
        r"Choookran",
        ["hada wajib  o dima b9a tfhem lklaam dial nass zmane ! "]
    ],


]


# Create a chatbot with the pairs
chatbot = Chat(pairs, reflections)

def main():
    # Set the page configuration
    st.set_page_config(
        page_title="NDWI M3A BA SIDI / PARLER AVEC MON GRAND-PERE",
        page_icon=":robot_face:",
        layout="wide",  # You can use "wide" or "centered"
        initial_sidebar_state="auto"
    )

    # Set the width of the main content


    st.title("NDWI M3A BA SIDI / PARLER AVEC MON GRAND-PERE")

    # Increase the height of the text area
    user_input = st.text_input("Votre message:")

    if user_input.lower() == 'q':
        st.text("Au revoir !\nALLh yredi 3lik !")
    else:
        response = chatbot.respond(user_input)
        if response is not None:
            st.markdown(f"<div style='width: 800px;'>Vous: {user_input}<br>BA SIDI: {response}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='width: 800px;'>Vous: {user_input}<br>N3eeeem ? Masmeee3tekch mzyann<br>Comment ? je n'ai pas compris</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
