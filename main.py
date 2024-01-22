from turtle import st
import ply.lex as lex
#import arabic_reshaper
import sys


from arabic_reshaper import reshape

tokens = (
    #proverbe 1 en arabe
    'prov1_1',
    'prov1_2',
    'prov1_3',
    'prov1_4',
    'prov1_5',
    'prov1_6',
    'prov1_7',

    #proverbe 2 en arabe
    'prov2_1',
    'prov2_2',
    'prov2_3',
    'prov2_4',
    'prov2_5',
    'prov2_6',

    #proverbe 3 en arabe
    'prov3_1',
    'prov3_2',
    'prov3_3',
    'prov3_4',
    'prov3_5',
    #'prov3_6',
    #'prov3_7',


    #proverbe 1 en fr
    'prov4_1',
    'prov4_2',
    'prov4_3',
    'prov4_4',
    'prov4_5',
    'prov4_6',
    'prov4_7',
    'prov4_8',

    #proverbe 2 en fr
   # 'PROV5_1',
    'PROV5_2',
    'PROV5_3',
    'PROV5_4',
   # 'PROV5_5',
    'PROV5_6',
    'PROV5_7',
    'PROV5_8',
    'PROV5_9'



)
#proverbe 1 en arabe
t_prov1_1 = r'شحال'
t_prov1_2 = r'ما'
t_prov1_3 = r'طال'
t_prov1_4 = r'الليل'
t_prov1_5 = r'ك'
t_prov1_6 = r'يطلع'
t_prov1_7 = r'النهار'


#proverbe 2 en arabe
t_prov2_1 = r'أنا'
t_prov2_2 = r'فران '
t_prov2_3= r'و'
t_prov2_4=r'قاد'
t_prov2_5=r'ب'
t_prov2_6=r'حوما'


# proverbe 3 en arabe
t_prov3_1 = r'لي '
#t_prov3_2 = r'ك'
t_prov3_2=r'يعيش'
t_prov3_3= r'أناني'
#t_prov3_=r'ك'
t_prov3_4=r'يموت'
t_prov3_5=r'وحداني'




#proverbe 1 en fr
t_prov4_1 = r'on|ON|On'
t_prov4_2 = r'ne|NE'
t_prov4_3= r'change|CHANGE'
t_prov4_4=r'jamais|JAMAIS'
t_prov4_5=r'une|UNE'
t_prov4_6=r'equipe|équipe|EQUIPE'
t_prov4_7=r'qui|QUI|Qui'
t_prov4_8=r'gagne|GAGNE'


#### proverbe 2 fr
#t_PROV5_1 = r'qui|QUI'
t_PROV5_2 = r'cherche|CHERCHE'
t_PROV5_3 = r'la|LA'
t_PROV5_4 = r'lune|LUNE'
#t_PROV5_5 = r'ne|NE'
t_PROV5_6 = r'voit|VOIT'
t_PROV5_7 = r'pas|PAS'
t_PROV5_8 = r'les|LES'
t_PROV5_9 = r'étoiles|etoiles|ETOILES'



###### lex ##############
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"le mot /l'lphabet/ alharf / alkalima : ne se trouve pas dans la literature '{t.value[0]}'\n")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.lineno = 1


# entrer data
#utilisateur = input()
#data=input()

data = sys.argv[1]
data = sys.argv[1].encode('utf-8').decode('utf-8')
data = arabic_reshaper.reshape(data)




lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    # Utilize arabic_reshaper to reshape Arabic characters for console display
    reshaped_text = arabic_reshaper.reshape(tok.value)
    #print(f'le mot / alkalimat :{reshaped_text}\n')
    print(f'le mot / alkalimat : {reshaped_text}\n')

######## yacc ############

import ply.yacc as yacc

# Define the start symbol
start = 'proverb'

# Define the grammar rules
def p_proverb(p):
    '''
    proverb : prov1
            | prov2
            | prov3
            | prov4
            | prov5
    '''

