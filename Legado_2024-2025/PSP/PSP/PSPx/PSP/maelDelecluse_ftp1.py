from ftplib import FTP

def ftp_client1():
    ftp = FTP('ftp.osuosl.org') 
    ftp.login() 
    ftp.cwd('pub/ubuntu/dists/xenial')
    
    print("Contenido del directorio:")
    ftp.retrlines('LIST')
    
    filename = 'Release.gpg'
    with open(filename, 'wb') as file:
        ftp.retrbinary(f'RETR {filename}', file.write) 
    
    print(f"Archivo '{filename}' descargado con éxito.")
    ftp.quit()

if __name__ == "__main__":
    ftp_client1()