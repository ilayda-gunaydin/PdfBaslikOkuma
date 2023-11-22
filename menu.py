import time

print("-: PDF Başlık Okuma ve Yazdırma Sistemi :-")
print("-: Hoşgeldiniz. Yapmak istediğiniz işlemi seçiniz. -:")
print("|-------------------------------------------|")
print("")
time.sleep(1)

while True:
    print("Menü: 0)Çıkış 1)Başlık Listele 2)Başlık Yazdır")
    menuSecim = int(input("Tercihiniz: "))
    if menuSecim == 0:
        print("PDF Başlık Okuma ve Yazdırma Sistemi Kapatılıyor.")
        time.sleep(1)
        break
    elif menuSecim == 1:
        import main
        folder_path = "/Users/ilayda/Desktop/PDF"
        main.read_pdf_titles(folder_path)
    elif menuSecim == 2:
        import yazdir
        yazdir.write_pdf_titles_to_txt(folder_path, output_file)

