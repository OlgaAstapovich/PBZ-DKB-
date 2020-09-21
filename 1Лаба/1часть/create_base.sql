SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

create database education;
USE education;


CREATE TABLE teacher (
  	teacher_id CHAR(4) NOT NULL primary key,
	surname VARCHAR(20) NOT NULL,
	teacher_position VARCHAR(20) NOT NULL,
	department VARCHAR(20) NOT NULL,
	speciality VARCHAR(30) NOT NULL,
	phone_number INT
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE subject (
  	code_number_of_the_subject CHAR(3) NOT NULL,
	subject_name VARCHAR(20) NOT NULL,
	number_of_hours INT NOT NULL,
	speciality VARCHAR(30) NOT NULL,
	semester INT NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE students_group (
  	group_code_number VARCHAR(3) NOT NULL primary key,
	group_name VARCHAR(5) NOT NULL,
	number_of_persons INT NOT NULL,
	speciality VARCHAR(30) NOT NULL,
	surname_of_the_headman VARCHAR(20) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE teacher_subject_group (
	group_code_number VARCHAR(3) NOT NULL,
  	code_number_of_the_subject CHAR(3) NOT NULL,
	teacher_id CHAR(4) NOT NULL,
	number_of_audience INT NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;



