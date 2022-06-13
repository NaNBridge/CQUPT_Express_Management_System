-- 创建数据库
create database cquptems_db;
-- 创建表
use cquptems_db;
-- 创建快递信息表

create table Packages(
    package_ID varchar(50) not null ,
    package_owner_phone_number varchar(11) not null ,
    shipping_address varchar(100)not null,
    express_company varchar(100)not null,
    primary key (package_ID,package_owner_phone_number)
);
-- 创建快递驿站表
create table Express_Station(
    package_ID varchar(50) not null ,
    pickup_user_student_ID varchar(10) not null ,
    import_time timestamp not null ,
    export_time timestamp default null,
    error_status int default 0,
    primary key (package_ID,pickup_user_student_ID)
);

-- 创建用户表
create table Users(
    user_name varchar(20) not null ,
    user_student_ID varchar(10) not null unique ,
    user_phone_number varchar(11)not null unique ,
    unique_pickup_code varchar(19) not null unique ,
    user_password varchar(6),
    primary key (user_name,user_phone_number,user_student_ID,unique_pickup_code)
);

-- 向users表中插入数据
INSERT INTO Users(USER_NAME, USER_STUDENT_ID, USER_PHONE_NUMBER, UNIQUE_PICKUP_CODE, USER_PASSWORD)
VALUES
    ('擎天柱','0123456789','01234567890','3478910236547896321','123456');
SELECT *
FROM Users
WHERE user_name LIKE '擎天柱';
DELETE FROM Users
WHERE user_name LIKE '擎天柱';
-- 表的删除语句
drop table Packages cascade ;
drop table Express_Station cascade ;
drop table users cascade ;

-- 向user表中插入信息
use cquptems_db;
insert
into users(user_name, user_student_ID, user_phone_number, unique_pickup_code)
values ('龚南桥', '2020211370', '15902364457', '1923500191540736252');

-- 删除users表中的数据
delete from users
where user_name like ‘龚南桥’;

-- 向Packages表中插入数据
insert
into packages(package_ID, package_owner_phone_number, shipping_address, express_company)
values ('01234567890123456789012345678901234567890123456789',
        '17669806701',
        '美国华盛顿特区',
        '中国邮政');

-- 删除packages中的信息
delete from packages
where package_owner_phone_number like '15902364472';

delete from packages;


-- 创建快递驿站的触发器,在向packages表中插入数据时触发
-- 向express_station表中插入对应信息
drop trigger wareinghouse;
create trigger wareinghouse
    after insert
    on packages
    FOR EACH ROW
    BEGIN
        INSERT INTO Express_Station (package_ID, pickup_user_student_ID, import_time)
            VALUES (NEW.package_ID,
                    (SELECT user_student_ID
                     FROM users,packages
                     WHERE user_phone_number=Packages.package_owner_phone_number
                     LIMIT 1),
                    CURRENT_TIMESTAMP);
    END;


-- (select user_student_ID
--             from users
--             where user_phone_number = package_owner_phone_number)

SELECT user_phone_number
FROM users;

SELECT user_phone_number,package_owner_phone_number
FROM users,Packages
WHERE user_phone_number=Packages.package_owner_phone_number;


UPDATE Packages
SET package_owner_phone_number='17669806701'
WHERE package_owner_phone_number LIKE '15902364472';

-- 插叙语句,用于登录
SELECT user_student_ID,user_password
FROM Users
WHERE user_student_ID='2020211370' AND user_password='9VpOZn';