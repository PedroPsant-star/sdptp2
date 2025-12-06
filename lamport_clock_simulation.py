"""
Simulação de Relógios Lógicos de Lamport
Tarefa 1 - Sistemas Distribuídos

Implementa a ordenação de eventos em um sistema assíncrono utilizando
os relógios lógicos de Lamport.
"""

class Process:
    """
    Representa um processo com seu relógio lógico de Lamport.
    """
    
    def __init__(self, name):
        """
        Inicializa um processo com relógio lógico em 0.
        
        Args:
            name (str): Nome identificador do processo (ex: "P1", "P2", "P3")
        """
        self.name = name
        self.clock = 0
        self.message_queue = []  # Fila de mensagens recebidas (mensagem, timestamp)
    
    def internal_event(self):
        """
        Regra 1: Executa um evento interno.
        Antes de executar o evento, incrementa o relógio lógico.
        """
        self.clock += 1
        print(f"[{self.name}] Evento interno. Relógio: {self.clock}")
        return self.clock
    
    def send_message(self, destination, message_content="msg"):
        """
        Regra 1 + Regra 2 (envio): Envia uma mensagem para outro processo.
        1. Incrementa o relógio (Regra 1)
        2. Inclui o timestamp atual na mensagem (Regra 2)
        
        Args:
            destination (Process): Processo destino
            message_content (str): Conteúdo da mensagem
            
        Returns:
            tuple: (mensagem, timestamp) enviados
        """
        self.clock += 1
        timestamp = self.clock
        message = (message_content, timestamp, self.name)
        destination.message_queue.append(message)
        
        print(f"[{self.name}] Envia mensagem para {destination.name} com timestamp {timestamp}. Relógio: {self.clock}")
        return message
    
    def receive_message(self):
        """
        Regra 2 (recebimento): Recebe uma mensagem da fila.
        1. Ajusta o relógio: L_j = max(L_j, t)
        2. Incrementa o relógio (Regra 1)
        
        Returns:
            tuple: (mensagem, timestamp, remetente) recebidos
        """
        if not self.message_queue:
            raise ValueError(f"Nenhuma mensagem na fila de {self.name}")
        
        message, timestamp, sender = self.message_queue.pop(0)
        
        # Regra 2: L_j = max(L_j, t)
        self.clock = max(self.clock, timestamp)
        
        # Regra 1: Incrementa antes de processar o evento
        self.clock += 1
        
        print(f"[{self.name}] Recebe mensagem de {sender} (timestamp {timestamp}). Relógio: {self.clock}")
        return (message, timestamp, sender)


def print_clock_states(processes):
    """
    Imprime o estado atual dos relógios de todos os processos.
    
    Args:
        processes (dict): Dicionário de processos {nome: Process}
    """
    print("\n--- Estado dos Relógios ---")
    for name, process in processes.items():
        print(f"{name}: {process.clock}")
    print("---------------------------\n")


def main():
    """
    Função principal que executa a simulação da sequência de eventos.
    """
    print("=" * 60)
    print("SIMULAÇÃO DE RELÓGIOS LÓGICOS DE LAMPORT")
    print("=" * 60)
    print()
    
    # Criar os 3 processos
    p1 = Process("P1")
    p2 = Process("P2")
    p3 = Process("P3")
    
    processes = {"P1": p1, "P2": p2, "P3": p3}
    
    print("Estado Inicial:")
    print_clock_states(processes)
    
    # Sequência de eventos conforme especificado
    
    # 1. P1: Evento interno
    print("Evento 1: P1 executa evento interno")
    p1.internal_event()
    print_clock_states(processes)
    
    # 2. P2: Envia mensagem para P3
    print("Evento 2: P2 envia mensagem para P3")
    p2.send_message(p3)
    print_clock_states(processes)
    
    # 3. P3: Recebe mensagem de P2
    print("Evento 3: P3 recebe mensagem de P2")
    p3.receive_message()
    print_clock_states(processes)
    
    # 4. P1: Envia mensagem para P2
    print("Evento 4: P1 envia mensagem para P2")
    p1.send_message(p2)
    print_clock_states(processes)
    
    # 5. P3: Evento interno
    print("Evento 5: P3 executa evento interno")
    p3.internal_event()
    print_clock_states(processes)
    
    # 6. P2: Recebe mensagem de P1
    print("Evento 6: P2 recebe mensagem de P1")
    p2.receive_message()
    print_clock_states(processes)
    
    # 7. P2: Envia mensagem para P1
    print("Evento 7: P2 envia mensagem para P1")
    p2.send_message(p1)
    print_clock_states(processes)
    
    # 8. P1: Recebe mensagem de P2
    print("Evento 8: P1 recebe mensagem de P2")
    p1.receive_message()
    print_clock_states(processes)
    
    print("=" * 60)
    print("SIMULAÇÃO CONCLUÍDA")
    print("=" * 60)
    print("\nResumo Final dos Relógios:")
    for name, process in processes.items():
        print(f"  {name}: {process.clock}")


if __name__ == "__main__":
    main()
