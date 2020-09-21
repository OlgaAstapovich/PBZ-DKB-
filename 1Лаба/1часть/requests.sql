USE education;
-- 1
select * from teacher;
-- 2
select * from students_group where speciality = "ЭВМ";
-- 3
select teacher_id, number_of_audience from teacher_subject_group where code_number_of_the_subject = "18П";
-- 4
select code_number_of_the_subject, subject_name from subject where code_number_of_the_subject in ( 
select code_number_of_the_subject from teacher_subject_group where teacher_id in (
select teacher_id from teacher where surname = "Костин"));
-- 5
select group_code_number from teacher_subject_group where teacher_id in (select teacher_id from teacher where surname = "Фролов");
-- 6
select * from subject where speciality = "АСОИ";
-- 7
select * from teacher where speciality LIKE "%АСОИ%";
-- 8
select surname from teacher where teacher_id in (select teacher_id from teacher_subject_group where number_of_audience = 210);
-- 9
select subject_name from subject where code_number_of_the_subject in (
select code_number_of_the_subject from teacher_subject_group where (number_of_audience >100) and (number_of_audience <200))
union select group_name from students_group where group_code_number in (
select group_code_number from teacher_subject_group where (number_of_audience >100) and (number_of_audience <200));  
-- 10
select a.group_code_number as group_code_number_1, b.group_code_number as group_code_number_2 
from students_group a, students_group b where a.group_name > b.group_name
and a.speciality = b.speciality;
-- 11
select SUM(number_of_persons) from students_group where speciality = "ЭВМ";
-- 12
select teacher_id from teacher_subject_group where group_code_number in (
select group_code_number from students_group where speciality = "ЭВМ");
-- 13
select code_number_of_the_subject from subject where code_number_of_the_subject in (
select code_number_of_the_subject from teacher_subject_group where (group_code_number = "8Г") 
and (group_code_number = "7Г") and (group_code_number = "3Г") and (group_code_number = "4Г") 
and (group_code_number = "17Г") and (group_code_number = "12Г") and (group_code_number = "10Г"));
-- 14
select surname from teacher where teacher_id in (
select teacher_id from teacher_subject_group where code_number_of_the_subject in (
select code_number_of_the_subject from teacher_subject_group where teacher_id in (
select teacher_id from teacher_subject_group where code_number_of_the_subject="14П")));
-- 15
select * from subject where code_number_of_the_subject not in (
select code_number_of_the_subject from teacher_subject_group where teacher_id = "221Л");
-- 16
select * from subject where code_number_of_the_subject not in (
select code_number_of_the_subject from teacher_subject_group where group_code_number in (
select group_code_number from students_group where group_name = "М-6"));
-- 17
select * from teacher where (teacher_position = "Доцент") and (teacher_id in (
select teacher_id from teacher_subject_group where (group_code_number ="3Г") or (group_code_number ="8Г")));
-- 18
select code_number_of_the_subject, teacher_id, group_code_number from teacher_subject_group where teacher_id in (
select teacher_id from teacher where (department = "ЭВМ") and (speciality LIKE "%АСОИ%"));
-- 19
select group_code_number from students_group where speciality in (
select speciality from teacher);
-- 20
select teacher_id from teacher where (department = "ЭВМ") and (teacher_id in (
select teacher_id from teacher_subject_group where code_number_of_the_subject in (
select code_number_of_the_subject from subject where speciality in (select speciality from students_group))));
-- 21
select speciality from students_group where group_code_number in (
select group_code_number from teacher_subject_group where teacher_id in (
select teacher_id from teacher where department ="АСУ"));
-- 22
select code_number_of_the_subject from teacher_subject_group where group_code_number in (
select group_code_number from students_group where group_name ="АС-8");
-- 23
select group_code_number from students_group where group_code_number in (
select group_code_number from teacher_subject_group where code_number_of_the_subject in (
select code_number_of_the_subject from teacher_subject_group where group_code_number in (
select group_code_number from students_group where group_name ="АС-8")));
-- 24
select group_code_number from students_group where group_code_number not in (
select group_code_number from teacher_subject_group where code_number_of_the_subject in (
select code_number_of_the_subject from teacher_subject_group where group_code_number in (
select group_code_number from students_group where group_name ="АС-8")));
-- 25
select group_code_number from students_group where group_code_number not in (
select group_code_number from teacher_subject_group where teacher_id = "430Л");
-- 26
select teacher_id from teacher where teacher_id in (
select teacher_id from teacher_subject_group where (group_code_number in (
select group_code_number from students_group where group_name = "Э-15")) and (code_number_of_the_subject != "12П"));

