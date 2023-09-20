# Selene

🐍 This project works with python3 & pymysql.   
⚙️ You can put your mysql identifiers and others settings in settings.json file.    
<br>
<hr>

### 📌 How to start ?  
Selene is an easy-to-use script written with python3. Thus, we will use python3 to start.
The <a href="https://github.com/dawnl3ss/Selene/blob/main/main.py">main.py</a> file takes 3 differents parameters :
- -hh / --host : the MySQL host ip-address.
- -u / --user : the username.
- -d / --database : the database that will be dumped.  


Here is an example :
<br>

```bash
python3 main.py -hh 127.0.0.1 -u root -d database-test
```

Then, Selene will be asking you the password which match with your username.

### 📌 Example :
```bash
┌─[amanara@parrot]─[~/Desktop/Selene]
└──╼ [★]$ python3 main.py -hh 127.0.0.1 -u root -d db_example
☾ Starting Selene dumper...

    _.._           ██████ ▓█████  ██▓    ▓█████  ███▄    █ ▓█████ 
   .' .-'`       ▒██    ▒ ▓█   ▀ ▓██▒    ▓█   ▀  ██ ▀█   █ ▓█   ▀ 
  /  /           ░ ▓██▄   ▒███   ▒██░    ▒███   ▓██  ▀█ ██▒▒███          _.._    
  |  |             ▒   ██▒▒▓█  ▄ ▒██░    ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄       .' .-'`  
  \  '.___.;     ▒██████▒▒░▒████▒░██████▒░▒████▒▒██░   ▓██░░▒████▒     /  /      
   '._  _.'      ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░     |  |      
      ``         ░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░     \  '.___.;
                 ░  ░  ░     ░     ░ ░      ░      ░   ░ ░    ░         '._  _.' 
                       ░     ░  ░    ░  ░   ░  ░         ░    ░  ░         ``    

✦ Best database dumper written by Dawnl3ss.
✦ This tool is only design for educationnal and ethical purpose. I am not responsible for your usage.
✦ Github : https://github.com/dawnl3ss
 
 MySQL root's password : root
 
✦ Dumping... 
✦ Database has been dumped !
 
 Which method you want to get your result ? [f=file | s=shell] : s
 


✦ Table 'faq' :
  | 1 |     | Software |     | Some question here |     | Some answer here |    
  | 1 |     | Software |     | Another question huh ? |     | Yup but i dont have any answer dude... |    
 
✦ Table 'users' :
  | 1 |     | Dawnless |     | daa@gmail.com |     | ijbndsbndihqsnhidqsbnd |
```
