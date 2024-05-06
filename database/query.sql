INSERT INTO
    public.nkda_user (
        username,
        first_name,
        last_name,
        "password",
        phone,
        email,
        gender,
        active,
        date_of_join
    )
VALUES
    (
        'deepdey',
        'Deep',
        'Dey',
        'password',
        '8697448896',
        'deep.websofttechs.com',
        'MALE',
        true,
        0
    );

INSERT INTO
    public.user_role (user_id, "name")
VALUES
    (1, 'ADMIN');

INSERT INTO
    public.user_role (user_id, "name")
VALUES
    (1, 'CHEIF_ENGINEER');

-- Product query starts here
INSERT INTO
    public.product (
        product_name,
        product_description,
        product_price
    )
VALUES
    (
        'Iphone',
        'This product is a smartphone with awesome features',
        100000
    );
-- Product query ends here.