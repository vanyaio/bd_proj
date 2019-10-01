create table people (
	name varchar(80),
	id int primary key
);

create table money (
	money int,
	id int primary key
);

insert into people values ('ivan', 1);
insert into people values ('oleg', 2);
insert into people values ('nikita', 3);

insert into money values (100, 1);
insert into money values (200, 2);
insert into money values (400, 4);

select * from people;
select * from money;

select *
from people
cross join money
where money.money > 100;

select name, money
from people
join money
on people.id = money.id;

select name, money
from people
left join money
on people.id = money.id;

select name, money
from people
right join money
on people.id = money.id;

select name, money
from people
full join money
on people.id = money.id;



create table t1 (
	a int
);

create table t2 (
	a int,
	name varchar(80)
);

insert into t1 values (10);
insert into t1 values (20);

insert into t2 values (10, 'ivan');
insert into t2 values (10, 'kek');

select t1.a, t2.name
from t1
join t2 on t1.a = t2.a
join people 
on t2.name = people.name;

drop table t1;
drop table t2;
drop table people;
drop table money;
