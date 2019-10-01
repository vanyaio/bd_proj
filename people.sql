create table people (
	first_name varchar(80),
	sec_name varchar(80)
);

alter table people add column birth_date date;

insert into people values ('ivan', 'petrov', '1999-3-9');
insert into people values ('igor', 'ivanov', '1999-4-3');
insert into people values ('oleg', 'sidrov', '1999-6-8');

create table cities (
	city varchar(80),
	id int primary key
);

insert into cities values ('spb', 1);
insert into cities values ('msk', 2);

alter table people add column city_id int references cities(id);

update people set city_id = 1;
update people set birth_date = '2000-11-09';

insert into people values ('oleg', 'sidrov', '1999-6-8', 2);

create rule city_delete as on delete to cities do delete from people where city_id = OLD.id;
delete from cities where id = 1;

select * from people;
select * from cities;
drop table people cascade;
drop table cities cascade;
