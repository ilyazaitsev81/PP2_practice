CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phnum VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phnum
    FROM phbook c
    WHERE c.name ILIKE '%' || pattern || '%'
       OR c.phnum ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, offs INT)
RETURNS TABLE(id INT, name VARCHAR, phnum VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phnum
    FROM phbook c
    ORDER BY c.id
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;