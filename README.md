# mlops-pipeline

**Autor:** Gabriel Vagula Gomes Baffa Clavero

Projeto desenvolvido como parte do exercício de modularização do pipeline de Machine Learning do curso de MLOps.

## Estrutura do projeto

```text
mlops-pipeline/
├── data/
│   └── raw/
│       └── points.csv
├── src/
│   ├── data.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── outputs/
│   └── metrics.json
├── generate_data.py
├── main.py
└── requirements.txt
```

## Funcionalidades

O projeto organiza o pipeline de clustering em módulos independentes:

- **data.py:** carregamento e preparação dos dados.
- **train.py:** treinamento do modelo KMeans.
- **evaluate.py:** avaliação do modelo.
- **predict.py:** previsão de clusters e cálculo de distâncias.

O arquivo `main.py` integra todas as etapas e salva os resultados em `outputs/metrics.json`.

## Como executar

1. Instalar as dependências:

```bash
pip install -r requirements.txt
```

2. Gerar os dados:

```bash
python generate_data.py
```

3. Executar o pipeline:

```bash
python main.py
```

Após a execução, as métricas de avaliação e a predição de exemplo serão exibidas no terminal e salvas no arquivo `outputs/metrics.json`.

## GitHub

Repositório público: https://github.com/gabrielvbaffa-oss/mlops-pipeline