### semantique et yacc et traduction
def p_prov1(p):
    '''
    prov1 : prov1_1 prov1_2 prov1_3 prov1_4 prov1_5 prov1_6 prov1_7
    '''
    if p[1] == 'شحال' and p[2] == 'ما' and p[3] == 'طال' and p[4] == 'الليل' and p[5] == 'ك' and p[6] == 'يطلع' and p[7] == 'النهار':
        print("al jomla sahiha fil maana\n ")
        print("la traduction de ce proverbe en francais est : Aussi longtemps que la nuit dure, le jour finira par se lever.\n")
    else:
        print("al jomla ghayr sahiha fil maana \n")


def p_prov2(p):
    '''
    prov2 : prov2_1 prov2_2 prov2_3 prov2_4 prov2_5 prov2_6
    '''
    if p[1] == 'أنا' and p[2] == 'فران' and p[3] == 'و' and p[4] == 'قاد' and p[5] == 'ب' and p[6] == 'حوما' :
        print("al jomla sahiha fil maana \n")
        print("la traduction de ce proverbe en francais est : Je suis capable du meilleur et du pire.\n")
    else:
        print("al jomla ghayr sahiha fil maana \n")

def p_prov3(p):
    '''
    prov3 : prov3_1 prov1_5 prov3_2 prov3_3 prov1_5 prov3_4 prov3_5
    '''
    if p[1] == 'لي' and p[2] == 'ك' and p[3] == 'يعيش' and p[4] == 'أناني' and p[5] == 'ك'and p[6] == 'يموت'and p[7] =='وحداني':
        print("al jomla sahiha fil maana\n")
        print("la traduction de ce proverbe en francais est : L'égoïsme, c'est la solitude qui se prépare à sa propre mort\n")
    else:
        print("al jomla ghayr sahiha fil maana\n ")

def p_prov4(p):
    '''
    prov4 : prov4_1 prov4_2 prov4_3 prov4_4 prov4_5 prov4_6 prov4_7 prov4_8
    '''
    if p[1] == 'on'  and p[2] == 'ne' and p[3] == 'change' and p[4] == 'jamais' and p[5] == 'une' and p[6] == 'equipe' and p[7] =='qui' and p[8] =='gagne' or p[1] == 'ON'  and p[2] == 'NE' and p[3] == 'CHANGE' and p[4] == 'JAMAIS' and p[5] == 'UNE' and p[6] == 'EQUIPE' and p[7] =='QUI' and p[8] =='GAGNE' :
        print("la phrase est correct\n")
        print("la traduction de ce proverbe en anglais est : Never change a winning team .\n")#ajouter maj
    else:
        print("la phrase n'est pas correct\n")


def p_prov5(p):
    '''prov5 : prov4_7 PROV5_2 PROV5_3 PROV5_4 prov4_2 PROV5_6 PROV5_7 PROV5_8 PROV5_9'''
    if p[1] == 'qui' and p[2] == 'cherche' and p[3] == 'la' and p[4] == 'lune' and p[5] == 'ne' and p[6] == 'voit' and p[7] == 'pas' and p[8] == 'les' and p[9] == 'etoiles' or p[9] == 'étoiles' or p[1] == 'QUI' and p[2] == 'CHERCHE' and p[3] == 'LA' and p[4] == 'LUNE' and p[5] == 'NE' and p[6] == 'VOIT' and p[7] == 'PAS' and p[8] == 'LES' and p[9] == 'ETOILES':
        print("la phrase est sémantiquement correcte\n")
        print("la traduction de ce proverbe en anglais est : He who seeks the moon does not see the stars.\n")
    else:
        print("la phrase n'est pas sémantiquement correcte\n")




"""def p_prov5(p):
    '''
    prov5 : prov5_1 prov5_2 prov5_3 prov5_4 prov5_5 prov5_6 prov5_7 prov5_8 prov5_9
    '''
    if p[1] == 'qui' and p[2] == 'cherche' and p[3] == 'la' and p[4] == 'lune' and p[5] == 'ne' and p[6] == 'voit' and p[7] == 'pas' and p[8] == 'les' and p[9] == 'etoiles' or p[1] == 'QUI' and p[2] == 'CHERCHE' and p[3] == 'LA' and p[4] == 'LUNE' and p[5] == 'NE' and p[6] == 'VOIT' and p[7] == 'PAS'and p[8] == 'LES'and p[9] == 'ETOILES':
        print("la phrase est semantiquement correct")
        print("la traduction de ce proverbe en anglais est : He who seeks the moon does not see the stars.")  # ajouter maj
    else:
       print("la phrase n'est pas semantiquement  correct")"""


