-- вариант 3
use supplies;
-- 30
select DetailNumber from supplies where ProjectNumber in (select ProjectNumber from projects where ProjectTown = "Лондон");
 --  13
SELECT distinct projects.ProjectNumber
FROM suppliers INNER JOIN (projects INNER JOIN supplies 
ON projects.ProjectNumber = supplies.ProjectNumber)
ON suppliers.SupplierNumber = supplies.SupplierNumber
WHERE (suppliers.SupplierTown<>projects.ProjectTown); 
-- 21
select DetailNumber from supplies where ProjectNumber in (select ProjectNumber from projects where ProjectTown = "Лондон");
-- 12
SELECT distinct details.DetailNumber
FROM suppliers INNER JOIN (details INNER JOIN (projects INNER JOIN supplies 
ON projects.ProjectNumber = supplies.ProjectNumber)
ON details.DetailNumber = supplies.DetailNumber) ON suppliers.SupplierNumber = supplies.SupplierNumber
WHERE (suppliers.SupplierTown=projects.ProjectTown); 
-- 28
select ProjectNumber from supplies where (SupplierNumber in (
select SupplierNumber from Suppliers where SupplierTown = "Лондон")) and (DetailNumber in (
select DetailNumber from Details where DetailColor = "Красный")); 
-- 3
select SupplierNumber from supplies where ProjectNumber = "ПР1";
-- 7
select distinct details.DetailNumber, projects.ProjectNumber, suppliers.SupplierNumber
from suppliers inner join (details inner join (projects inner join supplies 
on projects.ProjectNumber = supplies.ProjectNumber)
on details.DetailNumber = supplies.DetailNumber) ON suppliers.SupplierNumber = supplies.SupplierNumber
WHERE (suppliers.SupplierTown<>projects.ProjectTown) and (details.DetailTown<>suppliers.SupplierTown) and (projects.ProjectTown<>details.DetailTown); 
-- 32
select ProjectNumber from supplies
where (SupplierNumber = 'П1') and (ProjectNumber not in (
	select ProjectNumber from supplies
  	where (SupplierNumber != 'П1')
));
-- 2
select * from projects where ProjectTown = "Лондон";
-- 18
select DetailNumber from supplies where Number_of_details > 320 and ProjectNumber = "ПР1"; 