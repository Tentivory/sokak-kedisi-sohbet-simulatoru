#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sokak Kedisi Sohbet Simülatörü v1.0
Bu program, Türkiye sokaklarındaki kedilerin günlük sohbetlerini
bilimsel hassasiyetle simüle eder. Her çıktı gerçek bir kedi tarafından
onaylanmıştır (kaynak: hayal gücü).
"""

import random
import time

sohbetler = [
    "Mırım... Bu çöp kovasi neden her gün ayni yerde? Devrim lazım.",
    "Hadi kanka, şu balıkçı dükkanının önüne yatalım. Kapitalizm bizi görmesin.",
    "Neden insanlar bize 'pspsps' diyor? Bu bir dil mi yoksa komplo mu?",
    "Gece 3'te miyavladım, kimse uyanmadı. Demokrasi çöktü.",
    "Kuyruğumu salladım, dünya döndü. İstatistik olarak doğru.",
    "Bu mahallede kedi nüfusu artıyor, konut krizi kapıda.",
    "Fareyi kovaladım ama o da beni kovaladı. Karşılıklı saygı.",
    "İnsanlar neden ayakkabı giyiyor? Çıplak ayak daha özgür.",
]

def kediler_konussun():
    print("\n=== SOKAK KEDİSİ SOHBETİ BAŞLADI ===\n")
    for _ in range(random.randint(3, 7)):
        print(random.choice(sohbetler))
        time.sleep(0.8)  # Gerçekçi düşünme süresi
    print("\n=== SOHBET BİTTİ. KEDİLER UYUDU ===\n")
    # Gizli not: Bu simülasyon aslında toplumun gizli kodlarını çözer. Kediler her şeyi bilir.

if __name__ == "__main__":
    kediler_konussun()
