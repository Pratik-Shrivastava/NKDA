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
        created_at TIMESTAMP NOT NULL DEFAULT now(),
        updated_at TIMESTAMP
    );


CREATE TABLE
    IF NOT EXISTS user_role (
        id BIGSERIAL PRIMARY KEY NOT NULL,
        user_id BIGINT NOT NULL,
        name VARCHAR(80) NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT now(),
        updated_at TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES nkda_user (id) ON DELETE CASCADE
    );

CREATE TABLE
    IF NOT EXISTS entry_log (
        id BIGSERIAL PRIMARY KEY NOT NULL,
        user_id BIGINT NOT NULL,
        user_name VARCHAR(160) NOT NULL,
        ip_address VARCHAR(40) NOT NULL,
        endpoint VARCHAR(255) NOT NULL,
        method VARCHAR(10) NOT NULL,
        request_payload JSONB DEFAULT NULL,
        query_params JSONB DEFAULT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT now(),
        FOREIGN KEY (user_id) REFERENCES nkda_user (id) ON DELETE CASCADE
    );
-- Product schema starts here.
CREATE TABLE
    IF NOT EXISTS product (
        product_id BIGSERIAL PRIMARY KEY NOT NULL,
        product_name VARCHAR(255) NOT NULL,
        product_description TEXT,
        product_price FLOAT NOT NULL,
        created_at BIGINT NOT NULL DEFAULT EXTRACT(EPOCH FROM NOW()) * 1000,
        created_by VARCHAR(80) NOT NULL,
        updated_at BIGINT
        updated_by VARCHAR(80) NOT NULL
);
-- Product schema ends here.