create table s3 (
id int not null AUTO_INCREMENT,
key1 varchar(100),
key2 int,
key3 varchar(100),
key_part1 varchar(100),
key_part2 varchar(100),
key_part3 varchar(100),
common_field varchar(100),
primary key (id),
key idx_key1 (key1),
unique key idx_key2 (key2),
key idx_key3 (key3),
key idx_key_part(key_part1, key_part2, key_part3)

) Engine=InnoDB CHARSET=utf8;
EXPLAIN SELECT * FROM s1 WHERE key1 > 'a' AND key1 < 'b';


select id, key1, key2, key3, key_part1, key_part2, key_part3, common_field,`test`.`s2`.`id` AS `id`,`test`.`s2`.`key1` AS `key1`,`test`.`s2`.`key2` AS `key2`,`test`.`s2`.`key3` AS `key3`,`test`.`s2`.`key_part1` AS `key_part1`,`test`.`s2`.`key_part2` AS `key_part2`,`test`.`s2`.`key_part3` AS `key_part3`,`test`.`s2`.`common_field` AS `common_field` from `test`.`s1` join `test`.`s2` where ((`test`.`s1`.`common_field` = 'a') and (`test`.`s1`.`key1` = `test`.`s2`.`key2`))

explain format=json select * from s1 inner join s2 where s1.common_filed = 'a' and s1.key1 = s2.key2;


