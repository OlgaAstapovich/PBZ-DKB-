create database supplies;
use supplies;

create table suppliers (
	SupplierNumber char(2) not null,
    SupplierName varchar(20) not null,
    SupplierStatus int,
    SupplierTown varchar(20) not null, 
    primary key (SupplierNumber)
    );
    
create table details (
	DetailNumber char(2) not null,
    DetailName varchar(20) not null,
    DetailColor varchar(20) not null,
    DetailSize int not null,
    DetailTown varchar(20) not null,
	primary key (DetailNumber)
);

create table projects (
	ProjectNumber char(3) not null,
    ProjectName varchar(10) not null,
    ProjectTown varchar(20) not null,
	primary key (ProjectNumber)
);

create table supplies (
	SupplierNumber char(2) not null,
    DetailNumber char(2) not null,
    ProjectNumber char(3) not null,
    Number_of_details int not null 
);