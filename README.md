# Selene

🐍 This project works with python3 & pymysql.   

## 📌 Installation :
You can download Selene from github :
```console
# Clone the repository
$ git clone https://github.com/dawnl3ss/Selene

# go to the Selene directory
$ cd Selene
```
## 📌 Alternative Installation :
#### exposes the selene command to the whole  system
```shell
# Clone the repository
$ git clone https://github.com/dawnl3ss/Selene

# go to the Selene directory
$ cd Selene

# create a symlink bound to the selene.sh script
$ sudo ln -s $(realpath selene.sh) /usr/bin/selene
```

## 📌 How to start ?  
Selene is an easy-to-use script written with python3. Thus, we will use python3 to start it.
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

## 📌 Example :
<img src="https://github.com/dawnl3ss/Selene/blob/main/img/example.png">
