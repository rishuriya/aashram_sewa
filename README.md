# aashram_sewa
## To Run the webpage
Clone this repository, then do create the virtual environment and then run it<br>

```bash
cd aashram/
python3 pip -m venv <virtualenvname>
source <virtualenvname>/bin/activate
```

Then download and install the required package
```bash
pip install -r requirements.txt
```
<b>Migrate the models </b>
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

<b>Create Super user </b>
```bash
python3 manage.py createsuperuser
```
<b>Run the Website </b>
```bash
python3 manage.py runserver
```
