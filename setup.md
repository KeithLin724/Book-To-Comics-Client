# Book-To-Comics Setup
## Written By KYLiN

---
> Mention: Docker file is not complete
### Setup
please add a file under the folder of `./Book_to_Comics_Client`

The path is `./Book_to_Comics_Client/.env`

#### File format

```sh
# .env
SERVER_IP={YOUR_BOOK_TO_COMIC_API_SERVER_IP}
SERVER_PORT={YOUR_BOOK_TO_COMIC_API_SERVER_PORT}
```
> Set up Book To Comic server in here -> https://github.com/KeithLin724/Book-To-Comics

### Run the app
```sh
# make a venv
python -m venv .venv

# activate the venv
source Book-To-Comics-Client/.venv/bin/activate

# install list of package
pip install -r ./requirements.txt

# run the app
reflex run 

# or run the app in product mode
reflex run --env prod

# or run in debug mode
reflex run --loglevel debug
``` 
The app run in `http://localhost:3000`


---

## More information
### Reflex
- Website: https://reflex.dev/
- GitHub: https://github.com/reflex-dev/reflex
