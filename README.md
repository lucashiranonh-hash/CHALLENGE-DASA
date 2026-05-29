# Challenge DASA – Sprint 2

## Sistema Inteligente de Interpretação de Relatórios Genéticos com IA Generativa

## Aluno

* Lucas Yuji Nakayama Hirano RM:563420


---

# 1. Introdução

O presente projeto foi desenvolvido para a Sprint 2 do Challenge DASA/Genera e tem como objetivo propor uma solução baseada em Inteligência Artificial Generativa para auxiliar pacientes na interpretação de seus relatórios genéticos.

A solução utiliza técnicas de Processamento de Linguagem Natural (NLP), Embeddings, Busca Semântica e Retrieval-Augmented Generation (RAG) para permitir consultas inteligentes sobre informações de ancestralidade, predisposições genéticas e bem-estar.

O foco principal é transformar informações técnicas e complexas em explicações acessíveis, mantendo precisão, rastreabilidade e segurança.

---

# 2. Objetivos

## Objetivo Geral

Desenvolver um agente especialista capaz de interpretar dados genéticos estruturados e responder perguntas em linguagem natural de forma segura e compreensível.

## Objetivos Específicos

* Implementar arquitetura baseada em RAG.
* Realizar busca semântica em relatórios genéticos.
* Utilizar embeddings para representação vetorial dos dados.
* Criar um agente especialista em genética.
* Desenvolver uma interface de chat para interação com o usuário.
* Aplicar engenharia de prompts para controlar o comportamento do modelo.
* Garantir governança e segurança das respostas.

---

# 3. Problema de Negócio

Os relatórios genéticos contêm grande quantidade de informações técnicas que podem ser difíceis de interpretar por pacientes sem formação na área da saúde.

A proposta busca criar uma ponte entre o conhecimento científico presente nos relatórios e a compreensão do usuário final, permitindo acesso mais simples e intuitivo às informações genéticas.

---

# 4. Arquitetura da Solução

## Fluxo Geral

```text
Relatório PDF
       ↓
Extração dos Dados
       ↓
JSON Estruturado
       ↓
Limpeza e Normalização
       ↓
Geração de Embeddings
       ↓
Base Vetorial (FAISS)
       ↓
Busca Semântica
       ↓
LLM + RAG
       ↓
Resposta ao Usuário
```

### Etapas

#### Extração

Os dados do relatório são convertidos para formato estruturado JSON.

#### Processamento

Os textos são limpos e organizados para indexação.

#### Embeddings

Os dados são transformados em vetores numéricos que representam seu significado semântico.

#### Base Vetorial

Os vetores são armazenados em uma base vetorial para recuperação eficiente.

#### Busca Semântica

O sistema localiza os trechos mais relevantes para cada pergunta realizada.

#### Geração de Respostas

O modelo de linguagem utiliza apenas os trechos recuperados para gerar respostas contextualizadas.

---

# 5. Tecnologias Utilizadas

## Linguagens

* Python

## Inteligência Artificial

* OpenAI GPT-4o-mini

## Frameworks

* LangChain
* Streamlit

## Banco Vetorial

* FAISS

## Controle de Versão

* GitHub

---

# 6. Estrutura RAG (Retrieval-Augmented Generation)

A arquitetura RAG foi escolhida para reduzir alucinações do modelo e garantir que as respostas sejam fundamentadas nos dados reais do relatório.

## Funcionamento

### Recuperação (Retrieval)

A pergunta do usuário é convertida em embedding e comparada aos vetores armazenados.

O sistema recupera os trechos mais relevantes do relatório.

### Geração (Generation)

Os trechos recuperados são enviados ao modelo de linguagem, que gera uma resposta baseada exclusivamente nessas informações.

---

# 7. Embeddings

Embeddings são representações numéricas de textos que permitem identificar similaridades semânticas.

## Modelo Utilizado

text-embedding-3-small

