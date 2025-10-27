from ftplib import FTP

def ftp_client2():
    ftp = FTP('192.168.202.48') 
    ftp.login('alumno', 'ciud4d')  
    
    filename = 'calendario.pdf'
    with open(filename, 'wb') as file:
        ftp.retrbinary(f'RETR {filename}', file.write)  
    
    print(f"Archivo '{filename}' descargado con éxito.")
    ftp.quit()

if __name__ == "__main__":
    ftp_client2()
