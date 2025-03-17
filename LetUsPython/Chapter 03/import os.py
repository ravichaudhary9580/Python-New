import os

def count_problems_in_file(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip().startswith('# Problem'):
                count += 1
    return count

def count_problems_in_repo(repo_path):
    total_count = 0
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                total_count += count_problems_in_file(file_path)
                print(count_problems_in_file(file_path),file_path)
    return total_count

repo_path = r'c:\RAVI\Coding\Python'
total_problems = count_problems_in_repo(repo_path)
print(f'Total number of problems: {total_problems}')