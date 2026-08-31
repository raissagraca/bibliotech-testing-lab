# Missão QA — BiblioTech

Projeto da aula prática de QA com testes de caixa preta, caixa branca, cobertura,
pytest e GitHub Actions.

## Executar

```bash
pip install -r requirements-dev.txt
pytest -v
pytest --cov=src --cov-branch --cov-report=term-missing
```

## Escopo
- RF01 — Permissão para empréstimo
- RF02 — Multa por atraso
- RF03 — Classificação de atraso

O projeto segue a atividade proposta na aula e documenta casos, rastreabilidade,
testes automatizados, cobertura e parecer de QA.
