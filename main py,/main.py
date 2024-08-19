import random

def donustur_secim(secim):
    # Seçimleri Taş-Kağıt-Makas'tan Marvel karakterlerine dönüştür
    if secim == 'Hulk':
        return 'Hulk'
    elif secim == 'Thor':
        return 'Thor'
    elif secim == 'Iron Man':
        return 'Iron Man'
    else:
        return secim

def determine_winner(player, computer):
    if player == computer:
        return "Beraberlik"  # Beraberlik
    elif (player == 'Hulk' and computer == 'Iron Man') or \
         (player == 'Thor' and computer == 'Hulk') or \
         (player == 'Iron Man' and computer == 'Thor'):
        return "Player"  # Oyuncu kazandı
    else:
        return "Computer"  # Bilgisayar kazandı

def tas_kagit_makas_ECEMNUR_SEVIM():
    print("Marvel Karakterleri Taş-Kağıt-Makas Oyunu!\n")
    print("Kurallar: Hulk, Thor, Iron Man seçebilirsiniz.")
    print("\tOyun bilgisayara karşı oynanır")
    print("\tTaş: Hulk, Kağıt: Thor, Makas: Iron Man olarak tanımlanmıştır.")
    print("\tHulk, Thor'u yener.")
    print("\tThor, Iron Man'i yener.")
    print("\tIron Man, Hulk'u yener.")
    print("\tİki tur kazanan oyunu kazanacaktır.")
    
    choices = ['Hulk', 'Thor', 'Iron Man']
    
    player_wins = 0
    computer_wins = 0

    while True:
        player_round_wins = 0
        computer_round_wins = 0

        while player_round_wins < 2 and computer_round_wins < 2:
            player_choice = input("Hulk, Thor veya Iron Man seçin: ").title()
            player_choice = donustur_secim(player_choice)

            if player_choice not in choices:
                print("Geçersiz seçim, lütfen tekrar deneyin.")
                continue

            computer_choice = random.choice(choices)

            print(f"Oyuncu seçimi: {player_choice}")
            print(f"Bilgisayar seçimi: {computer_choice}")

            winner = determine_winner(player_choice, computer_choice)

            if winner == "Player":
                print("Bu turu kazandınız!")
                player_round_wins += 1
            elif winner == "Computer":
                print("Bu turu bilgisayar kazandı!")
                computer_round_wins += 1
            else:
                print("Bu tur berabere!")

        if player_round_wins == 2:
            print("Tebrikler! Oyunu kazandınız!")
            player_wins += 1
        elif computer_round_wins == 2:
            print("Üzgünüm, bilgisayar oyunu kazandı.")
            computer_wins += 1

        # Bilgisayarın yeniden oynamayı isteyip istemediğini rastgele belirleyelim
        computer_play_again = random.choice(['evet', 'hayır'])

        # Bilgisayar yeniden oynamak istemiyorsa, oyunu bitir
        if computer_play_again == 'hayır':
            print(f"Sonuç: Oyuncu {player_wins} - Bilgisayar {computer_wins}")
            print("Oyunu oynadığınız için teşekkürler. Çok eğlenceliydi!")
            break

        # Bilgisayar yeniden oynamak istiyorsa, oyuncuya tekrar sor
        play_again = input("Yeniden oynamak ister misiniz? (evet/hayır): ").lower()
        if play_again != 'evet':
            print(f"Sonuç: Oyuncu {player_wins} - Bilgisayar {computer_wins}")
            print("Oyunu oynadığınız için teşekkürler. Çok eğlenceliydi!")
            break

# Oyunu başlat
tas_kagit_makas_ECEMNUR_SEVIM()



