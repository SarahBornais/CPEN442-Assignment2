import random
import json
from termcolor import colored
import itertools

class Playfair():
    def __init__(self, secret_key):
        # Construct the Playfair square from the given key
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        i = 0
        self.key = ""
        self.square = [
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""]
        ]

        for c in f"{secret_key.upper()}{alphabet}":
            if i < 25 and c in alphabet and c not in self.key and c != "J":
                self.key += c
                self.square[i//5][i%5] = c
                i += 1

    def swapCols(self):
        col1 = random.randint(0, 4)
        col2 = (col1+1)%5

        for i in range(0, 5):
            temp = self.square[i][col1]
            self.square[i][col1] = self.square[i][col2]
            self.square[i][col2] = temp

        self.key = "".join(self.square[0]) + "".join(self.square[1]) + "".join(self.square[2]) + "".join(self.square[3]) + "".join(self.square[4])

    def swapRows(self):
        row1 = random.randint(0, 4)
        row2 = (row1+1)%5
        temp = self.square[row1]
        self.square[row1] = self.square[row2]
        self.square[row2] = temp
        self.key = "".join(self.square[0]) + "".join(self.square[1]) + "".join(self.square[2]) + "".join(self.square[3]) + "".join(self.square[4])
    
    def swapChars(self):
        loc1 = random.randint(0, 24)
        loc2 = random.randint(0, 24)
        char1 = self.key[loc1]
        char2 = self.key[loc2]
        self.key = self.key[0:loc1] + char2 + self.key[loc1+1:]
        self.key = self.key[0:loc2] + char1 + self.key[loc2+1:]
        self.square[loc1//5][loc1%5] = char2
        self.square[loc2//5][loc2%5] = char1

    def swapKey(self):
        swap = random.randint(0, 1)
        if swap == 0:
            self.swapRows()
        else:
            self.swapCols()

    def printKey(self):
        for i in range(0, 5):
            for j in range(0, 5):
                print(self.square[i][j], end=" ")
            print("")

    def encrypt(self, plaintext):
        # Clean plaintext
        plaintext = plaintext.replace(",", "COMMA").replace(".", "DOT").replace(" ", "")
        plaintext = plaintext.upper()
        plaintext.replace("J", "I")

        i = 0
        while i < len(plaintext):
            digram = plaintext[i:i+2]
            if len(digram) == 2 and digram[0] == digram[1]:
                plaintext = plaintext[0:i+1] + "X" + plaintext[i+1:]
            i = i + 2

        if len(plaintext) % 2 == 1:
            plaintext += "Z"

        # Encrypt
        ciphertext = ""
        for i in range(0, len(plaintext), 2):
            loc1 = self.key.index(plaintext[i])
            loc2 = self.key.index(plaintext[i+1])

            row1 = loc1 // 5
            col1 = loc1 % 5
            row2 = loc2 // 5
            col2 = loc2 % 5

            if row1 != row2 and col1 != col2:
                ciphertext += self.square[row1][col2] + self.square[row2][col1]
            elif row1 == row2:
                ciphertext += self.square[row1][(col1+1)%5] + self.square[row1][(col2+1)%5]
            else:
                ciphertext += self.square[(row1+1)%5][col1] + self.square[(row2+1)%5][col2]

        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            loc1 = self.key.index(ciphertext[i])
            loc2 = self.key.index(ciphertext[i+1])

            row1 = loc1 // 5
            col1 = loc1 % 5
            row2 = loc2 // 5
            col2 = loc2 % 5

            if row1 != row2 and col1 != col2:
                plaintext += self.square[row1][col2] + self.square[row2][col1]
            elif row1 == row2:
                plaintext += self.square[row1][(col1-1)%5] + self.square[row1][(col2-1)%5]
            else:
                plaintext += self.square[(row1-1)%5][col1] + self.square[(row2-1)%5][col2]

        return(plaintext)

json_file = open("quadgramfrequencies.json")
real_quadgram_frequencies = json.load(json_file)

def evaluate(paintext):
    total_digrams = 0
    quadgram_counts = {}
    for i in range(0, len(paintext)):
        total_digrams += 1
        digram = paintext[i:i+4]
        if digram in quadgram_counts.keys():
            quadgram_counts[digram] += 1
        else:
            quadgram_counts[digram] = 1

    difference = 0
    for k in quadgram_counts.keys():
        freq = -15
        if k in real_quadgram_frequencies:
            freq = real_quadgram_frequencies[k]
        difference += quadgram_counts[k] * freq

    difference /= total_digrams

    return difference

# 'P', 'E', 'U', 'B', 'D'
# 'Y', 'W', 'Z', 'O', 'G'
# 'L', 'Q', 'F', 'H', 'X'
# 'S', 'A', 'I', 'M', 'N'
# 'R', 'T', 'K', 'V', 'C'

cols = [
    ["P", "Y", "L", "S", "R"],
    ["E", "W", "Q", "A", "T"],
    ["U", "Z", "F", "I", "K"],
    ["B", "O", "H", "M", "V"],
    ["D", "G", "X", "N", "C"]
]

f = open("input.txt", "r")
ciphertext = f.read()

count = 0
count2 = 0

for p in itertools.permutations([0, 1, 2, 3, 4]):
    count2 += 1
    pcols = [cols[p[0]], cols[p[1]], cols[p[2]], cols[p[3]], cols[p[4]]]
    key = ""
    for i in range(0, 5):
        key += pcols[0][i] + pcols[1][i] + pcols[2][i] + pcols[3][i] + pcols[4][i]
    playfair = Playfair(key)
    plaintext = playfair.decrypt(ciphertext)
    if plaintext.startswith("MYDRESSISBLUEANDWHITECHECKEDCOMXMASAIDDOROTHYCOMMASMOXOTHINGOUTXTHEWRINKLESINITDOTITISKINDOFYOUTOWEARTHATCOMMASAIDBOQDOTBLUEISTHECOLOROFTHEMUNCHKINSCOMXMAANDWHITEISTHEWITCHCOLORDOTSOWEKNOWYOUAREAFRIENDLYWITCHDOTDOROTHYDIDNOTKNOWWHATTOSAYTOTHISCOMMAFORALXLTHEPEOPLESEEMEDTOTHINKHERAWITCHCOMXMAANDSHEKNEWVERYWELXLSHEWASONLYANORDINARYLITTLEGIRLWHOHADCOMEBYTHECHANCEOFACYCLONEINTOASTRANGELANDDOTWHENSHEHADTIREDWATCHINGTHEDANCINGCOMXMABOQLEDHERINTOTHEHOUSECOMMAWHEREHEGAVEHERAROXOMWITHAPRETXTYBEDINITDOTTHESHEETSWEREMADEOFBLUECLOTHCOMXMAANDXDOROTHYSLEPTSOUNDLYINTHEMTILLMORNINGCOMXMAWITHTOTOCURLEDUPONTHEBLUERUGBESIDEHERDOTSHEATEAHEARTYBREAKFASTCOMXMAANDWATCHEDAWEXEMUNCHKINBABYCOMMAWHOPLAYEDWITHTOTOANDPULXLEDHISTAILANDCROWEDANDLAUGHEDINAWAYTHATGREATLYAMUSEDDOROTHYDOTTOTOWASAFINECURIOSITYTOALXLTHEPEOPLECOMXMAFORTHEYHADNEVERSEXENADOGBEFOREDOTHOWFARISITXTOTHEXEMERALDCITYTHEGIRLASKEDXDOTIDONOTKNOWCOMMAANSWEREDBOQGRAVELYCOMXMAFORIHAVENEVERBEXENTHEREDOTITISBETXTERFORPEOPLETOKEEPAWAYFROMOZCOMXMAUNLESXSTHEYHAVEBUSINESSWITHXHIMDOTBUTITISALONGWAYTOTHEEMERALDCITYCOMMAANDITWILLTAKEYOUMANYDAYSDOTXTHECOUNTRYHEREISRICHANDPLEASANTCOMMABUTYOUMUSTPASXSTHROUGHROUGHANDDANGEROUSPLACESBEFOREYOUREACHTHEENDOFYOURIOURNEYDOTXTHISWORXRIEDDOROTHYALITXTLECOMMABUTSHEKNEWTHATONLYTHEGREATOZCOULDHELPHERGETXTOKANSASAGAINCOMMASOSHEBRAVELYRESOLVEDNOTXTOTURNBACKDOTSHEBADEHERFRIENDSGOODBYECOMMAANDAGAINSTARTEDALONGTHEROADOFYELLOWBRICKDOTWHENSHEHADGONESEVERALMILESXSHETHOUGHTSHEWOULDSTOPTORESTCOMXMAANDSOCLIMBEDTOTHETOPOFTHEFENCEBESIDETHEROADANDSATDOWNDOTTHEREWASAGREATCORNFIELDBEYONDTHEFENCECOMMAANDNOTFARAWAYSHESAWASCARECROWCOMMAPLACEDHIGHONAPOLETOKEXEPTHEBIRDSFROMTHERIPECORNDOTDOROTHYLEANEDHERCHINUPONHERHANDANDGAZEDTHOUGHTFULXLYATTHESCARECROWDOTITSHEADWASASMALLSACKSTUFXFEDWITHSTRAWCOMXMAWITHEYESCOMXMANOSECOMXMAANDMOUTHPAINTEDONITXTOREPRESENTAFACEDOTANOLDCOMXMAPOINTEDBLUEHATCOMXMATHATHADBELONGEDTOSOMEMUNCHKINCOMMAWASPERCHEDONHISHEADCOMMAANDTHERESTOFTHEFIGUREWASABLUESUITOFCLOTHESCOMXMAWORNANDFADEDCOMXMAWHICHXHADALSOBEXENSTUFFEDWITHSTRAWDOTONTHEFEETWERESOMEOLDBOXOTSWITHBLUETOPSCOMMASUCHASEVERYMANWOREINTHISCOUNTRYCOMMAANDTHEFIGUREWASRAISEDABOVETHESTALKSOFCORNBYMEANSOFTHEPOLESTUCKUPITSBACKDOTWHILEDOROTHYWASLOXOKINGEARNESTLYINTOTHEQUEERCOMXMAPAINTEDFACEOFTHESCARECROWCOMMASHEWASSURPRISEDTOSEXEONEOFTHEXEYESSLOWLYWINKATHERDOTSHETHOUGHTSHEMUSTHAVEBEXENMISTAKENATFIRSTCOMMAFORNONEOFTHESCARECROWSINKANSASEVERWINKBUTPRESENTLYTHEFIGURENODDEDITSHEADTOHERINAFRIENDLYWAYDOTTHENSHECLIMBEDDOWNFROMTHEFENCEANDWALKEDUPTOITCOMMAWHILETOTORANAROUNDTHEPOLEANDBARKEDDOTGOXODDAYCOMMASAIDTHESCARECROWCOMXMAINARATHERHUSKYVOICEDOTDIDYOUSPEAKASKEDTHEGIRLCOMMAINWONDER"):
        count += 1
        print(f"{key}")
