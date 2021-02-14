import config as conf

def main():
    config = conf.Config()

    nama = input("Masukkan Nama Anda ")
    username = input("Masukkan Username Anda ")
    password = input("Masukkan Password Anda ")
    role = input("Masukkan Role Anda ")
    departement = input("Masukkan departement Anda ")

    config.create(nama, username, password, role, departement)

if __name__ == '__main__':
    main()
