# SQL - More Queries

![SQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)

## Description

This directory expands on SQL concepts by diving into complex database interactions. It covers user management, granting privileges, primary/foreign keys constraints, and complex **`JOIN`** operations.

## Files

| File | Description |
| :--- | :--- |
| `0-privileges.sql` | Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2`. |
| `1-create_user.sql` | Creates the MySQL server user `user_0d_1` with all privileges. |
| `2-create_read_user.sql` | Creates the database `hbtn_0d_2` and the user `user_0d_2` (with SELECT privilege only). |
| `3-force_name.sql` | Creates the table `force_name` where the `name` column cannot be null. |
| `4-never_empty.sql` | Creates the table `id_not_null` where the `id` column defaults to 1. |
| `5-unique_id.sql` | Creates the table `unique_id` where the `id` column is unique and defaults to 1. |
| `6-states.sql` | Creates the database `hbtn_0d_usa` and the table `states` with a Primary Key. |
| `7-cities.sql` | Creates the table `cities` with a Foreign Key referencing `states`. |
| `8-cities_of_california_subquery.sql` | Lists all the cities of California that can be found in `hbtn_0d_usa` using a subquery. |
| `9-cities_by_state_join.sql` | Lists all cities contained in the database using a common `JOIN`. |
| `10-genre_id_by_show.sql` | Lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. |
| `11-genre_id_all_shows.sql` | Lists all shows contained in the database, displaying `NULL` if they don't have a genre (`LEFT JOIN`). |
| `12-no_genre.sql` | Lists all shows contained in `hbtn_0d_tvshows` without a genre linked. |
| `13-count_shows_by_genre.sql` | Lists all genres and displays the number of shows linked to each. |
| `14-my_genres.sql` | Retrieves all genres of the show 'Dexter' using multiple joins. |
| `15-comedy_only.sql` | Lists all Comedy shows in the database `hbtn_0d_tvshows`. |
| `16-shows_by_genre.sql` | Lists all shows and all genres linked to that show. |

---

## Author

- **CERQUEIRA Loïc** - *Student at Holberton School*
