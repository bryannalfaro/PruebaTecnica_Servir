create database pruebaServir;

create table department(
	code_dept varchar(50) primary key not null,
	name_dept varchar(255) not null,
	description_dept varchar(255) 
);


create sequence employee_sequence2;
create table employee(
	code_employee varchar(20) primary key default ('EMP-' || LPAD(nextval('employee_sequence2')::text, 4, '0')),
	name_employee varchar(255) not null,
	last_name_employee varchar(255) not null,
	date_of_birth_employee date,
	dept_employee varchar(50) not null,
	foreign key (dept_employee) references department(code_dept)
	
);