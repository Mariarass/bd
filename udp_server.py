import socket
import sqlite3

HOST = 'localhost' 
PORT = 12344
ss=0
unic=0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#создание потокового сокета для сетевого протокола IPv4
    s.bind((HOST, PORT))#связь  сокет с  хостом и портом с помощью метода bind
    
    while True:#несколько раз клиент
        
        s.listen()# запустим для данного сокета режим прослушивания (слушает свой порт)
        connect, addr = s.accept() #принять подключение с помощью метода accept
       
        with connect:
            if ss==0:
                print('Клиент подключен ', addr[0])
                ss=1
                
            while True:#несколько раз запросы
                con = sqlite3.connect('bus.db')
                cur = con.cursor()#бд
                try:
                    
                    data= connect.recv(18384)# принимает количество байт для чтения
                    
                    
                    if not data:
                        break
                    
                    result=data.decode(encoding='utf-8')
                    if result=='close':
                        print('Клиент отключен')
                        unic=1
                        ss=0
                    try:
                        cur.execute(data.decode(encoding='utf-8'))
                    except:
                        result=''
                        
                    data = str(cur.fetchall())

                    da=list(result.split())
                    
                    if da[0]=='SELECT':
                        print('Клиент выполнил выборку данных ',result)
                    if da[0]=='INSERT':
                        print('Клиент выполнил добавление данных ',result)
                    if da[0]=='DELETE':
                        print('Клиент выполнил удаление данных ',result)
                    if da[0]=='UPDATE':
                        print('Клиент выполнил обновление данных ',result)
                        
                    if data=='[]' and da[0]=='SELECT':
                        connect.sendall(bytes('0', encoding='utf-8'))  # Вернуть значение клиенту
                       
                    if data=='[]':
                        pass
  
                    else:
                        
                        connect.sendall(bytes(data, encoding='utf-8'))  # Вернуть значение клиенту
                    con.commit()
                    con.close()
                    
                except:
                    if unic ==1:
                        unic=0
                    else:
                        print('Ошибка')
                
              
    
