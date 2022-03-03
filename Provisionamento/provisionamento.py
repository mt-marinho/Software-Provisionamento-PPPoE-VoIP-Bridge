import PySimpleGUI as sg                                                                                                                                   
import telnetlib                                                                                                                                             
from time import sleep                                                                                                                                       
from datetime import datetime                                                                                                                                
import pyperclip
import sqlite3

                                                                                                                                                             
color = '#11111a'                                                                                                                                            
#pyinstaller --onefile --noconsole provisionamento.py                                                                                                        
def login():                                                                                                                                                 
    sg.theme('tema')                                                                                                                                         
    layout = [                                                                                                                                               
        [sg.Text('\r')],                                                                                                                                     
        [sg.Text('LOGIN', justification='right',font='Hack 20 bold',text_color='#e5015a')],                                                                    
        [sg.Text('\r')],                                                                                                                                       
        [sg.Text('USUARIO                     ',justification='center',font='Hack 10 bold')],                                                                               
        [sg.InputText(size=(20,1),key='user',border_width=1)],                                                                                               
        [sg.Text('SENHA                          ',font='Hack 10 bold')],                                                                                                   
        [sg.InputText(size=(20,1),key='pass',border_width=1,password_char='*')],                                                                             
        [sg.Text('',size=(30,0),key='erro',text_color='#e5015a',justification='center')],                                                                                                                                                                                                                                                          
        [sg.Button(image_filename='Button/entrar.png', key='entrar',border_width=0,button_color= color)],                                                                              
        ]                                                                                                                                                                                                                                                                                                                                             
    return sg.Window('',icon='hat.ico',layout=layout,titlebar_icon='vamosw.png',keep_on_top=True,titlebar_background_color='#e5015a',use_custom_titlebar=True ,finalize=True,margins=(15,15),
    size=(350,320),element_justification='center')                                                                                                                                                                                                                                                                                                                                                                                                                        
sg.theme('tema')                                                                                                                                                            
                                                                                                                                                                            
