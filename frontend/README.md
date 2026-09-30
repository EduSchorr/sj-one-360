# Relatório Geral em React

Migração gradual do SJ One 360 para React. O backend FastAPI, a autenticação,
as permissões, as integrações e as operações de escrita continuam no servidor.

## Desenvolvimento e atualização

Requer Node.js 20.19+ ou 22.12+ para Vite 7. No diretório `frontend`:

```bash
npm ci
npm run build
```

O build gera `static/react-report/app.js`, `app.css`, `home.js`, `home.css` e o código compartilhado em `assets/`. Esses arquivos já vêm compilados no ZIP de atualização; a instalação normal não precisa de Node.js. Inclua o código fonte, `package-lock.json` e os arquivos compilados no pacote, sem `node_modules`.

Rota React: `/relatorio-geral/novo`. Rota legada: `/relatorio-geral`.
Visão Geral React principal: `/central`. Tela anterior: `/central/classico`.
O endereço `/central/novo` permanece como alias para favoritos antigos.
API autenticada da Visão Geral: `/api/v2/central`; comparação financeira: `/api/v2/central/comparar`.
API autenticada: `/api/v2/relatorio-geral`, protegida por `reports_export`.
A comparação por bloco consulta `/api/v2/relatorio-geral/comparar?channel=...&date_from=...&date_to=...`,
com a mesma permissão; a resposta inclui apenas métricas agregadas do período B.
A API usa uma lista positiva de indicadores agregados; nunca incluir tickets,
mensagens, anexos, cookies de sessão ou detalhes pessoais na resposta.

Para atualizar o frontend, altere os arquivos em `src/` e execute o build,
atualize a versão e os parâmetros de cache do template correspondente.
Valide os dois temas e o fluxo de filtros.
