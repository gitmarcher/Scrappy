# Scrappy

*Scrappy* is a web scraping tool developed as part of a DBMS semester project. It leverages Python libraries such as `requests` and `BeautifulSoup` to efficiently scrape data from various sources, compiling comprehensive team rankings for premier leagues from 2000 to 2023.

## Key Features

1. **Data Extraction**: Retrieves historical team rankings from premier league websites.
2. **Comprehensive Coverage**: Includes data from 2000 through 2023.
3. **Database Integration**: Utilizes `PeeWee ORM` and `SQLConnector` to manage and store data in a SQL database.
4. **ER Diagrma** : ER diagram is available in ER.pdf file.

*Scrappy* not only extracts and parses data but also handles data storage and management, demonstrating practical skills in both web scraping and database interaction.

## Setup Instructions

**This script must be run in a Linux-based environment.**

### Install Dependencies

To install all required dependencies and packages, run the following command:

```bash
pip install -r requirements.txt
```
### Handling mysqlclient Installation Errors

If you encounter an error while installing `mysqlclient`, follow these steps:

1. Install the `libmysqlclient-dev` package using the command:

    ```bash
    sudo apt-get install libmysqlclient-dev
    ```

2. Run the following commands to gather configuration information:

    ```bash
    mysql_config --cflags
    mysql_config --libs
    ```

3. Add the obtained information to the `~/.bashrc` file. Use the following steps:

    ```bash
    nano ~/.bashrc
    ```

    Add the following lines:

    ```bash
    export MYSQLCLIENT_CFLAGS="-I/path/to/mysql/include"  # obtained from 'mysql_config --cflags'
    export MYSQLCLIENT_LDFLAGS="-L/path/to/mysql/lib -lmysqlclient"  # obtained from 'mysql_config --libs'
    ```

4. After making these changes, resume the installation of `mysqlclient`.

### Setting Up User Password

Another requirement for running this script is setting up a password for the user. The default user `'root'` created during an insecure installation uses `auth_socket` for authentication, which is handled by the OS.

Follow these steps to add the password:

```sql
ALTER USER 'your_username'@'localhost' IDENTIFIED BY 'new_password';
GRANT ALL PRIVILEGES ON database_name.* TO 'new_user'@'localhost';
FLUSH PRIVILEGES;
