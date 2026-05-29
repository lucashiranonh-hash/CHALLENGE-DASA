# Arquitetura da Solução

## Fluxo Geral

PDF → JSON → Embeddings → Base Vetorial → Busca Semântica → LLM → Resposta

### Componentes

* JSON estruturado contendo os dados genéticos.
* Embeddings para representação vetorial.
* FAISS como banco vetorial.
* Busca semântica para recuperação de contexto.
* Modelo de linguagem para geração das respostas.

## Estratégia RAG

A arquitetura Retrieval-Augmented Generation (RAG) foi escolhida para reduzir alucinações e garantir que as respostas sejam fundamentadas nos dados do relatório.

O sistema recupera os trechos mais relevantes antes de gerar uma resposta.
