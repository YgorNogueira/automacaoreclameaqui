import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    # Separa as reclamações usando um separador consistente
    complaints = []
    current_complaint = {"titulo": "", "descricao": "", "resolvida": "", "tempo_envio": ""}
    in_description = False
    
    for line in content.split('\n'):
        stripped = line.strip()
        
        if not stripped:
            continue  # Ignora linhas vazias
            
        # Detecta início de nova reclamação
        if not current_complaint["titulo"]:
            current_complaint["titulo"] = stripped
            in_description = True
            continue
            
        # Detecta status e tempo
        if stripped in ["Respondida", "Resolvido", "Não resolvido"]:
            current_complaint["resolvida"] = stripped
            continue
            
        if stripped.startswith("Há "):
            current_complaint["tempo_envio"] = stripped
            # Finaliza a reclamação quando encontramos o tempo
            complaints.append(current_complaint)
            current_complaint = {"titulo": "", "descricao": "", "resolvida": "", "tempo_envio": ""}
            in_description = False
            continue
            
        # Se estamos na descrição
        if in_description:
            # Se já temos conteúdo na descrição, adiciona quebra de linha
            if current_complaint["descricao"]:
                current_complaint["descricao"] += "\n" + stripped
            else:
                current_complaint["descricao"] = stripped
    
    # Escreve no arquivo CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['titulo', 'descricao', 'resolvida', 'tempo_envio']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        
        writer.writeheader()
        for complaint in complaints:
            writer.writerow(complaint)

# Uso
txt_to_csv('reclamacoes_normalizadas.txt', 'reclamacoes.csv')