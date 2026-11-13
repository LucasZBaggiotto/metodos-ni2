# Métodos para Tomada de Decisão — NI2

Material acadêmico: análise multicritério com AHP, CRITIC, SAW, TOPSIS, PROMETHEE II e SMAA.

## Arquivos
- **apresentacao/**: slides finais v4, em PowerPoint e PDF.
- **entregaveis/**: relatório explicativo v2 em PDF, Word e texto; planilha de cálculos v2; código e pacote de reprodução.
- **roteiro/**: roteiro de apresentação de 10 minutos e dossiê de perguntas v2, em PDF e Word.

## Reproduzir os cálculos
```sh
cd entregaveis
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python calcular_ni2_reproduzivel.py > resultados_recalculados.json
```
O script executa um milhão de amostras SMAA em cada um de dois cenários. O arquivo Excel contém fórmulas determinísticas e demonstrações reduzidas da simulação; consulte o LEIA-ME do pacote para as distinções.

## Escopo e limitações
Os identificadores das alternativas foram pseudonimizados. Isso não significa anonimização completa. As limitações de origem, agregação, autorização institucional e aplicação dos resultados continuam registradas nos documentos; esta publicação não comprova autorização institucional.

Os resultados são para análise acadêmica, não uma decisão operacional validada. O período informado é 01/08/2026 a 31/08/2026. Os valores agregados foram preservados, sem recálculo com microdados. As versões originais dos documentos foram mantidas.

Este repositório não equivale ao envio no Moodle. Não há licença ampla concedida para redistribuição dos dados ou materiais de terceiros.
