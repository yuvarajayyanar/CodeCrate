# Write your MySQL query statement below
select e.unique_id , d.name from Employees d left join EmployeeUNI e on d.id=e.id;