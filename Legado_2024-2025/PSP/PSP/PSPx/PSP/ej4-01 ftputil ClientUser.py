import ftputil

FTP_HOST = "192.168.1.46"
FTP_USER = "alumno"
FTP_PASS = "ciud4d"

def main():
    with ftputil.FTPHost(FTP_HOST, FTP_USER, FTP_PASS) as sitio:
        names = sitio.listdir(sitio.curdir)
        for name in names:
            print(name)
        sitio.download("calendario.pdf", "calendario2.pdf")
        sitio.upload("Release.gpg", "ReseaseNew4.gpg")

if __name__ == "__main__":
    main()
