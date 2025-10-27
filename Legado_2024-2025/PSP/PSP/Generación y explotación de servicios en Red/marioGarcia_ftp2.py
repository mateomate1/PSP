from ftplib import FTP

def ftp_client_2():
    print("Conectando al servidor del profesor...")
    ftp = FTP('agustin.gonzalez@educa.madrid.org')  
    ftp.login(user='alumno', passwd='ciud4d')
    
    archivo = 'calendario.pdf'
    print(f"Descargando {archivo}...")
    with open(archivo, 'wb') as f:
        ftp.retrbinary(f'RETR {archivo}', f.write)
    
    print(f"¡{archivo} descargado con éxito!")
    ftp.quit()

if __name__ == "__main__":
    ftp_client_2()
