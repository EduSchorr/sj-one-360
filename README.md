<div align="center">

# SJ One 360

### Operations · Customer Service · Automation · Analytics

**A full-stack operational platform designed to centralize customer-service workflows, internal queues, analytics and business automation.**

![Python](https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=3776AB)
![FastAPI](https://img.shields.io/badge/FastAPI-20232A?style=for-the-badge&logo=fastapi&logoColor=009688)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-20232A?style=for-the-badge&logo=typescript&logoColor=3178C6)
![SQLite](https://img.shields.io/badge/SQLite-20232A?style=for-the-badge&logo=sqlite&logoColor=003B57)

</div>

---

## Why this project exists

SJ One 360 started from a recurring operational problem: customer-service information was spread across different channels, manual controls and disconnected workflows. The goal was to turn those moving parts into one cohesive workspace.

The platform combines queue management, operational records, role-based access, dashboards, automation, financial workflows, reporting and AI-assisted tooling in a single application.

> This repository is a **sanitized portfolio edition**. Real customer data, employee information, credentials, internal network addresses, production databases and private company configuration are intentionally excluded or replaced with synthetic examples.

## Highlights

- Role-based operational workspace for agents, administrators and management
- Customer-service queue and case lifecycle management
- N1 → N2 escalation and return workflows
- Operational dashboards and period comparison
- Financial validation and refund/cancellation workflows
- Reporting and Excel/CSV-oriented exports
- Schedule-aware assignment and redistribution
- Notifications, audit trails and access management
- React + TypeScript interfaces integrated with the Python application
- AI/Copilot workspace architecture
- Backup, update and recovery tooling for local deployments
- Connectors for external operational channels, isolated from secrets/configuration

## Architecture

```text
┌──────────────────────────────────────────────┐
│                 React / Vite                 │
│ dashboards · reports · copilot · workspace  │
└──────────────────────┬───────────────────────┘
                       │
┌──────────────────────▼───────────────────────┐
│              Python / FastAPI                │
│ auth · workflows · reports · automation     │
└───────────────┬───────────────┬──────────────┘
                │               │
        ┌───────▼───────┐ ┌────▼────────────────┐
        │    SQLite     │ │ Optional Integrations│
        │ audit + data  │ │ Outlook / APIs / BI  │
        └───────────────┘ └──────────────────────┘
```

## Repository structure

```text
copilot/        AI-assisted workspace and provider abstraction
frontend/       React + TypeScript source
static/         Legacy/static UI layers and assets
templates/      Server-rendered operational screens
docs/           Technical documentation
server.py       FastAPI application and routes
database.py     SQLite schema, migrations and demo seed data
*_service.py    Domain-oriented business services
*_collector.py  Optional integration collectors
```

## Local setup

### Requirements

- Python 3.11+
- Node.js 20+ for rebuilding the React frontend
- Windows for integrations that depend on Outlook/Windows APIs

### Backend

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
copy config.env.example config.env
```

The production version uses an explicit startup authorization flow. For a portfolio/demo environment, review the startup-security settings before running the server.

### Frontend

```bash
cd frontend
npm install
npm run build
```

## Security & privacy

The public edition deliberately excludes:

- production databases and backups
- real customer or employee records
- corporate e-mail addresses
- credentials, tokens and API secrets
- private network endpoints
- internal security documentation
- production-specific configuration

Use `config.env.example` as the configuration template and never commit a populated `config.env`.

## Status

The original application is an actively evolved operational system. This repository is maintained as a portfolio-safe representation of its architecture and engineering work.

---

<div align="center">

Built by **Eduardo Lima** · [GitHub](https://github.com/EduSchorr)

</div>