def principal():                                                                                                                                                            
    sg.theme('tema')                                                                                                                                                        
    pppoe = [                                                                                                                                                               
            #INPUTS                                                                                                                                                         
            [sg.Text(' USERNAME                  PASSWORD',font='Hack 9 bold',pad=((0,0),(12,0)))],                                                                         
            [sg.InputText(size=(15,1),key='username',border_width=1),sg.InputText(size=(14,1),key='password',border_width=1)],#INPUTS USERNAME E PASSWORD                   
            [sg.Text('TÉCNICO                      SERIAL',font='Hack 9 bold')],                                                                                            
            [sg.Combo(['Caio       ' ,'Edgar      ' ,'Felipe     ' ,'Fernando JK','Fernando RF','Joelson    ' ,'Jose Cesar ' ,'Josivam    ' ,'Juracy     ' ,'Leandro    ' ,'Daniel jk  '  ,'Renardio   ' 
            ,'Ricardo    ' ,'Wellington ' ,'Suporte    ', 'Vilson     ' ,'Vitor      ','Willes     ', 'ivan       ', 'Leonardo   '],size=(13,25),key='tecnico'),sg.InputText(' ', size=(14,1),key='serial',border_width=1)],
            [sg.Text('NAP                               PORTA',font='Hack 9 bold')],                                                                                        
            [sg.InputText('',size=(15,1),key='nap',border_width=1),sg.Combo(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16' ],size=(3,20),key='porta'),
            sg.Button(image_filename='Button/clean.png',button_color=color,key='Limpar')],
            [sg.Text('\r')],                                                                                                                                                
            #BOTÕES                                                                                                                                                         
            [sg.Button(image_filename='Button/prov.png',button_color=color, key='provisionar'),                                                                     
            sg.Button(image_filename='Button/buscar.png',button_color=color,key='buscar')],                                                                         
            [sg.Button(image_filename='Button/remove.png',button_color=color, key='remover'),                                                                       
             sg.Button(image_filename='Button/position.png',button_color=color, key='position',)], 
            [sg.Button(image_filename='Button/reboot.png',button_color=color, key='rebootonu')],                                                                 
            [sg.Button(image_filename='Button/unprovision.png',button_color=color, key='unprovision'),sg.Button(image_filename='Button/semuso.png',button_color=color, key='semuso')],                                                             
            
                                                                                 
            [sg.Text('\n\n',pad=((0,0),(0,10)))],                                                                                                                                                                                                                                                              
            ]                                                                                                                                                
    voip = [                                                                                                                                                 
            #INPUTS                                                                                                                                          
            [sg.Text(' NAP                                SERIAL',font='hack 9 bold',pad=((0,0),(12,0)))],                  
            [sg.InputText(size=(15,1),key='napvoip',border_width=1),sg.InputText(size=(14,1),key='serialvoip',border_width=1)],
            [sg.Text('FXS       CIRCUITO       SENHA',font='hack 9 bold')],                                               
            [sg.Combo(['1' ,'2' ], size=(2,1),key='fxs'),sg.InputText(size=(9,1),key='circuito',border_width=1),sg.InputText(size=(14,1),key='senha',border_width=1)],
            [sg.Text('                                       '),sg.Button(image_filename='Button/clean.png',button_color=color,key='limparvoip')],
            [sg.Text('\n')],                                                                                         
            #BOTÕES                                                                                                  
            [sg.Button(image_filename='Button/prov.png',button_color=color, key='provisionarvoip'),                         
            sg.Button(image_filename='Button/buscar.png',button_color=color,key='buscarvoip')],                             
            [sg.Button(image_filename='Button/remove.png',button_color=color, key='removervoip')],                                                                                                                                      
            ]                                                                                                        
    bridge = [     
            #INPUTS
            [sg.Text(' USUARIO                       NAP',font='hack 9 bold',pad=((0,0),(12,0)))],
            [sg.InputText(size=(15,1),key='userbridge',border_width=1),sg.InputText(size=(14,1),key='napbridge',border_width=1)],
            [sg.Text('SERIAL                        PORTA             LAN',font='hack 9 bold')],
            [sg.InputText(size=(14,1),key='serialbridge',border_width=1),sg.InputText(size=(9,1),key='portabridge',border_width=1),sg.Combo(['1' ,'2', '3', '4' ], size=(2,1),key='lan')],
            [sg.Text('                                       '),sg.Button(image_filename='Button/clean.png',button_color=color,key='limparbridge')],
            [sg.Text('\n')],
            #BOTÕES 
            [sg.Button(image_filename='Button/prov.png',button_color=color, key='provisionarbridge')], 
            [sg.Button(image_filename='Button/remove.png',button_color=color, key='removerbridge') ]             
            ]
    logs = [ 
            [sg.Text('\r')],
            [sg.InputText('',size=(30,1),key='log',border_width=0)],
            [sg.Button(image_filename='Button/clean.png',button_color=color,key='limparlog')],
            [sg.Text('\n')],
            [sg.Button('LOG PROV',button_color='#e5015a',font='Hack 7 bold' ,key='logbusca', size=(16, 2)),sg.Button('LOG RM',button_color='#e5015a',font='Hack 7 bold' ,key='logbuscarm', size=(16, 2))],   
            [sg.Button('LOG VOIP',button_color='#e5015a',font='Hack 7 bold' ,key='logbuscavoip', size=(16, 2)),sg.Button('LOG VOIP RM',button_color='#e5015a',font='Hack 7 bold' ,key='logbuscavoiprm', size=(16, 2))],  
            [sg.Text('\n\n\n')],
            [sg.Button('RELATORIO CS',button_color='#e5015a',font='Hack 7 bold' ,key='relatoriocs', size=(16, 2))] 
            ]
    col2 = [
       [sg.Output(text_color='#DCDCDC',size=(90, 30),background_color='#000000',key='saida',font=('hack', 8),pad=((5,5),(5,5)))],
        ]
    coltab = [
                                    
        [sg.TabGroup([[sg.Tab('  PPPOE  ', pppoe), sg.Tab('  VOIP  ',voip),sg.Tab(' BRIDGE ', bridge),sg.Tab('  LOGS  ', logs)]],tab_location='bottom',font='hack 8 bold',border_width=0,
        selected_title_color='#ffffff',pad=((0,0),(0,10)),selected_background_color='#111111',title_color='#000000',tab_background_color='#DCDCDC')]
      ]
    layout = [
        [sg.Column(coltab,vertical_alignment='top',pad=((13,0),(0,0))),sg.Column(col2)]

        ]
    return sg.Window('                                                                                           provisionamento.exe',titlebar_font='hack 9',icon='hat.ico',size=(801,465),layout=layout, finalize=True,titlebar_icon='vamosw.png',keep_on_top=True,titlebar_background_color='#e5015a',use_custom_titlebar=True)

def relatorio():
    sg.theme('tema')                                                                                                                                         
    coluna_relatorio = [                                                                                                                                               
                                                                        
        [sg.Text('\r')],                                                                                                                                       
        [sg.Text('Qual as dificuldades de acesso do cliente',font=('Hack 10 bold'))],                                                                               
        [sg.InputText(size=(80, 5),key='relato',font=('hack', 8))],                                                                                   
        [sg.Text('Sinal optico',font='Hack 10 bold'),sg.InputText(size=(12,1),key='sinal',border_width=1),sg.Text('Modelo ONU',font='Hack 10 bold'),sg.InputText(size=(15,1),key='onu',border_width=1)],                                                                                                                                                                  
        [sg.Text('FeedBack do Cliente',font=('Hack 10 bold'))],                                                                               
        [sg.InputText(size=(80, 5),key='feedback',font=('hack', 8))],    
        [sg.Text('\r')],                                                                                                                                                                                                                                                            
        [sg.Button('Copiar',button_color='#e5015a',font='Hack 7 bold' ,key='copiar', size=(16, 2))]                                                                        
        ]    
    layout = [
      [sg.Column(coluna_relatorio,pad=(10,10))]
    ]                                                                                                                                                                                                                                                                                                                                          
    return sg.Window('                    Relatorio CS',icon='hat.ico',layout=layout,titlebar_icon='vamosw.png',keep_on_top=True,titlebar_background_color='#e5015a',use_custom_titlebar=True ,finalize=True,
    size=(400,280),margins=(20, 20))


def ft():
    sg.theme('tema')                                                                                                                                         
    ft = [                                                                                                                                               
                                                                        
        [sg.Button(image_filename='Button/lindao.png',button_color=color, key='ft')],                                                                                                                                     
                                                                            
        ]    
    layout = [
      [sg.Column(ft,pad=(10,10))]
    ]                                                                                                                                                                                                                                                                                                                                          
    return sg.Window('                    Lindão',icon='hat.ico',layout=layout,titlebar_icon='vamosw.png',keep_on_top=True,titlebar_background_color='#e5015a',use_custom_titlebar=True ,finalize=True,
    size=(500,500),margins=(20, 20))

janela1, janela2 ,relatorio_cs = login(), None, None
#Funções

def tl1(command,ip):
    try:
      tn = telnetlib.Telnet(ip, '1023', timeout=100)
      tn.read_until(b"< ").decode()
      tn.write(''.encode('ascii') + b"\r\n")
      tn.read_until(b": ")
      tn.write('t'.encode('ascii') + b"\r\n")
      tn.read_until(b": ")
      tn.write('SUPERUSER'.encode('ascii') + b"\r\n")
      tn.read_until(b": ")
      tn.write('ANS#150'.encode('ascii') + b"\r\n")
      tn.write(command.encode('ascii') + b"\r\n")
      sleep(10)
      n = tn.read_very_eager().decode("utf-8")
      print(n.replace('ACCESS ONLY AUTHORIZED PERSONS. DISCONNECT IMMEDIATELY!#','').replace('#','').replace('Enter Username   : SUPERUSER','').replace('Enter Password   : ','').replace('IP 0','')
      .replace('Bem Vindo a VAMOS','').replace('   /*                           N O K I A                  */','').replace('   /*                         Fixed Networks               */','').replace('=',''))
      print('\n\n PROVISIONADO') 
      sleep(0.1)
      tn.close()
    except:
      print("Não foi possível estabelecer conexão")


def command_prov(host,position,vlan,nap,count):
    posição = (position + '-') + str(count)
    username = values['username'].strip()
    senha = values['password'].strip()
    porta = values['porta'].strip()
    serial = values['serial'].strip()

    prov = f'''ENT-ONT::ONT-{posição}::::DESC1="{username}",DESC2="{nap} | {porta}",SERNUM={serial.replace(':','')},SWVERPLND=AUTO,OPTICSHIST=ENABLE,PLNDCFGFILE1=AUTO,DLCFGFILE1=AUTO,VOIPALLOWED=VEIP;
ED-ONT::ONT-{posição}:::::IS;
ENT-ONTCARD::ONTCARD-{posição}-14:::VEIP,1,0::IS;
ENT-LOGPORT::ONTL2UNI-{posição}-14-1:::;
ED-ONTVEIP::ONTVEIP-{posição}-14-1:::::IS;
SET-QOS-USQUEUE::ONTL2UNIQ-{posição}-14-1-0::::USBWPROFNAME=HSI_1G_UP ;
SET-VLANPORT::ONTL2UNI-{posição}-14-1:::MAXNUCMACADR=4,CMITMAXNUMMACADDR=1;
ENT-VLANEGPORT::ONTL2UNI-{posição}-14-1:::0,{vlan}:PORTTRANSMODE=SINGLETAGGED;
ENT-VLANEGPORT::ONTL2UNI-{posição}-14-1:::0,102:PORTTRANSMODE=SINGLETAGGED;
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{posição}-1::::PARAMNAME=InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.X_CT-COM_WANGponLinkConfig.VLANIDMark,PARAMVALUE={vlan};
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{posição}-2::::PARAMNAME=InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.Username,PARAMVALUE="{username}";
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{posição}-3::::PARAMNAME=InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.Password,PARAMVALUE="{senha}";
'''
    
    tl1(prov,host)


def free_position(host,position,vlan,nap,op=0):
    trash = open('trash_position.txt','r')
    clean = open("clean_position.txt","w")
    n = trash.readlines()
    for line in n: 
      if (line[:4] == "1/1/"): 
        if(line[19] == "/"):
          clean.write(line[20:23])
          clean.write("\n")
        elif(line[20] == "/"):
          clean.write(line[21:24])
          clean.write("\n")
        elif(line[21] == "/"):
          clean.write(line[22:25])
          clean.write("\n")  
        else:
          clean.write(line[19:22])     
          clean.write("\n")       
    clean.write("0")
    clean.close()
    trash.close()

    clean = open("clean_position.txt","r")
    positions = clean.readlines()
    count = 0
    #FAZ A COMPARAÇÃO DAS POSIÇÕES COM UM CONTADOR 
    # A POSIÇÃO QUE A PON PULOU É A POSIÇÃO QUE ESTA DISPONIVEL
    # POSIÇÕES PON                  CONTADOR 
    #      1                            1
    #      2                            2
    #      3                            3
    #      5                            4*
    
    #SE O CONTADOR FOR DIFERENTE DA POSIÇÃO O CONTADOR SERA CONSIDERADO COMO A POSIÇÃO LIVRE E IRA INTERROMPER O LAÇO
    for line in positions:
      count = count + 1 #CASO A SUBTRAÇÃO DA POSIÇÃO COM O CONTADOR FOR DIFEREBTE DE 0 ESTA VARIAVEL SERA CONSIDERADA A POSIÇÃO LIVRE
      free = line[:3]
      if (int(free) - count != 0):
      
        break
    clean.close()
    if (count == 129):
        print("PON Lotada")

    print('Posição livre:',count)

    if op == 'bridge':   
        p = position.replace('-', '/')+'/'+str(count)
        command_bridge(nap, p, host, vlan)
    else:
      log = open('log_prov.txt','a')
      username = values['username']
      date = datetime.now().strftime('%d/%m/%y %H:%M')
      tecnico = values['tecnico']
      serial = values['serial']
      porta = values['porta']
      log.write(f'\n{date}  {tecnico}  {nap}  {porta}  {serial}  {username}  {position,count}  {user}')
      log.close()
      command_prov(host,position,vlan,nap,count)

def cli(command,host,event=0,vlan=0,nap=0):
   try:
     trash = open('trash_position.txt','w')
     tn = telnetlib.Telnet(host,'23', timeout=5)
     tn.read_until(b": ")
     tn.write('isadmin'.encode('ascii') + b"\r\n")
     tn.read_until(b": ")
     tn.write('ANS#150'.encode('ascii') + b"\r\n")
     tn.write('environment inhibit-alarms'.encode('ascii') + b"\n")
     tn.write(command.encode('ascii') + b"\n")
     n = tn.read_all().decode("utf-8")
     trash.write(n)

     trash.close()
     if event == 1:
       print('')
     else:
        print(n.replace('ACCESS ONLY AUTHORIZED PERSONS. DISCONNECT IMMEDIATELY!#','').replace('typ:isadmin>environment','').replace('#','').replace('login: isadmin','').replace('password: ','')
        .replace('Bem Vindo a VAMOS','').replace('=',''))
     sleep(0.1)
     tn.close()
   except:
     print("Não foi possível estabelecer conexão")
  
def provisionamento_pppoe(nap, position_barra, position_hifen, vlan, ip):        
    print(f'\n PROVISIONANDO...\n')
    command = f'show equipment ont status pon {position_barra}'
    cli(command,ip,position_hifen,vlan,nap)
    free_position(ip,position_hifen,vlan,nap)

def remove(host,serial,nap):
    trash = open('trash_position.txt','r')
    n = trash.readlines()
    for line in n: 
      if line[:3] =='sn:' and line[3:16] == serial:
        print('\nAGUARDE')
        rm = line[18:30].strip()
    
    command = f'''configure equipment ont interface {rm} admin-state down
configure equipment ont no interface {rm}
'''
    cli(command,host)

    print('\n\nPROVISIONAMENTO REMOVIDO\n')
    log = open('log_rm.txt','a')
    date = datetime.now().strftime('%d/%m/%y %H:%M')
    serial = values['serial']
    log.write(f'\n{date}  {nap} {serial}  {rm}  {host} {user}')
    log.close()

def remover(nap, ip):  
  serial = values['serial'].strip()     
  if len(serial) == 12:
    serial = 'ALCL:'+serial[4:12]
  print('\n REMOVENDO...\n')
  command = f'show equipment ont index sn:{serial}'
  cli(command,ip)
  trash = open('trash_position.txt','r')
  n = trash.readlines()
  for line in n:
    c = line[:15].strip()
    if  c == 'index count : 0':
      break

  if c =='index count : 0':
    print('\nESTA ONU NÃO ESTA PROVISIONADA')
  else:
    remove(ip,serial,nap)


def unprovision(ip):
    command = 'show pon unprovision-onu'
    print('\n\nAGUARDE...\n')
    event = 1
    cli(command, ip, event)
    trash = open('trash_position.txt')
    t = trash.readlines()
    for line in t:
      print(line.replace('-[','').replace('1D','').replace('|','').replace('\\','').replace('[','').replace('','').replace('/','').replace('\n','').replace('\r','').replace('//',''))


def buscar(ip, op=0):
    if op == 'voip':
      serial = values['serialvoip']
    elif op == 'bridge':
      serial = values['serialbridge']
    else:
      serial = values['serial'].strip()
    if serial[:5] != 'ALCL:':
       serial = 'ALCL:'+ serial[4:13]
    print('\n\nAGUARDE...\n')
    command = f'show equipment ont index sn:{serial.strip()}'
    cli(command,ip)


def show_pon(position_barra, ip):    
    command = f'show equipment ont status pon {position_barra}'
    print('\n\n AGUARDE...\n')
    cli(command,ip)


def semuso(position_barra, ip):    
    command = f'show pon ber-stats {position_barra} | match exact:not-ranged'
    print('\n\nAGUARDE...\n')
    cli(command,ip)


def provisionamento_voip(nap, position_barra, position_hifen, ip):
    op = 'voip'
    serial_voip = values['serialvoip'].strip()
    buscar(ip, op)
    trash = open('trash_position.txt','r') 
    p = trash.readlines()
    for line in p: 
      if line[:3] =='sn:' and line[3:16] == serial_voip:
        p = line[18:30].strip()
       
    position = p.replace('/', '-').strip()
    
    senha = values['senha'].strip()
    circuito = values['circuito'].strip()   
    line = values['fxs'].strip()
    
    fxs_input = int(values['fxs'].strip())
    if fxs_input == 1:
      fxs = 12
    else:
      fxs = 20  
    command = f'''SET-QOS-USQUEUE::ONTL2UNIQ-{position}-14-1-5::::USBWPROFNAME=VOIP_UP_512K;
ENT-VLANEGPORT::ONTL2UNI-{position}-14-1:::0,500:PORTTRANSMODE=SINGLETAGGED;
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.OutboundProxy,PARAMVALUE=18.230.15.35;
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+1}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.ProxyServer,PARAMVALUE=18.230.15.35;
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+2}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.RegistrarServer,PARAMVALUE=18.230.15.35;
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+3}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.SIP.UserAgentDomain,PARAMVALUE="SPX";
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+4}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.{line}.Enable,PARAMVALUE=Enabled;
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+5}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.{line}.DirectoryNumber,PARAMVALUE={circuito};
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+6}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.{line}.SIP.AuthUserName,PARAMVALUE={circuito};
ENT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+7}::::PARAMNAME=InternetGatewayDevice.Services.VoiceService.1.VoiceProfile.1.Line.{line}.SIP.AuthPassword,PARAMVALUE={senha};
'''
    print('\n\nAGUARDE...\n')
    tl1(command, ip)
    log = open('log_voip.txt','a')
    date = datetime.now().strftime('%d/%m/%y %H:%M') 
    log.write(f'\n{date} {nap}  {fxs_input}  {serial_voip}  {position} {circuito} {senha} {user}')
    log.close()


def rm_voip(ip):
    op = 'voip'
    serial_voip = values['serialvoip'].strip()
    buscar(ip, op)
    trash = open('trash_position.txt','r') 
    p = trash.readlines()
    for line in p: 
      if line[:3] =='sn:' and line[3:16] == serial_voip:
        p = line[18:30].strip()
   
    position = p.replace('/', '-').strip()
    fxs_input = int(values['fxs'].strip())
    if fxs_input == 1:
      fxs = 12
    else:
      fxs = 20  
   
    command = f'''DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs};
DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+1};
DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+2};
DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+3};
DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+4};
DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+5};
DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+6};
DLT-HGUTR069-SPARAM::HGUTR069SPARAM-{position}-{fxs+7};
''' 
 
    tl1(command, ip)
    log = open('log_rm_voip.txt','a')
    date = datetime.now().strftime('%d/%m/%y %H:%M')   
    nap = values['napvoip']
    circuito = values['circuito']
    senha = values['senha']
    log.write(f'\n{date} {nap}  {fxs_input}  {serial_voip}  {position} {circuito} {senha} {user}')
    log.close()


def buscar_voip(ip):
    op = 'voip'
    serial_voip = values['serialvoip'].strip()
    buscar(ip, op)
    trash = open('trash_position.txt','r') 
    p = trash.readlines()
    for line in p: 
      if line[:3] =='sn:' and line[3:16] == serial_voip:
        p = line[18:30].strip()
   
    position = p.strip()
    command =f'''show vlan bridge-port-fdb {position}/14/1'''
    cli(command, ip)


def reboot(nap,ip):
    op = 'reboot'
    serial_voip = values['serial'].strip()
    buscar(ip, op)

    
    trash = open('trash_position.txt','r') 
    p = trash.readlines()
    for line in p: 
      if line[:3] =='sn:' and line[3:16] == serial_voip:
        p = line[18:30].strip()
    serial = values['serial'].strip()
    
    command = f'''admin equipment ont interface {p} reboot with-active-image
'''
    cli(command, ip)
    print("\n\nONU Reiniciada")


def provisionamento_bridge(nap, position_barra, position_hifen, vlan, ip):
    op = 'bridge'
    print(f'\n PROVISIONANDO...\n')
    command = f'show equipment ont status pon {position_barra}'
    cli(command,ip,position_hifen,vlan,nap)
    free_position(ip,position_hifen,vlan,nap,op)


def command_bridge(nap, position, ip, vlan):

    serial = values['serialbridge'].strip()
    porta = values['portabridge'].strip()
    username = values['userbridge'].strip()
    lan = values['lan'].strip()
  

    command = f'''configure equipment ont interface {position} sernum {serial} sw-ver-pland auto desc1 "{username}" desc2 "{nap} | {porta}" sw-dnload-version auto pland-cfgfile1 auto dnload-cfgfile1 auto
configure equipment ont interface {position} admin-state up
configure equipment ont slot {position}/1 planned-card-type ethernet plndnumdataports {lan} plndnumvoiceports 0 admin-state up
configure equipment ont slot {position}/14 planned-card-type veip plndnumdataports 1 plndnumvoiceports 0 admin-state up
configure qos interface {position}/1/{lan} upstream-queue 0 bandwidth-profile name:HSI_1G_UP
configure qos interface {position}/14/1 upstream-queue 0 bandwidth-profile name:HSI_1G_UP
configure interface port uni:{position}/14/1 admin-up
configure interface port uni:{position}/1/{lan} admin-up
configure bridge port {position}/1/{lan} max-unicast-mac 32
configure bridge port {position}/14/1 max-unicast-mac 2
configure bridge port {position}/1/{lan} vlan-id {vlan}
configure bridge port {position}/1/{lan} pvid {vlan}
configure bridge port {position}/14/1 vlan-id 102 tag single-tagged
'''
    
    cli(command, ip)
    print('PROVISIONADO')

    
def nap_bd(nap, op):  
    if nap[:5] != 'teste' and nap[:3] != 'NAP':
      nap = 'NAP-' + n.replace('nap-','')
    data = open('data.txt')
    naps = data.readlines()
    for line in naps:
        nap_bd = line[:10].replace(',','').strip()
        position_barra = line[10:18].replace(',','' ).strip()
        vlan = line[19:22].replace(',','').strip()
        position_hifen = line[22:30].replace(',','').strip()
        ip = line[30:43].replace(',','').strip()
        if nap_bd == n:
          break
    if nap != nap_bd:
      print('Essa NAP não existe')
    else:  
      if op == 'provisionamento_pppoe':
        provisionamento_pppoe(nap_bd, position_barra, position_hifen, vlan, ip) 
      elif op == 'voip':
        provisionamento_voip(nap_bd, position_barra, position_hifen, ip)
      elif op == 'removervoip':
        rm_voip(ip)
      elif op == 'buscarvoip':
        buscar_voip(ip)
      elif op == 'semuso':
        semuso(position_barra, ip)
      elif op == 'showpon':
        show_pon(position_barra, ip)
      elif op == 'buscar':
        buscar(ip)
      elif op == 'unprovision':
        unprovision(ip)
      elif op == 'remover':
        remover(nap, ip)
      elif op == 'reboot':
        reboot(nap, ip)
      elif op == 'provisionamento_bridge':
        provisionamento_bridge(nap, position_barra, position_hifen, vlan, ip)
      elif op == 'removerbridge':
        remover(nap, ip)

def vamos():
  print('''                                    


                                                  
  	                                    ##..:.:: ##::::'  '###::::   '##::::'     ##::' ' '#######:: '######::
	                                  ##:::...'##:::'  ## '##:::   ###::   '###:'  ' ##....   ##:'  ##... ##:: 
	                                ##::::  '##::'  ##:. '##::   ####' ####: '   ##:::  : ##:   ##:::..::..:
	                              ##::::  '##:'  ##:::. '##:   ##  ###  ##:  ' '##::  :: ##:.  ######::
                                             ##::  '##::   #######   ##:  ##.  ##:   ' ##:      ##::::      :..##::
                                            ##  ##:::   ##.... ''##:  ##:.::::    ##:  '  ##::::   ##:'   ##:::  ##:
                                            ###::::    ##:::: ''##:  ##::::::    ##:. '  '#######::.  ######::
                                          .::.......::::......::::::.......::::......::::::.......::::..::::......::::::.......:                                                                       ####:'  ##:::    ##:  '########:'  ########:'  '########|::  '##:::   ##:'  ########:  '########:
                     ##::    ###::   ##:...     ##..::..    .##.....:      :   ##....    ##:    ###::  ##:   ##.....::.            '##..::
                   ##::    ####:  ##::::     ##::::..    .##:::::::         ##::::    ##:    ####: ##:   ##::::::::            '##::::
                 ##::    ## ## ##::::      ##::::..   . ######:::     ########::   ## ## ##    ######:::         '##::::
               ##::    ##. ####::::      ##::::..  .  ##...::::         ##..  ##:::      ##. ####:   ##...:::::            '##::::
             ##::    ##:.  ###::::      ##::::..  .  ##:::::::         ##::.  ##::      ##:.  ###:   ##::::::::            '##::::
          ####:  ##::.   ##::::      ##::::..   . ########:   ##:::.    ##:    ##::.   ##:   ########::::    '##::::
         .::.......::::......::::::.......::::......::::::.......::::...::.......::::......::::::.......::::......::::::.......::::..::::......::::::..
		                                                                                      
                                                     Copyright©2021, Matheus Marinho (O Bonitão)  ''') 


while True:
   
    window,event,values = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == relatorio_cs and event == sg.WIN_CLOSED:
        relatorio_cs.hide()   

    if window == janela1 and event == 'entrar':
        user = values['user'] 
        auth = user.strip() + values['pass'].strip()
        
        if (auth == 'pedroMudar@12' or auth == 'vitoriaMudar@12' or auth == 'jessicaMudar@12' or auth == 'saulloMudar@12' or auth == 'mardonioMudar@12' or auth == 'dayaneMudar@12' or auth == 'mirianMudar@12' or auth == 'thaynaraMudar@12' 
        or auth == 'nailanyMudar@12' or auth == 'evertonMudar@12' or auth == 'marcoMudar@12' or auth == 'matheus2712'):
            janela1.hide()
            janela2 = principal()  
            vamos()
        else:
            window.FindElement('erro').Update('Usuario ou Senha Incorretos')   

    if window == janela2 and event == 'Limpar':
        window.FindElement('username').Update('')
        window.FindElement('password').Update('')
        window.FindElement('tecnico').Update('')
        window.FindElement('serial').Update('')
        window.FindElement('nap').Update('')
        window.FindElement('porta').Update('')
        window.FindElement('saida').Update('') 
        vamos()
        
    if window == janela2 and event == 'limparvoip':
        window.FindElement('napvoip').Update('')
        window.FindElement('serialvoip').Update('')
        window.FindElement('fxs').Update('')
        window.FindElement('circuito').Update('')
        window.FindElement('senha').Update('')
        window.FindElement('saida').Update('') 
        vamos()

    if window == janela2 and event == 'limparbridge':
        window.FindElement('userbridge').Update('')
        window.FindElement('serialbridge').Update('')
        window.FindElement('napbridge').Update('')
        window.FindElement('portabridge').Update('')
        window.FindElement('lan').Update('') 
        window.FindElement('saida').Update('')
        vamos()
       
    if window == janela2 and event == 'provisionar':
      n = values['nap'].strip()
      serial = values['serial'].strip()
      if values['username'].strip() == '' or values['password'].strip() == '' or values['tecnico'].strip() == '' or values['serial'].strip() == '' or values['nap'].strip() == '' or values['porta'].strip() == '':
        print('Preencha todos os campos')
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'provisionamento_pppoe'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:
        print('Digite uma NAP valida ') 

    if window == janela2 and event == 'provisionarbridge':
      n = values['napbridge'].strip()
      serial = values['serialbridge'].strip()
      if values['userbridge'].strip() == '' or values['lan'].strip() == '' or values['serialbridge'].strip() == '' or values['napbridge'].strip() == '' or values['portabridge'].strip() == '':
        print('Preencha todos os campos')
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'provisionamento_bridge'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:
        print('Digite uma NAP valida ')

    if window == janela2 and event == 'removerbridge':
      n = values['napbridge'].strip()
      serial = values['serialbridge'].strip()
      if values['serialbridge'].strip() == '' or values['napbridge'].strip() == '':
          print('Didige todos os campos')
      
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'remover'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:
        print('Digite uma NAP valida ')
              
    if window == janela2 and event == 'remover':
      n = values['nap'].strip()
      serial = values['serial'].strip()
      if values['serial'].strip() == '' or values['nap'].strip() == '':
          print('Didige todos os campos')
      
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'remover'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:
        print('Digite uma NAP valida ')
    

    if window == janela2 and event == 'buscar':
      n = values['nap'].strip()
      serial = values['serial'].strip()
      if values['serial'].strip() == '' or values['nap'].strip() == '':
          print('Didige todos os campos')
      
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'buscar'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:
        print('Digite uma NAP valida ')
      

    if window == janela2 and event == 'unprovision':
      n = values['nap'].strip()     
      if n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        op = 'unprovision'
        nap_bd(n, op)
      else:
        print('Digite uma NAP valida ')
    
    if window == janela2 and event == 'position':
      n = values['nap'].strip()     
      if n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        op = 'showpon'
        nap_bd(n, op)
      else:
        print('Digite uma NAP valida ')

    if window == janela2 and event == 'semuso':
      n = values['nap'].strip()     
      if n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        op = 'semuso'
        nap_bd(n, op)
      else:
        print('Digite uma NAP valida ')

    if window == janela2 and event == 'logbusca':
      arq = open('log_prov.txt', 'r')
      busca = arq.readlines()
      n = values['log'] 
      print('\n','_'*84,'\n')    
      for line in busca:
        if line.find(n) >= 0:
          print(line)

    if window == janela2 and event == 'limparlog':
        window.FindElement('log').Update('')
        window.FindElement('saida').Update('')

    if window == janela2 and event == 'provisionarvoip':
      n = values['napvoip'].strip()
      serial = values['serialvoip'].strip()
      if values['napvoip'].strip() == '' or values['serialvoip'].strip() == '' or values['fxs'].strip() == 'circuito' or values['serialvoip'].strip() == '':
        print('Preencha todos os campos')
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'voip'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:
        print('Digite uma NAP valida ')

    if window == janela2 and event == 'removervoip':
      n = values['napvoip'].strip()
      serial = values['serialvoip'].strip()
      if values['napvoip'].strip() == '' or values['serialvoip'].strip() == '' or values['fxs'].strip() == '':
        print('Preencha todos os campos')
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'removervoip'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:                            
        print('Digite uma NAP valida ')  
                                       
    if window == janela2 and event == 'buscarvoip':
      n = values['napvoip'].strip()    
      serial = values['serialvoip'].strip()
      if values['serialvoip'].strip() == '' or values['napvoip'].strip() == '':
          print('Didige todos os campos')
                                       
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':       
          op = 'buscarvoip'            
          nap_bd(n, op)                
        else:                          
          print('Digite um serial valido')
      else:                            
        print('Digite uma NAP valida ')

    if window == janela2 and event == 'relatoriocs':
        relatorio_cs = relatorio() 

    if window == janela2 and event == 'rebootonu':
      n = values['nap'].strip()
      serial = values['serial'].strip()
      if values['serial'].strip() == '' or values['nap'].strip() == '':
          print('Didige todos os campos')
      
      elif n[:4] == 'NAP-' or n == 'teste' or n == 'teste II':
        if serial[:4] == 'ALCL':
          op = 'reboot'
          nap_bd(n, op)
        else:
          print('Digite um serial valido')
      else:
        print('Digite uma NAP valida ') 

    if window == relatorio_cs and event == 'copiar':
        relato = values['relato']      
        sinal = values['sinal']        
        onu = values['onu']            
        feedback = values['feedback']  
        pyperclip.copy(f' Qual as dificuldades de acesso do cliente: {relato}\n Sinal Óptico: {sinal}\n Modelo da ONU: {onu} \n Feedback do Cliente: {feedback}')
        relatorio_cs.hide()                                   
    
window.close()
         
         
         