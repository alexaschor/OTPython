#!/usr/bin/env python3

import numpy as np
import nltk
import requests
import random

languages = ["de"]

ipas = []
ipa_reverse = {}

print("Starting data fetch...")
for l in languages:
    print(f"    Fetching language {l}...".ljust(40), end="", flush=True)
    url = f"https://github.com/open-dict-data/ipa-dict/raw/master/data/{l}.txt"
    data = requests.get(url, allow_redirects=True).content.decode('UTF-8')
    pairs = [p.split("\t") for p in data.split("\n")]
    len_before = len(ipas)
    for i in range(len(pairs)):
        if len(pairs[i]) == 2:
            word = pairs[i][0].strip()

            cleaned = pairs[i][1].replace("ˈ", "").replace("/", "").replace("ˌ", "")
            if "," in cleaned:
                for w in cleaned.split(","):
                    ipas.append(w.strip())
                    ipa_reverse[w.strip()] = f"{l}_{word}"
            else:
                ipas.append(cleaned.strip())
                ipa_reverse[cleaned.strip()] = f"{l}_{word}"
    print(f"Got {(len(ipas) - len_before):,} IPA strings. Total = {len(ipas):,}")


print("Some of the words and their origin languages:")
random.shuffle(ipas)
for i in ipas[:20]:
    print(f"    '{i}'".ljust(60), f"'{ipa_reverse[i]}'")


def invertDict(d):
    return {v: k for k, v in d.items()}


# =======================
#   GENERATION METHODS
# =======================

# ZH: g->k
# DE:
#       g->g
#       (a, o:, u:, a: , )g# -> X
#       (I E, e: , i: , ae, )g# -> ç

devoice_dict = {
    "z" : "s",
    "d" : "t",
    "ʒ" : "ʃ",
    "v" : "f",
    "b" : "p",
    "g" : "k",
}

def devoice(segment):
    for v in list(voicing_pairs.keys()):
        voicing_pairs[voicing_pairs[v]] = v

    if segment in voicing_pairs:
        return voicing_pairs[segment]
    else:
        return None

print(switchVoicing("s"))
