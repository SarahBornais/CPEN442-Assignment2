from termcolor import colored

f = open("input.txt", "r")
input = f.read()

cipher_freqs = ["VQ", "IM", "QB", "HV", "WV", "VG", "MS", "BG", "PT", "BP", "NH", "TP", "VW", "AK", "NS", "CG", "PA", "DT", "ZB", "KS", "DA", "VX", "TE", "QT", "AR", "VY", "CQ", "EN", "WT", "AM", "QP", "QM", "YV", "ST", "MA", "GM", "ML", "DQ", "SL", "WQ", "NA", "ZO", "BA", "WE", "OQ", "FM", "CX", "ZH", "EW", "HY", "MY", "YB", "TB", "AD", "EC", "FP", "GR", "DI", "SA", "EG", "UN", "WR", "MG", "BU", "NT", "NE", "DZ", "PW", "AN", "GH", "VR", "YH", "NR", "HZ", "QL", "AP", "TQ", "MH", "GD", "TD", "AC", "PI", "ZA", "UB", "SF", "QV", "SQ", "UQ", "CS", "RC", "SN", "CE", "UK", "OH", "CP", "QW", "CI", "TS", "PN", "DW", "SK", "VT", "WD", "QS", "AY", "BW", "PB", "QI", "WM", "ET", "IK", "KA", "BE", "LK", "UD", "OZ", "RA", "PQ", "PU", "QU", "MP", "NU", "IC", "TV", "QR", "EB", "SR", "EQ", "BQ", "MT", "LR", "DE", "IT", "BX", "YM", "TU", "GT", "NL", "ES", "RY", "FS", "TI", "CD", "KE", "EM", "GB", "BT", "AI", "WZ", "DB", "PX", "LO", "GC", "PL", "WS", "LS", "RQ", "SE", "RW", "GN", "ER", "KD", "PS", "MD", "ME", "SM", "CW", "GP", "OL", "PR", "KL", "ZG", "FL", "OX", "LZ", "NW", "MN", "WN", "IN", "XP", "VO", "ZV", "VL", "TN", "RT", "LM", "NZ", "PK", "XK", "UX", "NK", "IP", "OS", "RS", "QK", "SO", "PC", "EK", "XE", "PH", "EI", "IQ", "WO", "VF", "SX", "QY", "KN", "HQ", "HU", "ZS", "AV", "HS", "MQ", "OP", "WP", "ED", "MI", "ZY", "ZN", "VC", "XW", "VP", "SW", "NB", "SG", "PE", "IB", "LV", "CL", "PF", "BL", "HR", "YZ", "PO", "OE", "GX", "GV", "YS", "SU", "WU", "IZ", "RI", "XL", "BN", "YP", "BY", "ZK", "HO", "ZI", "AB", "MO", "ZD", "RP", "FR", "CU", "WA", "PY", "YA", "RE", "AU", "GA", "PD", "ZM", "TC", "RZ", "BH", "PG", "IR", "XR"]
plain_freqs = ["HE", "TH", "OM", "CO", "XA", "MX", "IN", "ER", "OT", "AT", "OU", "DO", "ND", "ED", "IT", "RE", "TO", "AS", "AN", "HA", "NG", "ON", "ES", "NT", "TI", "TX", "EA", "EN", "EC", "ST", "SA", "AR", "AI", "ET", "OR", "TE", "IS", "SH", "DT", "SE", "LE", "ID", "HI", "UT", "VE", "AL", "XN", "OF", "LX", "EX", "BE", "TA", "NO", "XH", "AX", "OW", "HO", "YO", "EL", "ME", "NE", "TS", "XO", "WA", "RO", "WH", "AD", "OX", "SO", "DI", "US", "NC", "CH", "XE", "LI", "EW", "UR", "EM", "RI", "RA", "WI", "RS", "TC", "DE", "RT", "NA", "MA", "TW", "FO", "DA", "LY", "AB", "XI", "IL", "SX", "GH", "EO", "KE", "RY", "SI", "HT", "GA", "MO", "UL", "LD", "AY", "LA", "WO", "WE", "CA", "CE", "LO", "IM", "NI", "NS", "FT", "UN", "IC", "SC", "GE", "EF", "DC", "EH", "AW", "TD", "EI", "EP", "AC", "GO", "OS", "RC", "IO", "EY", "RD", "AG", "GR", "EG", "PE", "XT", "TU", "DS", "TR", "IG", "AM", "XL", "DX", "YC", "KI", "IR", "IE", "UC", "UP", "QU", "BU", "TL", "PR", "BO", "OC", "EV", "YT", "AP", "FI", "CT", "EB", "AV", "MI", "TY", "PO", "IF", "PL", "RG", "GI", "OH", "OP", "XS", "OL", "GT", "XK", "OI", "DB", "SU", "DH", "RM", "CK", "FE", "SW", "DN", "NY", "XC", "UG", "PA", "DW", "FA", "YD", "TG", "UE", "XR", "RK", "YS", "AF", "YA", "XY", "LF", "GU", "FX", "SN", "SP", "KN", "XD", "PI", "MU", "XP", "SD", "NB", "RH", "AK", "DR", "TB", "FU", "FR", "GC", "TM", "IV", "GS", "RX", "YW", "WN", "YI", "OD", "BL", "PX", "DY", "OV", "TF", "PT", "NL", "TN", "MP", "EK", "NK", "CR", "XM", "DL", "UD", "UM", "DU", "AH", "NH", "IK", "RW", "OA", "RP", "KT", "RN", "VI", "GL", "YP", "CU", "EQ", "NW", "OB", "JE", "HC", "SL", "FC", "CL", "OJ", "YR", "YE", "JU", "GD", "TP", "KS", "AU", "OE", "RF", "RU", "PH", "HR", "MS", "BY", "DG", "MY", "RL", "IA", "SF", "DF", "PU", "NF", "KC", "NU", "DM", "UI", "NX", "AO", "BA", "HU", "BI", "IB", "BR", "HX", "SB", "LT", "LS", "FY", "MC", "BX", "OG", "SM", "FH", "MB", "WD", "XU", "LC", "VO", "KA", "MT", "WC", "WS", "WT", "OY", "DV", "YM", "HY", "FS", "XW", "YB", "SG", "LK", "SK", "UA", "EJ", "FL", "CI", "XF", "YL", "EU", "HS", "YH", "IW", "UK", "XB", "WX", "PS", "FD", "HD", "DP", "CX", "UB", "ZE", "KO", "YF", "OK", "NR", "BS", "WR", "GW", "TV", "SV", "IH", "NP", "WL", "LW", "GX", "LU", "KL", "GN", "YG", "PC", "RB", "MN", "CW", "NM", "IP", "SR", "VA", "GF", "YU", "PY", "GB", "SY", "HW", "YN", "GM", "LP", "UW", "YX", "AJ", "FM", "HM", "GP", "UH", "UF", "GY", "TK", "KD", "IZ", "FW", "NV", "MW", "MF", "UO", "MD", "KY", "BT", "LV", "RV", "TQ", "IX", "TJ", "GV", "WM", "DJ", "HL", "YK", "XV", "KH", "HP", "ZX", "FP", "AE", "JO", "XZ", "KW", "KM", "RQ", "DQ", "XG", "KU", "UZ", "DK", "SQ", "FG", "OQ", "LR", "XX", "PD", "WF", "FB", "HF", "FV", "YV", "PB", "YJ", "SJ", "WB", "HN", "NQ", "WY", "BJ", "HB", "MH", "CY", "ZA", "KF", "MG", "ZI", "FN", "WV", "JA", "FK", "LM", "WP", "HG", "AQ", "ML", "XJ", "IU", "UV", "PW", "GJ", "AZ", "GQ", "WU", "KJ", "BD", "KR", "NJ", "YQ", "VY", "UJ", "PG", "KP", "OZ", "LN", "QD", "KB", "BM", "UX", "PV", "KQ", "LB", "CB", "PN", "PM", "PK", "VD", "HV", "RJ", "XQ", "LZ", "KX", "LG", "WG", "MR", "KV", "ZY", "JC", "CD", "CS", "LH", "FJ", "MQ", "TZ", "T"]