## Justificativa

* Boa performance em textos complexos.
* Baixo custo computacional.
* Integração simples com ferramentas de IA Generativa.

---

# 8. Base Vetorial

## Tecnologia Escolhida

FAISS

## Justificativa

* Alta velocidade de busca.
* Fácil implementação.
* Excelente integração com Python.
* Suporte eficiente para busca por similaridade.

---

# 9. Engenharia de Prompts

O comportamento do agente é controlado através de um System Prompt.

## Prompt Base

```text
Você é um especialista em interpretação genética.

Regras:

- Utilize apenas informações recuperadas do relatório.
- Não invente informações.
- Não forneça diagnósticos médicos.
- Explique termos técnicos de forma simples.
- Utilize linguagem clara e amigável.
- Sempre informe que as respostas possuem caráter informativo.
```

---

# 10. Agente Especialista

O agente possui como responsabilidades:

* Interpretar ancestralidade.
* Explicar predisposições genéticas.
* Traduzir termos técnicos.
* Esclarecer dúvidas do usuário.
* Apresentar respostas compreensíveis.

---

# 11. Interface de Chat

A solução propõe uma interface simples desenvolvida em Streamlit.

## Funcionalidades

* Upload de relatório.
* Campo para perguntas.
* Respostas em tempo real.
* Exibição das fontes utilizadas.
* Histórico de interação.

---

# 12. Governança e Segurança

Devido à natureza sensível dos dados genéticos, foram definidos limites claros para atuação do agente.

## O agente NÃO pode:

* Emitir diagnósticos médicos.
* Prescrever medicamentos.
* Substituir profissionais de saúde.
* Inventar informações não presentes no relatório.
* Responder fora do contexto dos dados fornecidos.

## Estratégias de Controle

* Prompt Engineering.
* Busca baseada em RAG.
* Limitação de contexto.
* Restrições de comportamento do modelo.

---

# 13. Disclaimer

As respostas fornecidas pelo sistema possuem caráter exclusivamente informativo e educacional.

O agente não realiza diagnósticos médicos e não substitui a consulta com profissionais da área da saúde.

---

# 14. Exemplo de Dados Utilizados

```json
{
  "nome": "Paciente Exemplo",
  "ancestralidade": {
    "asiatica": 45,
    "europeia": 35,
    "africana": 20
  },
  "saude": [
    {
      "condicao": "Intolerância à lactose",
      "risco": "moderado"
    }
  ]
}
```

---

# 15. Exemplos de Perguntas

* Qual é minha ancestralidade?
* Tenho predisposição à intolerância à lactose?
* Quais riscos genéticos foram identificados?
* O que significa predisposição moderada?
* Existem recomendações relacionadas ao meu perfil genético?

---

# 16. Estrutura do Projeto

```text
challenge-dasa-sprint2
│
├── README.md
│
├── backend/
│
├── frontend/
│
├── data/
│   └── relatorio_exemplo.json
│
└── docs/
    ├── arquitetura.md
    └── governanca.md
```

---

# 17. Resultados Esperados

A solução proposta permite que pacientes compreendam seus relatórios genéticos de maneira mais acessível, reduzindo barreiras técnicas e facilitando o entendimento das informações fornecidas pelo exame.

Além disso, o uso de IA Generativa aliado à arquitetura RAG contribui para respostas mais confiáveis, transparentes e alinhadas aos princípios de segurança exigidos no contexto da saúde.

---

# 18. Conclusão

A Sprint 2 representa a evolução do sistema para uma plataforma inteligente de interpretação genética.

A utilização de NLP, Embeddings, Busca Semântica e IA Generativa possibilita uma experiência mais intuitiva para o usuário final, mantendo rastreabilidade das informações e respeitando limites éticos e médicos.

A solução proposta demonstra o potencial da Inteligência Artificial para democratizar o acesso ao conhecimento genético de forma segura e responsável.
