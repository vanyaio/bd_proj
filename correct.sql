3:
select * from
student_subj
left join
(select distinct student_subj.student_id, subj_id from
(select student_id,exam_id
from student_distrib,exam_distrib
where exam_distrib_id = exam_distrib.id) as t1, student_subj
where
student_subj.student_id = t1.student_id
order by student_subj.student_id, subj_id) as t2
on
t2.student_id = student_subj.student_id
and t2.subj_id = student_subj.subj_id;

4:
select id as student_id, req_subj.subj_id as rsi
from student,req_subj

except

select student_subj.student_id, req_subj.subj_id as rsi
from
req_subj,student_subj
where req_subj.subj_id = student_subj.subj_id 
order by rsi;

5:
not in his school:

select id from
student

except

select t2.student_id from
classroom,
(select student_id, school_id, t1.classroom_id
from
student,
(select student_id, classroom_id
from student_distrib,exam_distrib
where exam_distrib_id = exam_distrib.id) as t1
where student.id = t1.student_id) as t2
where classroom.id = t2.classroom_id
	  and classroom.school_id = t2.school_id;
