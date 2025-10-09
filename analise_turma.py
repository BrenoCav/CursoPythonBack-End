# analise_turma.py
alunos = [
    {"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},
    {"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},
    {"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},
    {"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},
    {"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},
    {"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0, "status_matricula": "ativo"},
    {"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},
    {"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"}
]

# 1. Filtrar alunos elegíveis: frequencia >= 75.0 e status == "ativo"
alunos_elegiveis = list(filter(
    lambda aluno: aluno['frequencia'] >= 75.0 and aluno['status_matricula'] == 'ativo',
    alunos
))

# 2. Aplicar bônus de 10% (nota máxima = 10.0)
def aplicar_bonus(aluno):
    aluno_com_bonus = aluno.copy()
    nova_nota = aluno['nota_final'] * 1.1
    aluno_com_bonus['nota_final'] = min(nova_nota, 10.0)  # Limita a 10.0
    return aluno_com_bonus

alunos_com_bonus = list(map(aplicar_bonus, alunos_elegiveis))

# 3. Identificar destaques: nota_final >= 9.0 após bônus
alunos_destaques = list(filter(
    lambda aluno: aluno['nota_final'] >= 9.0,
    alunos_com_bonus
))

# 4. Saída: nome e nota final dos destaques
print("🎓 ALUNOS DESTAQUE (com bônus aplicado):\n")
for aluno in alunos_destaques:
    print(f"{aluno['nome']}: {aluno['nota_final']:.2f}")