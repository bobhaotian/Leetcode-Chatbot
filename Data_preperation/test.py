import pandas as pd
import re


def remove_explanation(input_str):
    # Initialize variables
    code_lines = []
    inside_code_block = False
    last_return_line = None

    # Split the input string into lines
    liness = input_str.split('\n')

    for line in liness:
        # Check for the start or end of a code block
        if '```' in line:
            break

        # Check if the line is part of the code block
        if line.strip() and not re.match(r'^\s*#', line):
            if 'return' in line:
                last_return_line = line
            code_lines.append(line)
    return '\n'.join(code_lines).strip()


# Load the CSV file
df = pd.read_csv('leetcode_python.csv')
solutions = df['Solution']
indent = "    "
solution_idx = 0
solution_len = len(solutions)

while solution_idx < solution_len:
    solution = solutions[solution_idx]
    trim_solution = remove_explanation(solution.strip())
    lines = trim_solution.split('\n')
    first_line = lines[0].strip()

    if first_line != 'class Solution:':
        if first_line.startswith('def'):
            final_solution = 'class Solution:\n'
            indented_lines = [indent + line for line in lines]
            final_solution += '\n'.join(indented_lines) + '\n'
            df.loc[solution_idx, 'Solution'] = final_solution
            solution_idx += 1
        else:
            lines.pop(0)
            update_solution = '\n'.join(lines) + '\n'
            df.loc[solution_idx, 'Solution'] = update_solution
    else:
        df.loc[solution_idx, 'Solution'] = trim_solution + '\n'
        solution_idx += 1

df.to_csv('leetcode_python_updated.csv', index=False)

