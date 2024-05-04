CREATE TABLE
    IF NOT EXISTS nkda_user (
        id BIGSERIAL PRIMARY KEY NOT NULL,
        username VARCHAR(80) UNIQUE NOT NULL,
        first_name VARCHAR(80) NOT NULL,
        last_name VARCHAR(80) NOT NULL,
        password VARCHAR(80) NOT NULL,
        phone VARCHAR(20) UNIQUE NOT NULL,
        email VARCHAR(120) UNIQUE NOT NULL,
        gender VARCHAR(20) NOT NULL,
        active BOOLEAN DEFAULT true,
        date_of_join BIGINT NOT NULL,
        created_at BIGINT NOT NULL DEFAULT extract(epoch from now()) * 1000,
        updated_at BIGINT
    );


CREATE TABLE
    IF NOT EXISTS user_role (
        id BIGSERIAL PRIMARY KEY NOT NULL,
        user_id BIGINT NOT NULL,
        name VARCHAR(80) NOT NULL,
        created_at BIGINT NOT NULL DEFAULT extract(epoch from now()) * 1000,
        updated_at BIGINT,
        FOREIGN KEY (user_id) REFERENCES nkda_user (id) ON DELETE CASCADE
    );