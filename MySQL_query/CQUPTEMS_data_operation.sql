-- 创建数据库
create database cquptems_db;
-- 创建表
use cquptems_db;
-- 创建快递信息表
create table Packages(
    package_ID varchar(50) not null ,
    package_owner_phone_number decimal(11,0) not null ,
    shipping_address varchar(100)not null,
    express_company varchar(100)not null,
    primary key (package_ID,package_owner_phone_number)
);
-- 创建快递驿站表
create table Express_Station(
    package_ID varchar(50) not null ,
    pickup_user_student_ID decimal(10,0) not null ,
    import_time timestamp not null ,
    export_time timestamp default null,
    error_status int default 0,
    primary key (package_ID,pickup_user_student_ID)
);

-- 创建用户表
create table Users(
    user_name varchar(20) not null ,
    user_student_ID decimal(10,0) not null unique ,
    user_phone_number decimal(11,0)not null unique ,
    unique_pickup_code varchar(50) not null unique ,
    primary key (user_name,user_phone_number,user_student_ID,unique_pickup_code)
);
-- 表的删除语句
drop table Packages cascade ;
drop table Express_Station cascade ;
drop table users cascade ;