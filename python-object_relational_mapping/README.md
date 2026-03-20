# Python - Object Relational Mapping (ORM)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)

## Description

This directory introduces database connections from Python. It transitions from using raw SQL queries with `MySQLdb` to utilizing an **Object Relational Mapper (ORM)** via `SQLAlchemy`.

## Files

| File | Description |
| :--- | :--- |
| `0-select_states.py` | Lists all `states` from the database `hbtn_0e_0_usa` using `MySQLdb`. |
| `1-filter_states.py` | Lists all `states` with a name starting with `N` using `MySQLdb`. |
| `2-my_filter_states.py` | Takes in an argument and displays all values in the `states` table where `name` matches the argument. |
| `3-my_safe_filter_states.py` | A safe version of state filtering that is protected against SQL injections. |
| `4-cities_by_state.py` | Lists all `cities` from the database, utilizing a `JOIN` query via `MySQLdb`. |
| `5-filter_cities.py` | Takes in the name of a state as an argument and lists all `cities` of that state using `MySQLdb`. |
| `model_state.py` | Contains the class definition of a `State` and an instance `Base = declarative_base()` for SQLAlchemy. |
| `model_city.py` | Contains the class definition of a `City` for SQLAlchemy. |
| `7-model_state_fetch_all.py` | Lists all `State` objects from the database using SQLAlchemy. |
| `8-model_state_fetch_first.py` | Prints the first `State` object from the database using SQLAlchemy. |
| `9-model_state_filter_a.py` | Lists all `State` objects that contain the letter `a` using SQLAlchemy. |
| `10-model_state_my_get.py` | Prints the `State` object with the name passed as argument using SQLAlchemy. |
| `11-model_state_insert.py` | Adds the `State` object "Louisiana" to the database. |
| `12-model_state_update_id_2.py` | Changes the name of a `State` object in the database. |
| `13-model_state_delete_a.py` | Deletes all `State` objects with a name containing the letter `a`. |
| `14-model_city_fetch_by_state.py` | Fetches and prints all `City` objects by state using a relationship in SQLAlchemy. |

*Note: Various `.sql` files are included for initial database setup and mock data.*

---

## Author

- **CERQUEIRA Loïc** - *Student at Holberton School*