##########################

if data == 'on' or data=='ne' or data=='change' or data=='jamais' or data=='une' or data=='qui' or data=='gagne'\
        or data == 'on ne ' or data == 'change jamais'or data == 'une equipe'or data == 'equipe'or data == 'qui gagne'\
        or data == 'on ne change' :
    print("Voulez-vous dire : on ne change jamais une équipe qui gagne ?\n")

if data == 'qui' or data=='cherche' or data=='la' or data=='lune' or data=='ne' or data=='voit' or data=='pas'\
        or data == 'les' or data == 'etoiles'or data == 'étoiles'or data == 'qui cherche'or data == 'la lune'\
        or data == 'ne voit pas les etoiles' :
    print("Voulez-vous dire : qui cherche la lune ne voit pas les étoiles ?\n")



if data == 'شحال' or data=='ما' or data=='طال' or data=='الليل' or data=='ك' or data=='يطلع' or data=='النهار'\
        or data == 'شحال الليل ' or data == 'النهار يطلع ':
    print("Voulez-vous dire : شحال ما طال الليل كيطلع النهار ؟\n")


if data == 'أنا' or data=='فران' or data=='و' or data=='قاد' or data=='بحوما' or data=='أنا فران' or data=='قاد بحوما'\
        or data == 'شحال الليل ' or data == 'النهار يطلع ':
    print("Voulez-vous dire : أنا فران و قاد بحوما\n")



if data == 'لي' or data=='كيعيش' or data=='و' or data=='أناني' or data=='كيموت' or data=='وحداني'  or data == 'يموت وحداني ' or data == 'كيعيش أناني ':
    print("Voulez-vous dire :  لي كيعيش أناني كيموت وحداني ?\n")


"""
keywords = ['on', 'ne', 'change', 'jamais', 'une', 'equipe', 'qui', 'gagne']

if any(keyword1 in data for keyword1 in keywords):
    print("Voulez-vous dire : on ne change jamais une équipe qui gagne ?\n")


# Définir un ensemble de mots-clés
keywords_set = {'شحال', 'ما', 'طال', 'الليل', 'ك', 'يطلع', 'النهار'}

# Vérifier si au moins un mot-clé est présent dans la chaîne data
if any(keyword in data for keyword in keywords_set):
    print("Voulez-vous dire : شحال ما طال الليل كيطلع النهار ؟\n")



# Définir un ensemble de mots-clés
keywords_set1 = {'أنا', 'فران', 'و', 'قاد', 'ب', 'حوما'}

# Vérifier si au moins un mot-clé est présent dans la chaîne data
if any(keyword in data for keyword in keywords_set1):
    print("Voulez-vous dire : أنا فران و قاد بحوما ؟\n")


# Pour le premier bloc
keywords_set_2 = {'لي', 'ك', 'يعيش', 'أناني', 'يموت', 'وحداني'}
if any(keyword in data for keyword in keywords_set_2):
    print("Voulez-vous dire : لي كيعيش أناني كيموت وحداني ?\n")

# Pour le deuxième bloc
keywords_set_3 = {'qui', 'cherche', 'la', 'lune', 'ne', 'voit', 'pas', 'les', 'etoiles', 'étoiles'}
if any(keyword2 in data for keyword2 in keywords_set_3):
    print("Voulez-vous dire : qui cherche la lune ne voit pas les étoiles ?\n")

"""
# Error rule for syntax errors
def p_error(p):
    print(f"l'orde des mots  / tartib alkalimat : n'est pas correct \n")
    #print(f"l'orde de mot  / tartib alkalima: n'est pas correct : {p.type}")
# Build the parser
parser = yacc.yacc()

# Parse the input data
result = parser.parse(data)

# Output the parsed result
print(result)