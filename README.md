
## Poor Man's Twitter


## Description
An  an application that allows the users to tweet out messages buitt with  **Django(DRF) - Python** and **VueJs - Javascript**

- Key Application features
    - Send tweet with name and message
    - Message limited to 50 characters
    - Table showing messages from lastest


## Technology Stack

- Django
- DRF
- SQLlite
- VueJS


###  Setting Up For Local Development

-   Check that python 3 is installed:


-   Clone the favorite-thing repo and cd into it:

    ```
    git clone https://github.com/tonyguesswho/not-twitter.git
    ```

- Create and activate a  virtual enviroment

-   Install dependencies from requirements.txt file:

    ```
    pip install -r requirements.txt
    ```


-   Apply migrations:

    ```
    cd into the backend folder and run python manage.py migrate
    ```

*   Run the application with the command

    ```
    python manage.py runserver
    ```

- Application is available on `http://127.0.0.1:8000/`

## Running tests
cd into the backend folder and run
```
python manage.py test
```


## API Endpoints
<table>
  <tr>
      <th>Request</th>
      <th>End Point</th>
      <th>Action</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>/api/tweet/</td>
    <td>Get all messages</td>
  </tr>
  <tr>
    <td>POST</td>
    <td>/api/tweet/</td>
    <td>Create a new message</td>
  </tr>
</table>



I will appreciate any feedback on this project :)
