# CGPA MCP Server

An MCP server (FastMCP) that shares the PUCIT BS(CS) GPA/CGPA tools:
`marks_to_grade_points`, `calculate_semester_gpa`, `calculate_new_cgpa`,
`required_gpa_for_target`, `get_semester_courses`, `get_remaining_credit_hours`
and `save_report`.

## Run locally

```
pip install -r requirements.txt
python server.py        # serves http://127.0.0.1:8000/mcp
```

## Test without an agent

```
fastmcp list server.py
fastmcp call server.py marks_to_grade_points marks=78
```
