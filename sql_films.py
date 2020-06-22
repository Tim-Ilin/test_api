import psycopg2

films_list = []


def get_films_db():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="pg",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from films"
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            film_dict = {}
            film_dict["code"] = str(row[0]).strip(' ')
            film_dict["title_rus"] = row[1]
            films_list.append(film_dict)
        return films_list

    except (Exception, psycopg2.Error) as error:
        print(error)

    finally:
        if (connection):
            cursor.close()
            connection.close()


if __name__ == '__main__':
    get_films_db()
