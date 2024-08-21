--
-- File generated with SQLiteStudio v3.4.4 on Вт Тра 14 13:13:15 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: auth_group
CREATE TABLE auth_group (
    id   INTEGER       NOT NULL
                       PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (150) NOT NULL
                       UNIQUE
);


-- Table: auth_group_permissions
CREATE TABLE auth_group_permissions (
    id            INTEGER NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    group_id      INTEGER NOT NULL
                          REFERENCES auth_group (id) DEFERRABLE INITIALLY DEFERRED,
    permission_id INTEGER NOT NULL
                          REFERENCES auth_permission (id) DEFERRABLE INITIALLY DEFERRED
);


-- Table: auth_permission
CREATE TABLE auth_permission (
    id              INTEGER       NOT NULL
                                  PRIMARY KEY AUTOINCREMENT,
    content_type_id INTEGER       NOT NULL
                                  REFERENCES django_content_type (id) DEFERRABLE INITIALLY DEFERRED,
    codename        VARCHAR (100) NOT NULL,
    name            VARCHAR (255) NOT NULL
);


-- Table: auth_user
CREATE TABLE auth_user (
    id           INTEGER       NOT NULL
                               PRIMARY KEY AUTOINCREMENT,
    password     VARCHAR (128) NOT NULL,
    last_login   DATETIME,
    is_superuser BOOL          NOT NULL,
    username     VARCHAR (150) NOT NULL
                               UNIQUE,
    last_name    VARCHAR (150) NOT NULL,
    email        VARCHAR (254) NOT NULL,
    is_staff     BOOL          NOT NULL,
    is_active    BOOL          NOT NULL,
    date_joined  DATETIME      NOT NULL,
    first_name   VARCHAR (150) NOT NULL
);


-- Table: auth_user_groups
CREATE TABLE auth_user_groups (
    id       INTEGER NOT NULL
                     PRIMARY KEY AUTOINCREMENT,
    user_id  INTEGER NOT NULL
                     REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    group_id INTEGER NOT NULL
                     REFERENCES auth_group (id) DEFERRABLE INITIALLY DEFERRED
);


-- Table: auth_user_user_permissions
CREATE TABLE auth_user_user_permissions (
    id            INTEGER NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    user_id       INTEGER NOT NULL
                          REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    permission_id INTEGER NOT NULL
                          REFERENCES auth_permission (id) DEFERRABLE INITIALLY DEFERRED
);


-- Table: django_admin_log
CREATE TABLE django_admin_log (
    id              INTEGER             NOT NULL
                                        PRIMARY KEY AUTOINCREMENT,
    action_time     DATETIME            NOT NULL,
    object_id       TEXT,
    object_repr     VARCHAR (200)       NOT NULL,
    change_message  TEXT                NOT NULL,
    content_type_id INTEGER
                                        REFERENCES django_content_type (id) DEFERRABLE INITIALLY DEFERRED,
    user_id         INTEGER             NOT NULL
                                        REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    action_flag     [SMALLINT UNSIGNED] NOT NULL
                                        CHECK ("action_flag" >= 0) 
);


-- Table: django_content_type
CREATE TABLE django_content_type (
    id        INTEGER       NOT NULL
                            PRIMARY KEY AUTOINCREMENT,
    app_label VARCHAR (100) NOT NULL,
    model     VARCHAR (100) NOT NULL
);


-- Table: django_migrations
CREATE TABLE django_migrations (
    id      INTEGER       NOT NULL
                          PRIMARY KEY AUTOINCREMENT,
    app     VARCHAR (255) NOT NULL,
    name    VARCHAR (255) NOT NULL,
    applied DATETIME      NOT NULL
);


-- Table: django_session
CREATE TABLE django_session (
    session_key  VARCHAR (40) NOT NULL
                              PRIMARY KEY,
    session_data TEXT         NOT NULL,
    expire_date  DATETIME     NOT NULL
);


-- Table: main_account
CREATE TABLE main_account (
    id           INTEGER       NOT NULL
                               PRIMARY KEY AUTOINCREMENT,
    phone_number VARCHAR (128) NOT NULL
                               UNIQUE,
    user_id      INTEGER       NOT NULL
                               UNIQUE
                               REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED
);


-- Table: main_historicalparking_place
CREATE TABLE main_historicalparking_place (
    id                    BIGINT             NOT NULL,
    number                INTEGER            NOT NULL,
    parking_cost          INTEGER            NOT NULL,
    start_time_reserved   DATETIME,
    end_time_reserved     DATETIME,
    is_place_for_disable  BOOL               NOT NULL,
    is_place_for_electric BOOL               NOT NULL,
    distance_to_exit      [INTEGER UNSIGNED] NOT NULL
                                             CHECK ("distance_to_exit" >= 0),
    status                VARCHAR (2)        NOT NULL,
    reserved_qr           TEXT,
    history_id            INTEGER            NOT NULL
                                             PRIMARY KEY AUTOINCREMENT,
    history_date          DATETIME           NOT NULL,
    history_change_reason VARCHAR (100),
    history_type          VARCHAR (1)        NOT NULL,
    history_user_id       INTEGER
                                             REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    parking_id            BIGINT,
    reserved_by_id        INTEGER
);


