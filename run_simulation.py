"""
Script de teste para visualizar a saída da simulação de Lamport
"""

import subprocess
import sys

print("Executando simulação de Relógios Lógicos de Lamport...\n")
print("=" * 70)

result = subprocess.run(
    [sys.executable, "lamport_clock_simulation.py"],
    capture_output=True,
    text=True
)

print(result.stdout)

if result.returncode == 0:
    print("\n✅ Simulação executada com sucesso!")
else:
    print("\n❌ Erro na execução:")
    print(result.stderr)
