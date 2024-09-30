
# Dicionário para armazenar resultados dos estudantes
results = {}

def add_result(student_name, phase, score):
    if student_name not in results:
        results[student_name] = {}
    results[student_name][phase] = score

def get_result(student_name, phase):
    return results.get(student_name, {}).get(phase, "No result for this phase")

# Exemplo de uso
add_result("Dr. João", "Phase 1", 85)
add_result("Dr. João", "Phase 2", 90)
print(get_result("Dr. João", "Phase 1"))  # Output: 85

results = []

def add_result(student_name, phase, score):
    results.append((student_name, phase, score))

def get_result(student_name, phase):
    for s_name, s_phase, s_score in results:
        if s_name == student_name and s_phase == phase:
            return s_score
    return "No result for this phase"

# Exemplo de uso
add_result("Dra. Maria", "Phase 1", 88)
add_result("Dra. Maria", "Phase 2", 92)
print(get_result("Dra. Maria", "Phase 1"))  # Output: 88

# Lista para armazenar resultados de forma aninhada
results = []

def add_result(results, student_name, phase, score):
    if not results:
        results.extend([student_name, phase, score, []])
    else:
        add_result_recursive(results, student_name, phase, score)

def add_result_recursive(node, student_name, phase, score):
    if not node[3]:
        node[3] = [student_name, phase, score, []]
    else:
        add_result_recursive(node[3], student_name, phase, score)

def get_result(results, student_name, phase):
    return get_result_recursive(results, student_name, phase)

def get_result_recursive(node, student_name, phase):
    if node[0] == student_name and node[1] == phase:
        return node[2]
    elif node[3]:
        return get_result_recursive(node[3], student_name, phase)
    return "No result for this phase"

# Exemplo de uso
add_result(results, "Dr. Pedro", "Phase 1", 80)
add_result(results, "Dr. Pedro", "Phase 2", 75)
print(get_result(results, "Dr. Pedro", "Phase 1"))  # Output: 80