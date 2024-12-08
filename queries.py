import sqlite3
import pandas as pd

def sqlite_to_dataframe(sql_script):
    # Create a connection to an in-memory SQLite database
    conn = sqlite3.connect('student_alcohol_data.db')
    cursor = conn.cursor()
    
    # Execute the provided SQL script
    cursor.execute(sql_script)
    
    results = cursor.fetchall()

    # Fetch column names from the cursor
    column_names = [description[0] for description in cursor.description]
    
    # Convert to DataFrame with column names
    results = pd.DataFrame(results, columns=column_names)

    
    # Close the connection
    conn.close()
    
    return results

# All students scatter plot, study & going out times
byGrade = """
SELECT final_grade as 'Final Grade' ,round(AVG(study_time),2) AS 'Average Study Ranking', round(AVG(go_out),2) AS 'Average Party Ranking'
FROM student
INNER JOIN grades
ON student.student_id = grades.student_id
GROUP BY final_grade 
ORDER BY round(AVG(study_time),2) DESC
"""
byGrade = sqlite_to_dataframe(byGrade)

#Data Overview
overview_sql = """
SELECT 
	s.student_id ,
	s.sex ,
	s.age ,
	s.parent_status ,
	s.study_time ,
	s.failures ,
	s.activities ,
	s.higher_edu ,
	s.family_relationship ,
	s.free_time ,
	s.go_out ,
	s.workday_alcohol ,
	s.weekend_alcohol ,
	s.health_status ,
	s.absences ,
	s.currently_dating ,
	s.tutored ,
	g.s1_grade ,
	g.s2_grade ,
	g.final_grade 
FROM
	student s
JOIN
	grades g
ON s.student_id = g.student_id ;
"""

overview_sql = sqlite_to_dataframe(overview_sql)

#Does alcohol consumption affect student performance?
Q1 = """
SELECT 
	g.final_grade as "Final Grade",
	AVG(s.workday_alcohol) as "Average Daily Consumption"  
FROM
	student s
join
	grades g
on
	s.student_id = g.student_id 
GROUP BY
	g.final_grade
order BY 
	"Average Daily Consumption" DESC;
"""
Q1 = sqlite_to_dataframe(Q1)

#What are the common traits among the students who consume alcohol frequently during the week?

Q4_1 = """
SELECT sex AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY sex
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_1 = sqlite_to_dataframe(Q4_1)

Q4_2 = """
SELECT age AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY age
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_2 = sqlite_to_dataframe(Q4_2)

Q4_3 = """
SELECT parent_status AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY parent_status 
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_3 = sqlite_to_dataframe(Q4_3)

Q4_4 = """
SELECT study_time AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY study_time 
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_4 = sqlite_to_dataframe(Q4_4)

Q4_5 = """
SELECT failures AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY failures
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_5 = sqlite_to_dataframe(Q4_5)

Q4_6 = """
SELECT activities AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY activities
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_6 = sqlite_to_dataframe(Q4_6)

Q4_7 = """
SELECT higher_edu AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY higher_edu 
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_7 = sqlite_to_dataframe(Q4_7)

Q4_8 = """
SELECT family_relationship AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY family_relationship 
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_8 = sqlite_to_dataframe(Q4_8)

Q4_9 = """
SELECT free_time AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY free_time
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_9 = sqlite_to_dataframe(Q4_9)

Q4_10 = """
SELECT go_out AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY go_out
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_10 = sqlite_to_dataframe(Q4_10)

Q4_11 = """
SELECT weekend_alcohol AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY weekend_alcohol
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_11 = sqlite_to_dataframe(Q4_11)

Q4_12 = """
SELECT health_status AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY health_status
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_12 = sqlite_to_dataframe(Q4_12)

Q4_13 = """
SELECT absences AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY absences
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_13 = sqlite_to_dataframe(Q4_13)

Q4_14 = """
SELECT currently_dating AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY currently_dating 
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_14 = sqlite_to_dataframe(Q4_14)

Q4_15 = """
SELECT tutored AS "Trait",
COUNT(*), ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) AS "Percent Of Total"
FROM student 
WHERE workday_alcohol IN (4,5)
GROUP BY tutored 
ORDER BY ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER(), 1) DESC
LIMIT 1;
"""
Q4_15 = sqlite_to_dataframe(Q4_15)

