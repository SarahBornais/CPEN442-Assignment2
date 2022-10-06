from disjoint_set import DisjointSet

mappings = {
    "OD": "DE",
    "DO": "ED",
    "VQ": "TH",
    "IM": "MA",
    "QB": "HE",
    "HV": "OM",
    "WV": "OT",
    "VG": "CO",
    "MS": "AN",
    "PT": "ER",
    "BP": "ED",
    "NH": "MX",
    "TP": "RE",
    "VW": "TO",
    "AK": "IT",
    "VX": "CH",
    "TE": "AT",
    "AR": "ST",
    "WT": "EA",
    "GM": "ON",
    "ML": "SH",
    "DQ": "EX",
    "BA": "EM",
    "OQ": "WH",
    "EW": "TE",
    "EC": "DT",
    "FP": "LU",
    "GR": "YC",
    "DI": "UN",
    "EG": "DW",
    "BU": "EB",
    "DZ": "UG",
    "AN": "SI",
    "TQ": "AW",
    "UB": "BE",
    "QV": "HT",
    "CE": "TD",
    "UK": "KI",
    "CP": "RD",
    "QS": "LA",
    "PB": "DE",
    "QI": "FA",
    "TV": "RT",
    "DE": "UP",
    "IT": "AK",
    "KD": "CU",
    "PS": "RL",
    "MD": "NB",
    "ME": "AB",
    "SM": "NA",
    "MQ": "AH",
    "OP": "YB",
    "WP": "YE",
    "MI": "AM",
    "GV": "OC",
    "YP": "PR",
    "SO": "MY",
    "PC": "DR",
    "PA": "ES",
    "MP": "SB",
    "CG": "ND",
    "DT": "EC",
    "RC": "CK",
    "AM": "SA",
    "NU": "ID",
    "BG": "DO",
    "VY": "RO",
    "AI": "SM",
    "GH": "OX",
    "FM": "HI",
    "CX": "NG",
    "ZB": "OU",
    "CQ": "TX",
    "WQ": "EW",
    "KS": "RI",
    "IC": "NK",
    "QP": "LE",
    "SN": "NI",
    "NA": "IS",
    "ZH": "OF",
    "WZ": "YO",
    "EK": "UT",
    "ZO": "OW",
    "QM": "HA",
    "VR": "TC",
    "OH": "BO",
    "XE": "QD",
    "PH": "BL",
    "DB": "UE",
    "YH": "OL",
    "YV": "OR",
    "SA": "NS",
    "HY": "LO",
    "MY": "SO",
    "QW": "WE",
    "CI": "KN",
    "EI": "UA",
    "IQ": "AF",
    "DA": "EN",
    "PX": "DL",
    "WO": "YW",
    "LO": "HY",
    "UN": "DI",
    "GC": "DN",
    "WR": "YT",
    "NR": "SC",
    "HZ": "FO",
    "TS": "RA",
    "QL": "LX",
    "QR": "LT",
    "EB": "PE",
    "YB": "OP",
    "AP": "SE",
    "NS": "IN",
    "VF": "KH",
    "PN": "DS",
    "TB": "VE",
    "PL": "RY",
    "SR": "LS",
    "QT": "WA",
    "SX": "NL",
    "WS": "YA",
    "MG": "NO",
    "ST": "AR",
    "LS": "YL",
    "RQ": "TL",
    "DW": "EG",
    "SK": "IR",
    "QY": "LW",
    "MH": "HO",
    "GD": "DC",
    "TD": "CE",
    "NT": "AC",
    "AD": "NE",
    "MA": "AS",
    "VT": "TR",
    "WD": "GE",
    "EQ": "TW",
    "KN": "CI",
    "HQ": "QL",
    "AC": "NT",
    "PI": "US",
    "BQ": "EH",
    "MT": "AV",
    "ZA": "WI",
    "SE": "AP",
    "RW": "TY",
    "WE": "ET",
    "AY": "SW",
    "NE": "AD",
    "BW": "EO",
    "HU": "FB",
    "GN": "DX",
    "LR": "YS",
    "ER": "PT",
    "ZS": "YI",
    "AV": "MT",
    "SF": "IL",
    "HS": "LM",
    "WM": "OA",
    "ED": "PU",
    "BX": "DH",
    "ET": "TA",
    "EN": "DA",
    "CW": "TG",
    "SL": "LY",
    "GP": "YD",
    "IK": "FI",
    "YM": "OS",
    "OL": "YH",
    "PR": "RS",
    "ZY": "OG",
    "SQ": "AL",
    "ZN": "GI",
    "TU": "KE",
    "KA": "TI",
    "VC": "TK",
    "GT": "WC",
    "XW": "QG",
    "VP": "RB",
    "KL": "RF",
    "BE": "EP",
    "SW": "AY",
    "LK": "FR",
    "ZG": "OZ",
    "NL": "SX",
    "FL": "HX",
    "NB": "MD",
    "UD": "BU",
    "PW": "EY",
    "SG": "NY",
    "PE": "DP",
    "IB": "MU",
    "ES": "PA",
    "LV": "HR",
    "OX": "GH",
    "RY": "SP",
    "UQ": "EF",
    "LZ": "FY",
    "CS": "RN",
    "OZ": "WO",
    "CL": "RX",
    "FS": "LI",
    "RA": "TS",
    "PF": "UL",
    "PQ": "EL",
    "BL": "PH",
    "TI": "KA",
    "NW": "AG",
    "MN": "AI",
    "CD": "NC",
    "HR": "LV",
    "KE": "TU",
    "EM": "BA",
    "YZ": "GO",
    "GB": "OD",
    "PO": "BY",
    "WN": "GA",
    "OE": "WB",
    "GX": "DG",
    "BT": "EV",
    "IN": "MI",
    "XP": "LD",
    "VO": "MB",
    "PU": "DB",
    "QU": "FE",
    "YS": "PL",
    "ZV": "OK",
    "SU": "IP",
    "VL": "RH",
    "WU": "ZE",
    "IZ": "FU",
    "TN": "CA",
    "RT": "CR",
    "RI": "KS",
    "XL": "FX",
    "LM": "HS",
    "BN": "DM",
    "BY": "PO",
    "NZ": "IG",
    "PK": "UR",
    "ZK": "UI",
    "XK": "FC",
    "UX": "DF",
    "NK": "IC",
    "HO": "OB",
    "ZI": "UF",
    "AB": "ME",
    "MO": "HB",
    "IP": "SU",
    "OS": "YM",
    "ZD": "GU",
    "RP": "SR",
    "FR": "LK",
    "CU": "KD",
    "RS": "SL",
    "WA": "EQ",
    "QK": "FT",
    "PY": "RP",
    "YA": "WS",
    "RE": "TP",
    "AU": "IE",
    "GA": "WN",
    "PD": "DU",
    "ZM": "OI",
    "TC": "RK",
    "RZ": "KY",
    "BH": "VO",
    "PG": "DY",
    "IR": "SK",
    "XR": "LC"
}

character_mappings = {}

for (k, v) in mappings.items():
    for i in range(0, 2):
        if v[i] not in character_mappings.keys():
            character_mappings[v[i]] = { k[i] }
        else:
            character_mappings[v[i]].add(k[i])

for (k, v) in character_mappings.items():
    print(f"{k} {v}")

rows = []

ds = DisjointSet()

for (k, v) in character_mappings.items():
    for c in v:
        if k in character_mappings[c]:
            ds.union(c, k)

print(list(ds.itersets()))

colmaps = {}

for (k, v) in character_mappings.items():
    for c in v:
        if not ds.connected(k, c):
            colmaps[k] = c
            print(f"{k}: {c}")


# 'P', 'E', 'U', 'B', 'D'
# 'Y', 'W', 'Z', 'O', 'G'
# 'L', 'Q', 'F', 'H', 'X'
# 'S', 'A', 'I', 'M', 'N'
# 'R', 'T', 'K', 'V', 'C'
