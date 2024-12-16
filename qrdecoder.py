from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
import os

def generate_qrcode(method):
    if method.lower() == "buat":
        #input form user
        data_buat = input("masukkan text yang ingin di jadikan qrcode: ")
        data_buat_nama = input("masukkan nama file (tanpa ekstensi seperti .png atau yang lainnya): ")
        lokasi_buat = input("masukkan lokasi file untuk disimpan: ")

        #validasi direktori

        if not os.path.exists(lokasi_buat):
            print("lokasi tidak ditemukan")
            return



        data_buat_hasil = qrcode.make(data_buat)
        data_buat_path = os.path.join(lokasi_buat, f"{data_buat_nama}.png")

        try:
            data_buat_hasil.save(data_buat_path)
            print(f"qrcode berhasil dibuat di {data_buat_path}")

        except Exception as e:
            print(f"terjadi kesalahan {e}")
    #decode
    elif method.lower() == "baca":
        #input form user
        data_baca = input("masukkan lokasi qrcode yang ingin dibaca: ")
        try:
            image = Image.open(data_baca)
            baca_data = decode(image)
            if baca_data:
                for baca in baca_data:
                    print()
                    print(baca.data.decode("utf-8"))
                    print()
            else:
                print("qrcode tidak terdeteksi")
        except Exception as e:
            print(f"terjadi kesalahan {e}")
    #jika input tidak diketahui
    else:
        print("perintah tidak diketahui")
if __name__ == "__main__":
    method = input("ingin buat qrcode atau membaca qrcode (buat/baca): ")
    generate_qrcode(method)