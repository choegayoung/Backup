USE edu;

-- 전체 사용 가져오기
SELECT # SQL 검색 키워드
*      # 컬럼 * << 전체 컬럼 모두 가져와
FROM   # 가져오는 곳
edu.employees # 대상
;

-- 1. 사원의 이름, 성별 정보 추출

SELECT first_name, last_name, gender
FROM edu.employees;

-- 2. 부서의 부서번호, 부서명 추출

SELECT dept_no, dept_name
FROM edu.departments;

-- 3. 사원의 사원번호, 연봉 추출

SELECT emp_no, salary
FROM edu.salaries;

-- 4. 사원의 이름과 연봉 추출
SELECT e.first_name,
       e.last_name,
       s.salary
FROM edu.employees AS e
INNER JOIN edu.salaries AS s
ON (e.emp_no = s.emp_no)
;

-- 5. 사원 중 남자의 연봉 추출
SELECT e.first_name,
       e.last_name,
       s.salary,
       e.gender
FROM edu.employees AS e
INNER JOIN edu.salaries AS s
ON (e.emp_no = s.emp_no) # join 한 테이블중 같은 항목을 같다고 명시
WHERE e.gender <> 'M'  # 부정문 != , <> 이용가능
;

-- 6. 여성 사원 중 연봉이 7만 이상인 사원을 추출
SELECT e.first_name,
       e.last_name,
       s.salary,
       e.gender
FROM edu.employees AS e
INNER JOIN edu.salaries AS s
   ON (e.emp_no = s.emp_no)
WHERE e.gender = 'F'
 AND s.salary >= 70000
 AND s.to_date = '9999-01-01'
;

-- 7. 여성 사원 중 연봉 협상이 가장 많은 사원 출력
SELECT emp_no, COUNT(emp_no) AS cnt
FROM edu.salaries
GROUP BY emp_no # 집계성 함수에서는 group by를 이용해서 묶음
ORDER BY 2 DESC, 1;

-- 8. 이름까지 출력
SELECT e.first_name,
       e.last_name,
		 e.gender ,
		 s.emp_no,
		COUNT(s.emp_no) AS cnt
FROM edu.salaries AS s
INNER JOIN edu.employees AS e
ON (s.emp_no = e.emp_no)
WHERE e.gender = 'F'
GROUP BY emp_no
ORDER BY 5 DESC, 1;