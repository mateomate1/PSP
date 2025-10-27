#Conexión a un servidor FTP
import ftplib

FTP_HOST = "ftp.osuosl.org"
FTP_USER = ""
FTP_PASS = ""

ftp = ftplib.FTP(FTP_HOST)
ftp.login(passwd="anonymous@")  # Acceso anónimo
ftp.encoding = "utf-8"

print(ftp.getwelcome())  # Mensaje de bienvenida

#Subir archivos al servidor
def enviarFicheroBinario(ftp, filename):
    file = open(filename, "rb")
    ftp.storbinary(f"STOR {filename}", file)

def enviarFichero(ftp, filename):
    file = open(filename, "rb")
    ftp.storlines(f"STOR {filename}", file)
# Descargar archivos del servidor
def descargarFicheroBinario(ftp, filename):
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    localfile.close()

def descargarFichero(ftp, filename):
    localfile = open(filename, 'w')
    ftp.retrlines('RETR ' + filename, localfile.write)
    localfile.close()
#Listar directorios en el servidor
def listarDirectorio(ftp):
    try:
        ftp.login()
        files = []
        ftp.dir(files.append)
        print(files)
    except ftplib.all_errors as e:
        print('FTP error:', e)

def etoquees(block):
    print("CB +", block)


def main():
    ftp = ftplib.FTP(FTP_HOST)#, FTP_PASS, FTP_USER)
    #ftp = ftplib.FTP_TLS(FTP_HOST)
    ftp.login(passwd="anonymous@")
    ftp.encoding = "utf-8"
    wcMsg = ftp.getwelcome()
    print(wcMsg)
    response = ftp.retrlines("NLST", etoquees)
    print(response)
    print("---")
    #response = ftp.mlsd()   
    response = []
    #ftp.retrlines('MLSD', response.append)
    ftp.dir(response.append)
    for elem in response:
        print(elem)
    print("---")    
    #Cambiar de directorio y descargar archivos
    print(ftp.pwd())
    ftp.cwd('pub/ubuntu/dists/xenial')
    response = []
    ftp.dir(response.append)
    for elem in response:
        print(elem)
    descargarFichero(ftp, "Release.gpg")
    ftp.quit()

main()
