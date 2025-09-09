# 📡 NASA Probes — Dashboards de Exoplanetas

Projeto em desenvolvimento por **Tony Del Nero**, com foco em análise e visualização de dados de exoplanetas detectados por sondas da NASA.

---

## 🚀 Objetivo

Explorar dados astronômicos com ferramentas de ciência de dados e visualização, criando dashboards interativos que facilitam a interpretação de características físicas dos exoplanetas — como massa, raio e temperatura estelar — e suas tendências ao longo do tempo.

---

## 📁 Estrutura do Projeto


| Caminho                          | Conteúdo / Finalidade                                                                 |
|----------------------------------|----------------------------------------------------------------------------------------|
| `data/`                          | 📊 Arquivos de dados originais, como o CSV da NASA                                    |
| `data/tmp/`                      | 🧪 Arquivos temporários gerados por scripts, como amostras de dados                   |
| `scripts/`                       | 🐍 Scripts Python para manipulação e preparação dos dados                             |
| `notebooks/`                     | 📓 Notebooks Jupyter para análises exploratórias (em desenvolvimento)                |
| `powerbi/`                       | 📈 Dashboards interativos criados no Power BI                                         |
| `README.md`                      | 📘 Documentação do projeto                                                             |


## 🧠 Tecnologias Utilizadas

- **Python**: manipulação e limpeza de dados com `pandas` e `pathlib`
- **Power BI**: construção de dashboards interativos com segmentadores, gráficos estatísticos e KPIs
- **Git & GitHub**: versionamento e publicação do projeto
- **Jupyter Notebooks**: análises exploratórias

---


## ✅ Funcionalidades Concluídas

- Script `open_armory.py` para carregamento seguro de arquivos CSV e padronização de colunas
- ETL completo para geração de amostra tratada dos dados originais
- Dashboard Power BI com:
  - KPIs de massa, raio e total de exoplanetas
  - Gráfico de dispersão (massa × raio)
  - Tabela estatística por faixa de temperatura estelar
  - Segmentador temporal (1995–2023)
  - Gráfico de descobertas por ano
- Organização modular do repositório para facilitar manutenção e expansão


---


## 👨‍💻 Autor

**Tony Del Nero**  
Desenvolvedor e entusiasta de dados espaciais  
GitHub: [delneronitoni](https://github.com/delneronitoni)

---

> Este projeto está finalizado em sua primeira versão, com ETL completo e dashboard da amostra criado. Novas extensões e análises poderão ser adicionadas futuramente.


