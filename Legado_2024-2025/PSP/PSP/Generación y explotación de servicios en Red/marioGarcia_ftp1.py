from ftplib import FTP

def ftp_client_1():
    print("Conectando al servidor FTP...")
    ftp = FTP('ftp.osuosl.org')
    ftp.login()
    ftp.cwd('pub/ubuntu/dists/xenial')
    
    print("Listando contenido de la carpeta...")
    ftp.retrlines('LIST')
    
    archivo = 'Release.gpg'
    print(f"Descargando {archivo}...")
    with open(archivo, 'wb') as f:
        ftp.retrbinary(f'RETR {archivo}', f.write)
    
    print(f"¡{archivo} descargado con éxito!")
    ftp.quit()

if __name__ == "__main__":
    ftp_client_1()
