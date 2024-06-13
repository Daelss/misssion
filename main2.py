import psycopg2

# Подключение к базе данных
conn = psycopg2.connect("dbname=test user=postgres password=123 options='-c client_encoding=utf8'")

# Создание курсора для выполнения операций в базе данных
cur = conn.cursor()

# Создание таблицы сущности "Заказы"
cur.execute("CREATE TABLE Orders (order_id SERIAL PRIMARY KEY, date DATE, client_id INT, status VARCHAR(20))")
conn.commit()

# Заполнение таблицы Orders
cur.execute("INSERT INTO Orders (date, client_id, status) VALUES ('2022-01-01', 1, 'Новый')")
cur.execute("INSERT INTO Orders (date, client_id, status) VALUES ('2022-01-02', 2, 'В работе')")
# Добавьте еще записей по аналогии

# Создание процедуры для проверки адреса электронной почты
cur.execute("""
CREATE OR REPLACE FUNCTION check_email(email VARCHAR) RETURNS BOOLEAN AS $$
BEGIN
    -- Проверка на корректность адреса электронной почты
    RETURN email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}$';
END;
$$ LANGUAGE plpgsql;
""")
conn.commit()

# Создание таблицы для истории изменения статусов заказов
cur.execute("CREATE TABLE History (change_date DATE, order_id INT, order_date DATE, old_status VARCHAR(20), new_status VARCHAR(20))")
conn.commit()

# Создание триггера для отслеживания изменения статусов заказов
cur.execute("""
CREATE OR REPLACE FUNCTION trigger_history()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO History (change_date, order_id, order_date, old_status, new_status)
    VALUES (current_date, NEW.order_id, NEW.date, OLD.status, NEW.status);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER status_change
AFTER UPDATE OF status ON Orders
FOR EACH ROW
EXECUTE FUNCTION trigger_history();
""")
conn.commit()

# Закрытие курсора и соединения конец
cur.close()
conn.close()
