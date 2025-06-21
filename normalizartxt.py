def normalize_complaints(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Filtra e processa as linhas
    filtered_lines = []
    status_list = ["Respondida", "Resolvido", "Não resolvido", "Resolvida", "Não resolvida", "Respondido"]
    
    for line in lines:
        stripped = line.strip()
        
        # Remove cabeçalhos de reclamação e indicadores de página
        if stripped.startswith('--- Reclamação') or stripped.startswith('---Reclamação') or \
           (stripped.replace(' ', '').isdigit() and 'de' in stripped):
            continue
            
        # Remove linhas de separação com asteriscos
        if stripped == '*****':
            continue
            
        # Mantém apenas linhas com conteúdo relevante
        if stripped:
            filtered_lines.append(stripped)

    # Processa as reclamações
    complaints = []
    current = []
    
    for line in filtered_lines:
        current.append(line)
        
        # Verifica se encontrou o final de uma reclamação
        if len(current) >= 2:
            last_line = current[-1]
            second_last = current[-2]
            
            if second_last in status_list and last_line.startswith('Há '):
                # Separa título, descrição e status
                title = current[0]
                description_lines = current[1:-2]  # Tudo entre título e status
                status_line = current[-2]
                time_line = current[-1]
                
                # Monta a reclamação formatada
                description = '\n'.join(description_lines) if description_lines else ''
                
                if description:
                    complaint = f"{title}\n\n{description}\n\n{status_line}\n{time_line}"
                else:
                    complaint = f"{title}\n\n{status_line}\n{time_line}"
                
                complaints.append(complaint)
                current = []
    
    # Processa última reclamação se existir
    if current and len(current) >= 2:
        last_line = current[-1]
        second_last = current[-2]
        if second_last in status_list and last_line.startswith('Há '):
            title = current[0]
            description_lines = current[1:-2]
            description = '\n'.join(description_lines) if description_lines else ''
            
            if description:
                complaint = f"{title}\n\n{description}\n\n{second_last}\n{last_line}"
            else:
                complaint = f"{title}\n\n{second_last}\n{last_line}"
            
            complaints.append(complaint)

    # Salva no arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(complaints))

# Uso
normalize_complaints('reclamacoes.txt', 'reclamacoes_normalizadas.txt')