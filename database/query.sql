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