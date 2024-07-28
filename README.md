# PySubFinder
Subdomain finder write in python
### Install on Linux
---
- Clone the repository from Github
```shell
git clone https://github.com/Gun8hoot/PySubFinder.git
```
- Go to the project repository
```shell
cd ./PySubFinder
```
- **(optional)** : If you don't have a wordlist extract the subdomain_wl.tar file
```shell
tar -xvf ./subdomain_wl.tar
```
- **(optional)** :  Create a python virtual environment before installing every module
```shell
python3 -m venv .venv && source ./.venv/bin/activate
```
- Go to the project repository
```shell
pip install -r ./requirements.txt
```
### Usage
---
```shell
python3 ./main.py -u {URL} -f {WORDLIST_PATH}
```
![Usage gif](./images/example.gif)
***I dont know why admin was print twice***


> ⚠️ : It is preferable to use ffuf in CTF, because you can't filter HTTP response size with this tool
 ```shell
 # To filter HTTP response size with ffuf do:
 ffuf -w {WORDLIST}:FUZZ -u {URL} -H "Host: FUZZ.{URL}"
 # Look common size in the output. If the commun size 15949, replace 15949 in {SIZE}
 ffuf -w {WORDLIST}:FUZZ -u {URL} -H "Host: FUZZ.{URL}" -fs {SIZE}
 ```


<br><br>

---
> Write in: </br>
>[![S/O skillicons for th icon](https://skillicons.dev/icons?i=python&theme=dark)](https://skillcons.dev/)