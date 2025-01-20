import os
import sys
from yt_dlp import YoutubeDL

def download_tiktok(url, output_path="/sdcard/TikTok/"):
    # Pastikan folder output ada
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Konfigurasi yt-dlp
    options = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',
        'format': 'best',
        'quiet': False,
    }

    with YoutubeDL(options) as ydl:
        try:
            print("\n[INFO] Mendownload video dari TikTok...")
            ydl.download([url])
            print(f"\n[SUKSES] Video berhasil diunduh ke: {output_path}")
        except Exception as e:
            print(f"\n[ERROR] Terjadi kesalahan: {str(e)}")

def main():
    print("====================================================")
    print("       TikTok/Youtube/facebook/Dll Downloader (UI)       ")
    print("===================================================")
    print("1. Masukkan URL video TikTok/Dll")
    print("2. Tekan ENTER untuk mulai download")
    print("-------------------------------------")

    url = input("Masukkan URL Vidio: ")

    if url.strip() == "":
        print("[ERROR] URL tidak boleh kosong!")
        sys.exit(1)

    print("\nMemulai proses download...")
    download_tiktok(url)

if __name__ == "__main__":
    main()
