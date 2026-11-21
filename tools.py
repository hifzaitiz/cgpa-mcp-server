COURSES = {
    1: [("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0)],

    2: [("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5)],

    3: [("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5)],

    4: [("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5)],

    5: [("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5)],

    6: [("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5)],

    7: [("CC-411", "Final Year Project - I", 2.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 3.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5)],

    8: [("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5)],
}


def marks_to_grade_points(marks: int) -> float | str:
    """
    Use this when a student tells you the marks they got in one course.
    It gives back the grade points for that course. Call it once for each
    course, then pass the grade points to the GPA tool.
    """
    if marks < 0 or marks > 100:
        return "Error: marks must be between 0 and 100"
    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0
    
    
def calculate_semester_gpa(grade_points: list[float], credit_hours: list[float]) -> float | str:
    """
    Use this when you already have the grade points and credit hours of all
    courses in a semester and need the semester GPA. It needs grade points,
    not marks, so convert marks with marks_to_grade_points first.
    Both lists must be in the same order: item 0 of each list is the same course.
    """
    if len(grade_points) == 0 or len(credit_hours) == 0:
        return "Error: no courses given"

    if len(grade_points) != len(credit_hours):
        return "Error: grade points and credit hours must have the same number of items"

    for gp in grade_points:
        if gp < 0 or gp > 4.0:
            return "Error: grade points must be between 0 and 4.0"

    for ch in credit_hours:
        if ch <= 0:
            return "Error: credit hours must be more than 0"

    numer = 0
    denomi = 0
    for i in range(len(grade_points)):
        numer = numer + grade_points[i] * credit_hours[i]
        denomi = denomi + credit_hours[i]

    return round(numer / denomi, 2)

def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float,semester_gpa: float, semester_credit_hours: float) -> float | str:
    """
    Use this after the semester GPA has been worked out, when the student
    wants to know their new CGPA. It needs the current CGPA, the credit hours
    already completed, this semester's GPA and this semester's credit hours.
    """
    if current_cgpa < 0 or current_cgpa > 4.0:
        return "Error: current CGPA must be between 0 and 4.0"
    if semester_gpa < 0 or semester_gpa > 4.0:
        return "Error: semester GPA must be between 0 and 4.0"
    if completed_credit_hours < 0:
        return "Error: completed credit hours cannot be negative"
    if semester_credit_hours <= 0:
        return "Error: semester credit hours must be more than 0"

    top = current_cgpa * completed_credit_hours + semester_gpa * semester_credit_hours
    bottom = completed_credit_hours + semester_credit_hours
    return round(top / bottom, 2)


def required_gpa_for_target(target_cgpa: float, current_cgpa: float,completed_credit_hours: float,remaining_credit_hours: float) -> float | str:
    """
    Use this when the student has a target CGPA and wants to know what GPA
    they need in their remaining credit hours to reach it. Get the remaining
    credit hours from get_remaining_credit_hours first.
    The answer can be above 4.0, which means the target can't be reached
    in that many credit hours.
    """
    if target_cgpa < 0 or target_cgpa > 4.0:
        return "Error: target CGPA must be between 0 and 4.0"
    if current_cgpa < 0 or current_cgpa > 4.0:
        return "Error: current CGPA must be between 0 and 4.0"
    if completed_credit_hours < 0:
        return "Error: completed credit hours cannot be negative"
    if remaining_credit_hours <= 0:
        return "Error: remaining credit hours must be more than 0"

    total = completed_credit_hours + remaining_credit_hours
    needed = (target_cgpa * total - current_cgpa * completed_credit_hours) / remaining_credit_hours
    return round(needed, 2)


def get_semester_courses(semester: int) -> str:
    """
    Use this when the student asks which courses are in a semester, or when
    you need a semester's courses and credit hours before doing a calculation.
    It lists every course with its credit hours and gives the total at the end.
    """
    if semester < 1 or semester > 8:
        return "Error: semester must be between 1 and 8"

    text = ""
    total = 0
    for code, name, ch in COURSES[semester]:
        text = text + f"{code} - {name} ({ch} credit hours)\n"
        total = total + ch

    text = text + f"Total: {total} credit hours"
    return text


def get_remaining_credit_hours(current_semester: int, last_semester: int = 8) -> float | str:
    """
    Use this when you need to know how many credit hours are left from the
    current semester up to some later semester, for example before calling
    required_gpa_for_target. The current semester counts as remaining.
    For a target-CGPA question, always pass last_semester and start with it
    equal to current_semester, so only this semester is counted. If the
    required GPA comes out above 4.0, increase last_semester by 1 and try again.
    If last_semester is left out, it counts all the way to graduation (semester 8).
    For example, current_semester=5 and last_semester=5 gives only semester 5's hours.
    It can also count past semesters: pass current_semester=1 and last_semester
    as the semester before the student's current one to get their completed hours.
    """
    if current_semester < 1 or current_semester > 8:
        return "Error: current semester must be between 1 and 8"
    if last_semester < current_semester or last_semester > 8:
        return "Error: last semester must be between the current semester and 8"

    total = 0
    for sem in range(current_semester, last_semester + 1):
        for code, name, ch in COURSES[sem]:
            total = total + ch
    return total


def save_report(filename: str, content: str) -> str:
    """
    Use this only when the student asks to save the report to a file.
    Do not call it on your own.
    """
    if filename == "":
        return "Error: filename cannot be empty"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Report saved to {filename}"
    except OSError:
        return f"Error: could not save the file {filename}"


tools = [
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report,
]


if __name__ == "__main__":
    print(marks_to_grade_points(85))
    print(marks_to_grade_points(84))
    print(marks_to_grade_points(49))
    print(marks_to_grade_points(101))

    print(calculate_semester_gpa([3.3, 4.0, 2.3], [3.0, 3.0, 3.0]))
    print(calculate_semester_gpa([4.0, 2.0], [3.0, 0.5]))
    print(calculate_semester_gpa([4.0], [3.0]))
    print(calculate_semester_gpa([3.0, 4.0], [3.0]))
    print(calculate_semester_gpa([], []))
    print(calculate_semester_gpa([5.0], [3.0]))
    print(calculate_semester_gpa([3.0], [0.0]))

    print(calculate_new_cgpa(3.0, 64, 3.2, 18.5))
    print(calculate_new_cgpa(5.0, 64, 3.2, 18.5))

    print(required_gpa_for_target(3.4, 3.0, 64, 18.5))
    print(required_gpa_for_target(3.4, 3.0, 64, 37))
    print(required_gpa_for_target(3.4, 3.0, 64, 55.5))
    print(required_gpa_for_target(3.4, 3.0, 64, 0))

    print(get_semester_courses(5))
    print(get_semester_courses(9))

    print(get_remaining_credit_hours(5))
    print(get_remaining_credit_hours(5, 5))
    print(get_remaining_credit_hours(5, 4))

    print(save_report("test_report.txt", "Hello"))
    print(save_report("", "Hello"))
