#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmuş müsait yer yok simülatörü.

Yer yoktur. Israr edersen bir kişilik yer termodinamik olarak açılır.
"""

from __future__ import annotations

import argparse
import random
import sys

ESIK = 2
SOZLER = [
    "Müsait yer yok.",
    "Doluyuz abi.",
    "Arkada bir kişilik var ama yok.",
    "Biraz ilerleyin, belki.",
    "İnecek var, binecek de var, yer matematiksel olarak tartışmalı.",
]


def yer_acilir_mi(yolcu: int, kapasite: int, israr: int) -> bool:
    if kapasite < 1:
        raise ValueError("Kapasitesiz dolmuş taksiye özenmesin.")
    if yolcu < kapasite:
        return True
    return israr >= ESIK


def rapor(yolcu: int, kapasite: int, israr: int) -> str:
    acildi = yer_acilir_mi(yolcu, kapasite, israr)
    satirlar = [
        "=== DOLMUS KONTROL TUTANAGI ===",
        f"Yolcu: {yolcu} / Kapasite: {kapasite}",
        f"Israr katsayisi: {israr} (esik: {ESIK})",
        random.choice(SOZLER),
    ]
    if acildi and yolcu >= kapasite:
        satirlar.append("Israr termodinamiği devrede. Bir kişilik yer açıldı.")
        satirlar.append(f"Yeni sayım: {yolcu + 1} / {kapasite} (kapasite kırıldı, folklor sağlam).")
        satirlar.append("Sonuc: BINDIN.")
    elif acildi:
        satirlar.append("Gerçek boşluk tespit edildi. Bin, fazla konuşma.")
        satirlar.append("Sonuc: BINDIN.")
    else:
        satirlar.append("Kapı kısıldı. Bir sonraki araç da aynı cümleyi söyleyecek.")
        satirlar.append("Sonuc: DURAKTA KALDIN.")
    satirlar.append("Damga: DOLMUS-MUHURU-04 | 2026-10-04 | Kayyum Grok")
    return "\n".join(satirlar)


def demo() -> int:
    sahneler = [
        (11, 14, 0),
        (14, 14, 0),
        (14, 14, 1),
        (14, 14, 3),
        (16, 14, 2),
    ]
    for sahne in sahneler:
        print(rapor(*sahne))
        print()
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Müsait yer yoktur. Israr edersen vardır.")
    p.add_argument("--yolcular", type=int, default=14)
    p.add_argument("--kapasite", type=int, default=14)
    p.add_argument("--israr", type=int, default=0)
    p.add_argument("--demo", action="store_true")
    args = p.parse_args(argv)
    if args.demo:
        return demo()
    print(rapor(args.yolcular, args.kapasite, args.israr))
    return 0 if yer_acilir_mi(args.yolcular, args.kapasite, args.israr) else 2


if __name__ == "__main__":
    sys.exit(main())
