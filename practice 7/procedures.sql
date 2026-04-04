CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_name VARCHAR,
    p_phone VARCHAR
)
AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM phbook WHERE name = p_name
    ) THEN
        UPDATE phbook
        SET phnum = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phbook(name, phnum)
        VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],
    phones TEXT[]
)
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        IF length(phones[i]) = 11 THEN
            CALL insert_or_update_user(names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: %, %',
                names[i], phones[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(
    query TEXT
)
AS $$
BEGIN
    DELETE FROM phbook
    WHERE name ILIKE '%' || query || '%'
       OR phnum ILIKE '%' || query || '%';
END;
$$ LANGUAGE plpgsql;