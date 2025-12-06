# Simulação de Relógios Lógicos de Lamport - README

## 📝 Descrição

Implementação do algoritmo de Relógios Lógicos de Lamport para ordenação de eventos em sistemas distribuídos assíncronos.

## 🎯 Funcionalidades

- ✅ Simulação de 3 processos concorrentes (P1, P2, P3)
- ✅ Implementação completa das Regras de Lamport
- ✅ Rastreamento de timestamps para cada evento
- ✅ Visualização do estado dos relógios em cada etapa

## 🚀 Como Executar

```bash
python lamport_clock_simulation.py
```

Ou use o script de teste:

```bash
python run_simulation.py
```

## 📊 Resultado da Simulação

### Estado Final dos Relógios
- **P1**: 5
- **P2**: 4
- **P3**: 3

### Sequência de Eventos Simulada
1. P1: Evento interno → L1 = 1
2. P2: Envia mensagem para P3 → L2 = 1
3. P3: Recebe mensagem de P2 → L3 = 2
4. P1: Envia mensagem para P2 → L1 = 2
5. P3: Evento interno → L3 = 3
6. P2: Recebe mensagem de P1 → L2 = 3
7. P2: Envia mensagem para P1 → L2 = 4
8. P1: Recebe mensagem de P2 → L1 = 5

## 🔧 Arquitetura

### Classe `Process`
- **Atributos:**
  - `name`: Identificador do processo
  - `clock`: Relógio lógico (inicia em 0)
  - `message_queue`: Fila de mensagens recebidas

- **Métodos:**
  - `internal_event()`: Executa evento interno
  - `send_message(destination)`: Envia mensagem com timestamp
  - `receive_message()`: Recebe e processa mensagem

## 📚 Regras Implementadas

### Regra 1
Antes de executar qualquer evento, o processo incrementa seu relógio:
```
L_i = L_i + 1
```

### Regra 2 (Envio)
Ao enviar mensagem, inclui timestamp atual:
```
send(mensagem, L_i)
```

### Regra 2 (Recebimento)
Ao receber mensagem com timestamp t:
```
L_j = max(L_j, t)
L_j = L_j + 1
```

## 📂 Arquivos

- `lamport_clock_simulation.py`: Implementação principal
- `run_simulation.py`: Script de teste auxiliar
- `README.md`: Este arquivo

## 👨‍💻 Autor

Implementação para a disciplina de Sistemas Distribuídos
Tarefa 1 - Relógios Lógicos de Lamport
