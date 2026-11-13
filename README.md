# Métodos para Tomada de Decisão — NI2

Material acadêmico: análise multicritério com AHP, CRITIC, SAW, TOPSIS, PROMETHEE II e SMAA.

## Decisão final: L10

Escolhemos **L10** para a priorização acadêmica da carteira, considerando a base disponível e as preferências AHP adotadas. Custódia e média das movimentações recebem conjuntamente 87,22% do peso. L10 lidera SAW (0,809566), TOPSIS (0,817896) e PROMETHEE II (fluxo líquido 0,758439) com esses pesos. A concordância é evidência complementar, não votação entre modelos independentes.

A decisão está tomada: priorizar L10. A análise de sensibilidade documenta os limites da recomendação: na SMAA com ordem dos pesos, L10 fica em primeiro em 61,73% das amostras; na SMAA livre, L04 tem maior aceitabilidade de primeiro lugar (30,27%, contra 24,55% de L10). Essas frequências não medem probabilidade de acerto ou sucesso comercial. No SAW, elevar o peso de C2 de 8,53% para 14,2249%, reescalando proporcionalmente os demais, empata L10/L04. TOPSIS–CRITIC também indica L10, com vantagem pequena sobre L08 (0,006522). Esse teste descreve outro cenário, sem deixar em aberto a escolha de L10 para o cenário definido.

A atualização torna explícita a decisão, sem alterar os dados, fórmulas ou rankings. Não autoriza implantação operacional ou concessão de crédito.

## Arquivos
- **apresentacao/**: slides finais v6 (15 slides), em PowerPoint e PDF.
- **entregaveis/**: relatório explicativo v4 em PDF, Word e texto; planilha de cálculos v4; código e pacote de reprodução.
- **roteiro/**: roteiro de apresentação de 10 minutos e dossiê de perguntas v4, em PDF e Word.

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

Os resultados são para análise acadêmica, não uma decisão operacional validada. O período informado é 01/08/2026 a 31/08/2026. Os valores agregados foram preservados, sem recálculo com microdados. As versões anteriores permanecem no histórico Git e nos arquivos locais de trabalho.

Este repositório não equivale ao envio no Moodle. Não há licença ampla concedida para redistribuição dos dados ou materiais de terceiros.