-- Table: main_parking
CREATE TABLE main_parking (
    id     INTEGER            NOT NULL
                              PRIMARY KEY AUTOINCREMENT,
    name   VARCHAR (100)      NOT NULL,
    street VARCHAR (100)      NOT NULL,
    count  [INTEGER UNSIGNED] NOT NULL
                              CHECK ("count" >= 0),
    type   VARCHAR (2)        NOT NULL,
    lat    REAL               NOT NULL,
    lng    REAL               NOT NULL,
    img    VARCHAR (100)      NOT NULL,
    info   TEXT               NOT NULL,
    urls   VARCHAR (100)      NOT NULL
);


-- Table: main_parking_place
CREATE TABLE main_parking_place (
    id                    INTEGER            NOT NULL
                                             PRIMARY KEY AUTOINCREMENT,
    is_place_for_disable  BOOL               NOT NULL,
    is_place_for_electric BOOL               NOT NULL,
    distance_to_exit      [INTEGER UNSIGNED] NOT NULL
                                             CHECK ("distance_to_exit" >= 0),
    parking_id            BIGINT             NOT NULL
                                             REFERENCES main_parking (id) DEFERRABLE INITIALLY DEFERRED,
    number                INTEGER            NOT NULL,
    status                VARCHAR (2)        NOT NULL,
    reserved_qr           VARCHAR (100),
    parking_cost          INTEGER            NOT NULL,
    start_time_reserved   DATETIME,
    reserved_by_id        INTEGER
                                             REFERENCES auth_user (id) DEFERRABLE INITIALLY DEFERRED,
    end_time_reserved     DATETIME
);


-- Index: auth_group_permissions_group_id_b120cbf9
CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions (
    "group_id"
);


-- Index: auth_group_permissions_group_id_permission_id_0cd325b0_uniq
CREATE UNIQUE INDEX auth_group_permissions_group_id_permission_id_0cd325b0_uniq ON auth_group_permissions (
    "group_id",
    "permission_id"
);


-- Index: auth_group_permissions_permission_id_84c5c92e
CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions (
    "permission_id"
);


-- Index: auth_permission_content_type_id_2f476e4b
CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission (
    "content_type_id"
);


-- Index: auth_permission_content_type_id_codename_01ab375a_uniq
CREATE UNIQUE INDEX auth_permission_content_type_id_codename_01ab375a_uniq ON auth_permission (
    "content_type_id",
    "codename"
);


-- Index: auth_user_groups_group_id_97559544
CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups (
    "group_id"
);


-- Index: auth_user_groups_user_id_6a12ed8b
CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups (
    "user_id"
);


-- Index: auth_user_groups_user_id_group_id_94350c0c_uniq
CREATE UNIQUE INDEX auth_user_groups_user_id_group_id_94350c0c_uniq ON auth_user_groups (
    "user_id",
    "group_id"
);


-- Index: auth_user_user_permissions_permission_id_1fbb5f2c
CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions (
    "permission_id"
);


-- Index: auth_user_user_permissions_user_id_a95ead1b
CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions (
    "user_id"
);


-- Index: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
CREATE UNIQUE INDEX auth_user_user_permissions_user_id_permission_id_14a6b632_uniq ON auth_user_user_permissions (
    "user_id",
    "permission_id"
);


-- Index: django_admin_log_content_type_id_c4bce8eb
CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log (
    "content_type_id"
);


-- Index: django_admin_log_user_id_c564eba6
CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log (
    "user_id"
);


-- Index: django_content_type_app_label_model_76bd3d3b_uniq
CREATE UNIQUE INDEX django_content_type_app_label_model_76bd3d3b_uniq ON django_content_type (
    "app_label",
    "model"
);


-- Index: django_session_expire_date_a5c62663
CREATE INDEX django_session_expire_date_a5c62663 ON django_session (
    "expire_date"
);


-- Index: main_historicalparking_place_history_date_28744822
CREATE INDEX main_historicalparking_place_history_date_28744822 ON main_historicalparking_place (
    "history_date"
);


-- Index: main_historicalparking_place_history_user_id_bfcb8db3
CREATE INDEX main_historicalparking_place_history_user_id_bfcb8db3 ON main_historicalparking_place (
    "history_user_id"
);


-- Index: main_historicalparking_place_id_c5c02fa6
CREATE INDEX main_historicalparking_place_id_c5c02fa6 ON main_historicalparking_place (
    "id"
);


-- Index: main_historicalparking_place_parking_id_2d8c85d1
CREATE INDEX main_historicalparking_place_parking_id_2d8c85d1 ON main_historicalparking_place (
    "parking_id"
);


-- Index: main_historicalparking_place_reserved_by_id_b3a5f880
CREATE INDEX main_historicalparking_place_reserved_by_id_b3a5f880 ON main_historicalparking_place (
    "reserved_by_id"
);


-- Index: main_parking_place_parking_id_14c5446f
CREATE INDEX main_parking_place_parking_id_14c5446f ON main_parking_place (
    "parking_id"
);


-- Index: main_parking_place_reserved_by_id_eeabf046
CREATE INDEX main_parking_place_reserved_by_id_eeabf046 ON main_parking_place (
    "reserved_by_id"
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
