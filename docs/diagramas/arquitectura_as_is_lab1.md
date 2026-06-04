graph TD
    %% ========================================================
    %% TITULO DEL DIAGRAMA
    %% Arquitectura As-Is — API Riesgo Crediticio — FinTech Nova
    %% Laboratorio 1 — Roslaysoft Consulting
    %% ========================================================

    %% ── ACTOR EXTERNO ─────────────────────────────────────
    Cliente(["👤 Cliente FinTech Nova<br/>(App Móvil / Web Browser)"]):::actor

    %% ── ZONA INTERNET ─────────────────────────────────────
    subgraph Internet["🌐 INTERNET / Red Pública"]
    Canal["HTTPS / TLS 1.3<br/>Puerto público (443)"]
    end

    %% ── GITHUB CODESPACES ─────────────────────────────────
    subgraph Codespaces["☁️ GitHub Codespaces | Microsoft Azure"]

    subgraph Contenedor["📦 Contenedor Linux Efímero | VS Code Server"]

    subgraph FastAPI["⚙️ FastAPI Application | uvicorn | Puerto 8000"]
    EP1["POST /evaluar-riesgo<br/>Scoring Crediticio"]:::endpoint_safe
    EP2["GET /status<br/>Health Check"]:::endpoint_monitor
    EP3["GET /datos-financieros/{id}<br/>⚠️ VULNERABLE — Sin Autenticación"]:::endpoint_vuln
    end

    end
    end

    %% ── CONEXIONES / FLUJOS ───────────────────────────────
    Cliente -->|"HTTPS Request<br/>JSON Payload"| Canal
    Canal -->|"HTTP interno<br/>Puerto 8000"| FastAPI
    FastAPI -->|"Procesa request"| EP1
    FastAPI -->|"Procesa request"| EP2
    FastAPI -->|"Procesa request"| EP3

    EP1 -.->|"JSON Response<br/>{resultado: Aprobado/Rechazado}"| Cliente
    EP2 -.->|"JSON Response<br/>{status: healthy}"| Cliente
    EP3 -.->|"JSON Response<br/>⚠️ Historial sin restricción"| Cliente

    %% ── ESTILOS / LEYENDA ─────────────────────────────────
    classDef actor fill:#EBF5FB,stroke:#1A5C9A,stroke-width:2px,color:#0D2B55
    classDef endpoint_safe fill:#C8DDEF,stroke:#1A5C9A,stroke-width:2px,color:#0D2B55
    classDef endpoint_monitor fill:#D5F5E3,stroke:#1E8449,stroke-width:2px,color:#1E8449
    classDef endpoint_vuln fill:#FADBD8,stroke:#C0392B,stroke-width:4px,color:#C0392B