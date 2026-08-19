#!/usr/bin/env python3
"""Penguji `kirim_ajuan.py` — jalanin: `python uji_kirim_ajuan.py`

Nol butuh pustaka tambahan, nol nyentuh jaringan, nol butuh kunci. Ada di sini karena repo
panduan nol punya robot pemeriksa: kalau alat ini rusak, nol ada yang ngasih tau selain uji ini.

Yang dijaga paling utama: **contoh ajuan yang DITERBITIN di repo ini wajib lolos alatnya
sendiri.** Contoh yang ditolak server bikin tiap orang yang nurut panduan kena tolak.
"""

import copy
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kirim_ajuan as K  # noqa: E402

CONTOH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "references", "contoh-ajuan.json")
gagal = []


def cek(nama, syarat, catatan=""):
    print(("  OK   " if syarat else "  GAGAL") + "  " + nama + (("  -- " + catatan) if catatan and not syarat else ""))
    if not syarat:
        gagal.append(nama)


def contoh():
    with open(CONTOH, encoding="utf-8") as f:
        return json.load(f)


def masalah_langkah(data):
    """Cuma keluhan soal langkah. `periksa` nembak semua aturan sekaligus."""
    return [m for m in K.periksa(data, arah="turun", nama_saya="Nur") if "langkah" in m.lower()]


print("== contoh ajuan yang diterbitin ==")
data = contoh()
cek("contoh-ajuan.json bawa langkah", bool(data.get("langkah")),
    "contoh tanpa langkah = tiap orang yang nurut panduan kena tolak server")
cek("tiap langkah di contoh punya judul + kata kunci",
    all(str(s.get("judul") or "").strip() and str(s.get("kata_kunci") or "").strip()
        for s in data.get("langkah") or []))
cek("contoh lolos periksa() tanpa keluhan langkah", masalah_langkah(data) == [],
    str(masalah_langkah(data)))

print("== langkah wajib ==")
tanpa = contoh()
tanpa.pop("langkah", None)
cek("ajuan tanpa langkah ditolak", masalah_langkah(tanpa) != [])

kosong = contoh()
kosong["langkah"] = []
cek("daftar langkah kosong ditolak", masalah_langkah(kosong) != [])

bukan = contoh()
bukan["langkah"] = "bukan daftar"
cek("langkah bukan-daftar ditolak, nol meledak", masalah_langkah(bukan) != [])

print("== tiap langkah wajib kepakai ==")
for isian in ("judul", "kata_kunci"):
    rusak = contoh()
    rusak["langkah"] = copy.deepcopy(rusak["langkah"])[:1]
    rusak["langkah"][0][isian] = "  "
    keluhan = masalah_langkah(rusak)
    cek("langkah tanpa " + isian + " ditolak", keluhan != [])
    if isian == "kata_kunci" and keluhan:
        cek("keluhan kata kunci nyebut judul langkahnya",
            any(str(rusak["langkah"][0]["judul"]) in m for m in keluhan), str(keluhan))

print("== langkah beneran kekirim ke server ==")
badan = K.badan_permintaan(contoh())
cek("badan permintaan bawa langkah", bool(badan.get("langkah")),
    "sebelum tambalan ini `badan_permintaan` MBUANG langkah diam-diam")
if badan.get("langkah"):
    cek("nilai langkah kekirim utuh",
        badan["langkah"][0].get("kata_kunci") == contoh()["langkah"][0]["kata_kunci"])

kotor = contoh()
kotor["langkah"] = copy.deepcopy(kotor["langkah"])[:1]
kotor["langkah"][0]["rahasia"] = "jangan ikut kekirim"
kotor["langkah"][0]["hp"] = "628000000000"
badan_kotor = K.badan_permintaan(kotor)
cek("isian asing di langkah nol ikut kekirim",
    set(badan_kotor["langkah"][0]) <= {"judul", "bobot", "repo", "kata_kunci"},
    str(sorted(badan_kotor["langkah"][0])))

print("== arah sebaliknya (anti alarm palsu) ==")
cek("langkah lengkap nol diprotes", masalah_langkah(contoh()) == [])
bobot_kosong = contoh()
bobot_kosong["langkah"] = copy.deepcopy(bobot_kosong["langkah"])
bobot_kosong["langkah"][0]["bobot"] = ""
cek("bobot kosong tetap sah (dibagi rata otomatis)", masalah_langkah(bobot_kosong) == [])
repo_kosong = contoh()
repo_kosong["langkah"] = copy.deepcopy(repo_kosong["langkah"])
repo_kosong["langkah"][0]["repo"] = ""
cek("gudang kode kosong tetap sah", masalah_langkah(repo_kosong) == [])

print()
if gagal:
    print("GAGAL " + str(len(gagal)) + " uji: " + ", ".join(gagal))
    sys.exit(1)
print("SEMUA LULUS")