stacked_df = pd.concat([Q4_1, Q4_2, Q4_3, Q4_4, Q4_5, Q4_6, Q4_7, Q4_8, Q4_9, Q4_10, Q4_11, Q4_12, Q4_13, Q4_14, Q4_15], axis=0, ignore_index=True)
stacked_df1 = stacked_df.drop(columns='COUNT(*)', inplace=False)
stacked_df1["Category"] = ["Sex", "Age", "Parent Status", "Study Time", "Failures", "Activities", "Higher Education", "Family Relationship", "Free Time", "Go Out", "Weekend Alcohol", "Health Status", "Absenses", "Currently Dating", "Tutored"]
print(stacked_df1)


# How does alcohol consumption vary among genders?
Q8 = """
SELECT
	sex as Gender,
	round(AVG(workday_alcohol),2) AS 'Workday Consumpton',
	round(AVG(weekend_alcohol),2) AS 'Weekend Consumption'
FROM
	student
GROUP BY
	Gender
"""
Q8 = sqlite_to_dataframe(Q8)

# Should students abstain from alcohol in order to do better in school?
Q6 = """
SELECT SUM((student.workday_alcohol + student.weekend_alcohol)) AS Alcohol_Consumption, grades.final_grade AS Final_Grade
FROM student
INNER JOIN grades 
ON student.student_id = grades.student_id
GROUP BY grades.final_grade
ORDER BY grades.final_grade ASC;
"""
Q6 = sqlite_to_dataframe(Q6)

# Does being in a relationship affect drinking habits?

Q7 = """
SELECT 
    workday_alcohol AS "Workday Alcohol Consumption",
    currently_dating AS "Currently Dating",
    COUNT(*) AS "Count of Students",
    ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY currently_dating)), 1) AS "Percent of Total"
FROM student
GROUP BY workday_alcohol, currently_dating;
"""
Q7 = sqlite_to_dataframe(Q7)



Q10 = """
SELECT
	student.workday_alcohoL,
	grades.final_grade,
	COUNT(final_grade) AS final_grade_count
FROM
	student
INNER JOIN grades
		USING(student_id)
GROUP BY
	student.workday_alcohol,
	grades.final_grade
ORDER BY
	student.workday_alcohol;
"""
Q10 = sqlite_to_dataframe(Q10)

Q10_2 = """
SELECT
	CASE 
		WHEN workday_alcohol = 1 AND weekend_alcohol >= 3 THEN "Weekend Only Drinkers"
		WHEN workday_alcohol >= 2 AND weekend_alcohol >= 3 THEN"Any Day Drinkers"
	END AS "Drinker Category",	
	g.final_grade AS 'Final Grade',
	COUNT(final_grade) AS 'Count of Final Grade'
FROM
	student s
INNER JOIN grades g
		USING(student_id)
WHERE s.weekend_alcohol >= 3 AND (workday_alcohol = 1 OR workday_alcohol >=3)
GROUP BY "Drinker Category", final_grade 
"""
Q10_2 = sqlite_to_dataframe(Q10_2)

Q10_3 = """
SELECT
    drinker_category,
    final_grade,
    COUNT(final_grade) AS count_of_final_grade,
    ROUND(
        COUNT(final_grade) * 100.0 / SUM(COUNT(final_grade)) OVER (PARTITION BY drinker_category),
        2
    ) AS percentage_of_category
FROM (
    SELECT
        CASE 
            WHEN workday_alcohol = 1 AND weekend_alcohol >= 3 THEN "Weekend Only Drinkers"
            WHEN workday_alcohol >= 2 AND weekend_alcohol >= 3 THEN "Any Day Drinkers"
        END AS drinker_category,	
        g.final_grade AS final_grade
    FROM
        student s
    INNER JOIN grades g
        USING(student_id)
    WHERE s.weekend_alcohol >= 3 AND (workday_alcohol = 1 OR workday_alcohol >= 3)
) subquery
GROUP BY drinker_category, final_grade
ORDER BY drinker_category, final_grade;
"""
Q10_3 = sqlite_to_dataframe(Q10_3)
