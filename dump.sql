create table Game_life_casaproduzione
(
    id   integer      not null
        primary key autoincrement,
    nome varchar(100) not null
);

create table Game_life_cliente
(
    id   integer      not null
        primary key autoincrement,
    nome varchar(100) not null
);

create table Game_life_gioco
(
    id     integer      not null
        primary key autoincrement,
    titolo varchar(100) not null
);

create table Game_life_acquisto
(
    id         integer not null
        primary key autoincrement,
    data       date    not null,
    cliente_id bigint  not null
        references Game_life_cliente
            deferrable initially deferred,
    gioco_id   bigint  not null
        references Game_life_gioco
            deferrable initially deferred
);

create index Game_life_acquisto_cliente_id_9ac9cbc3
    on Game_life_acquisto (cliente_id);

create index Game_life_acquisto_gioco_id_27a47e51
    on Game_life_acquisto (gioco_id);

create table Game_life_gioco_case_produzione
(
    id                integer not null
        primary key autoincrement,
    gioco_id          bigint  not null
        references Game_life_gioco
            deferrable initially deferred,
    casaproduzione_id bigint  not null
        references Game_life_casaproduzione
            deferrable initially deferred
);

create index Game_life_gioco_case_produzione_casaproduzione_id_af3b64ad
    on Game_life_gioco_case_produzione (casaproduzione_id);

create index Game_life_gioco_case_produzione_gioco_id_c95e288e
    on Game_life_gioco_case_produzione (gioco_id);

create unique index Game_life_gioco_case_produzione_gioco_id_casaproduzione_id_a0ce4cb7_uniq
    on Game_life_gioco_case_produzione (gioco_id, casaproduzione_id);

create table Game_life_recensione
(
    id         integer not null
        primary key autoincrement,
    contenuto  text    not null,
    cliente_id bigint  not null
        references Game_life_cliente
            deferrable initially deferred,
    gioco_id   bigint  not null
        references Game_life_gioco
            deferrable initially deferred
);

create index Game_life_recensione_cliente_id_76855e81
    on Game_life_recensione (cliente_id);

create index Game_life_recensione_gioco_id_1690eda9
    on Game_life_recensione (gioco_id);

create table Game_life_venditore
(
    id   integer      not null
        primary key autoincrement,
    nome varchar(100) not null
);

create table Game_life_gioco_venditori
(
    id           integer not null
        primary key autoincrement,
    gioco_id     bigint  not null
        references Game_life_gioco
            deferrable initially deferred,
    venditore_id bigint  not null
        references Game_life_venditore
            deferrable initially deferred
);

create index Game_life_gioco_venditori_gioco_id_6b4f9008
    on Game_life_gioco_venditori (gioco_id);

create unique index Game_life_gioco_venditori_gioco_id_venditore_id_a5dd7859_uniq
    on Game_life_gioco_venditori (gioco_id, venditore_id);

create index Game_life_gioco_venditori_venditore_id_eb527604
    on Game_life_gioco_venditori (venditore_id);

create table auth_group
(
    id   integer      not null
        primary key autoincrement,
    name varchar(150) not null
        unique
);

create table auth_user
(
    id           integer      not null
        primary key autoincrement,
    password     varchar(128) not null,
    last_login   datetime,
    is_superuser bool         not null,
    username     varchar(150) not null
        unique,
    last_name    varchar(150) not null,
    email        varchar(254) not null,
    is_staff     bool         not null,
    is_active    bool         not null,
    date_joined  datetime     not null,
    first_name   varchar(150) not null
);

create table auth_user_groups
(
    id       integer not null
        primary key autoincrement,
    user_id  integer not null
        references auth_user
            deferrable initially deferred,
    group_id integer not null
        references auth_group
            deferrable initially deferred
);

create index auth_user_groups_group_id_97559544
    on auth_user_groups (group_id);

create index auth_user_groups_user_id_6a12ed8b
    on auth_user_groups (user_id);

create unique index auth_user_groups_user_id_group_id_94350c0c_uniq
    on auth_user_groups (user_id, group_id);

create table django_content_type
(
    id        integer      not null
        primary key autoincrement,
    app_label varchar(100) not null,
    model     varchar(100) not null
);

create table auth_permission
(
    id              integer      not null
        primary key autoincrement,
    content_type_id integer      not null
        references django_content_type
            deferrable initially deferred,
    codename        varchar(100) not null,
    name            varchar(255) not null
);

create table auth_group_permissions
(
    id            integer not null
        primary key autoincrement,
    group_id      integer not null
        references auth_group
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id);

create unique index auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    on auth_group_permissions (group_id, permission_id);

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id);

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id);

create unique index auth_permission_content_type_id_codename_01ab375a_uniq
    on auth_permission (content_type_id, codename);

create table auth_user_user_permissions
(
    id            integer not null
        primary key autoincrement,
    user_id       integer not null
        references auth_user
            deferrable initially deferred,
    permission_id integer not null
        references auth_permission
            deferrable initially deferred
);

create index auth_user_user_permissions_permission_id_1fbb5f2c
    on auth_user_user_permissions (permission_id);

create index auth_user_user_permissions_user_id_a95ead1b
    on auth_user_user_permissions (user_id);

create unique index auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
    on auth_user_user_permissions (user_id, permission_id);

create table django_admin_log
(
    id              integer           not null
        primary key autoincrement,
    object_id       text,
    object_repr     varchar(200)      not null,
    action_flag     smallint unsigned not null,
    change_message  text              not null,
    content_type_id integer
        references django_content_type
            deferrable initially deferred,
    user_id         integer           not null
        references auth_user
            deferrable initially deferred,
    action_time     datetime          not null,
    check ("action_flag" >= 0)
);

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id);

create unique index django_content_type_app_label_model_76bd3d3b_uniq
    on django_content_type (app_label, model);

create table django_migrations
(
    id      integer      not null
        primary key autoincrement,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime     not null
);

create table django_session
(
    session_key  varchar(40) not null
        primary key,
    session_data text        not null,
    expire_date  datetime    not null
);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);


