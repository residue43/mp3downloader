import os
import sys
import subprocess

def get_base_path():
    # Kod .exe olarak mı çalışıyor yoksa .py olarak mı kontrol et
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

def run_pipeline(batch_file="list.txt"):
    base_path = get_base_path()
    batch_path = os.path.join(base_path, batch_file)
    output_dir = os.path.join(base_path, "indirilenler")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not os.path.exists(batch_path):
        print(f"\nHATA: Lutfen '{batch_file}' dosyasini .exe ile ayni klasore koyun!")
        input("\nCikmak icin Enter'a basin...")
        return

    command = [
        "yt-dlp",
        "-x", "--audio-format", "mp3", "--audio-quality", "0",
        "-a", batch_path,
        "-o", f"{output_dir}/%(title)s.%(ext)s"
    ]

    print("\n--- İndirme İşlemi Başlıyor ---\n")
    subprocess.run(command)
    print("\n--- Tüm İşlemler Tamamlandı! ---")
    
    # Çift tıklandığında pencere hemen kapanmasın diye:
    input("\nKapatmak için Enter'a basın...")

if __name__ == "__main__":
    run_pipeline()