mappings = {
    "DO": "ED",
    "VQ": "TH",
    "IM": "MA",
    "QB": "HE",
    "HV": "OM",
    "WV": "OT",
    "VG": "CO",
    "MS": "AN",
    # "BG": "DO",
    "PT": "ER",
    "BP": "DO",
    "NH": "MX",
    "TP": "RE",
    "VW": "TO",
    # "AK": "ED",
    # "NS": "IT",
    # "CG": "DO",
    # "PA": "AT",
    # "DT": "EC",
    # "ZB": "AN",
    # "KS": "HA",
    # "DA": "NG",
    # "VX": "ON",
    # "TE": "ES",
    # "QT": "NT",
    # "AR": "TI",
    # "VY": "TX",
    # "CQ": "EA",
    # "EN": "EN",
    # "WT": "EC",
    # "AM": "ST",
    # "QP": "SA",
    # "QM": "AR",
    # "YV": "XT",
    # "ST": "ET",
    # "MA": "OR",
    # "GM": "RE",
    # "ML": "IS",
    # "DQ": "SH",
    # "SL": "DT",
    # "WQ": "SE",
    # "NA": "LE",
    # "ZO": "ID",
    # "BA": "HI",
    # "WE": "UT",
    # "OQ": "VE",
    # "FM": "AL",
    # "CX": "XN",
    # "ZH": "OF",
    # "EW": "LX",
    # "HY": "EX",
    # "MY": "BE",
    # "YB": "TA",
    # "TB": "NO",
    # "AD": "XH",
    "EC": "DT",
    # "FP": "OW",
    "GR": "EC",
    # "DI": "YO",
    # "SA": "EL",
    # "EG": "ME",
    # "UN": "NE",
    # "WR": "TS",
    # "MG": "ER",
    # "BU": "WA",
    # "NT": "RO",
    # "NE": "WH",
    # "DZ": "AD",
    # "PW": "OX",
    # "AN": "SO",
    # "GH": "DI",
    # "VR": "US",
    # "YH": "NC",
    # "NR": "CH",
    # "HZ": "XE",
    # "QL": "LI",
    # "AP": "TA",
    # "TQ": "UR",
    # "MH": "EM",
    # "GD": "RI",
    # "TD": "CE",
    # "AC": "WI",
    # "PI": "RS",
    # "ZA": "TC",
    # "UB": "DE",
    # "SF": "RT",
    # "QV": "NA",
    # "SQ": "MA",
    # "UQ": "TW",
    # "CS": "FO",
    # "RC": "DA",
    # "SN": "LY",
    "CE": "TD",
    # "UK": "XI",
    # "OH": "IL",
    # "CP": "SX",
    # "QW": "GH",
    # "CI": "EO",
    # "TS": "KE",
    # "PN": "RY",
    # "DW": "SI",
    # "SK": "HT",
    # "VT": "GA",
    # "WD": "MO",
    # "QS": "UL",
    # "AY": "LD",
    # "BW": "AY",
    "PB": "OD",
    # "QI": "WO",
    # "WM": "WE",
    # "ET": "CA",
    # "IK": "CE",
    # "KA": "LO",
    # "BE": "IM",
    # "LK": "NI",
    # "UD": "NS",
    # "OZ": "FT",
    # "RA": "UN",
    # "PQ": "IC",
    # "PU": "SC",
    # "QU": "GE",
    # "MP": "EF",
    # "NU": "DC",
    # "IC": "EH",
    # "TV": "AW",
    # "QR": "TD",
    # "EB": "EI",
    # "SR": "EP",
    # "EQ": "AC",
    # "BQ": "GO",
    # "MT": "OS",
    # "LR": "RC",
    "DE": "IO",
    # "IT": "EY",
    # "BX": "RD",
    # "YM": "AG",
    # "TU": "GR",
    # "GT": "EG",
    # "NL": "PE",
    # "ES": "XT",
    # "RY": "TU",
    # "FS": "DS",
    # "TI": "TR",
    # "CD": "IG",
    # "KE": "AM",
    # "EM": "XL",
    # "GB": "OD",
    # "BT": "YC",
    # "AI": "KI",
    # "WZ": "IR",
    # "DB": "IE",
    # "PX": "UC",
    # "LO": "UP",
    # "GC": "QU",
    # "PL": "BU",
    # "WS": "TL",
    # "LS": "PR",
    # "RQ": "BO",
    # "SE": "OC",
    # "RW": "EV",
    # "GN": "YT",
    # "ER": "AP",
    "KD": "CU",
    "PS": "RL",
    # "MD": "EB",
    # "ME": "AV",
    "SM": "NA",
    # "CW": "TY",
    # "GP": "PO",
    # "OL": "IF",
    # "PR": "PL",
    # "KL": "RG",
    # "ZG": "GI",
    # "FL": "OH",
    # "OX": "OP",
    # "LZ": "XS",
    # "NW": "OL",
    # "MN": "GT",
    # "WN": "XK",
    # "IN": "OI",
    # "XP": "DB",
    # "VO": "SU",
    # "ZV": "DH",
    # "VL": "RM",
    # "TN": "CK",
    # "RT": "FE",
    # "LM": "SW",
    # "NZ": "DN",
    # "PK": "NY",
    # "XK": "XC",
    # "UX": "UG",
    # "NK": "PA",
    # "IP": "DW",
    # "OS": "FA",
    # "RS": "YD",
    # "QK": "TG",
    # "SO": "UE",
    # "PC": "XR",
    # "EK": "RK",
    # "XE": "YS",
    # "PH": "AF",
    # "EI": "YA",
    # "IQ": "XY",
    # "WO": "LF",
    # "VF": "GU",
    # "SX": "FX",
    # "QY": "SN",
    # "KN": "SP",
    # "HQ": "KN",
    # "HU": "XD",
    # "ZS": "PI",
    # "AV": "MU",
    # "HS": "XP",
    # "MQ": "SD",
    # "OP": "NB",
    # "WP": "RH",
    # "ED": "AK",
    "MI": "AM",
    # "ZY": "TB",
    # "ZN": "FU",
    # "VC": "FR",
    # "XW": "GC",
    # "VP": "TM",
    # "SW": "IV",
    # "NB": "GS",
    # "SG": "RX",
    # "PE": "YW",
    # "IB": "WN",
    # "LV": "YI",
    # "CL": "OD",
    # "PF": "BL",
    # "BL": "PX",
    # "HR": "DY",
    # "YZ": "OV",
    # "PO": "TF",
    # "OE": "PT",
    # "GX": "NL",
    "GV": "OC",
    # "YS": "MP",
    # "SU": "EK",
    # "WU": "NK",
    # "IZ": "CR",
    # "RI": "XM",
    # "XL": "DL",
    # "BN": "UD",
    # "YP": "UM",
    # "BY": "DU",
    # "ZK": "AH",
    # "HO": "NH",
    # "ZI": "IK",
    # "AB": "RW",
    # "MO": "OA",
    # "ZD": "RP",
    # "RP": "KT",
    # "FR": "RN",
    # "CU": "VI",
    # "WA": "GL",
    # "PY": "YP",
    # "YA": "CU",
    # "RE": "EQ",
    # "AU": "NW",
    # "GA": "OB",
    # "PD": "JE",
    # "ZM": "HC",
    # "TC": "SL",
    # "RZ": "FC",
    # "BH": "CL",
    # "PG": "OJ",
    # "IR": "YR",
    # "XR": "YE"
}

# for i in range(0, len(cipher_freqs)):
#     mappings[cipher_freqs[i]] = plain_freqs[i]

# for m in mappings.keys():
#     print(f"\"{m}\": \"{mappings[m]}\",")

for i in range(0, len(input), 2):
    digraph = input[i:i+2]
    color = "grey"
    if digraph in mappings.keys():
        digraph = mappings[digraph]
        color = "green"
    print(colored(digraph, color), end=" ")
