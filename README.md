Seminario - Tecnologo
Proyecto: Seminario Tecnologo - Grupo Marcela, Ronald, Juan

Integrantes del Grupo
Marcela	
Ronald	
Juan	
Laboratorio 1 — Arquitectura As-Is
1. URL del Codespace (API Activa)
Haz clic abajo para ver la documentación interactiva (Swagger UI):https://silver-system-q7r9p9w5v46396wx-8000.app.github.dev/docs

2. Diagrama Arquitectónico (Imagen)
docs/diagramas/Arquitectura_As_Is_Lab1.PNG

3. Código del Diagrama (Interactivo)
graph TD    %% Arquitectura As-Is — API Riesgo Crediticio        Cliente(["👤 Cliente FinTech Nova<br/>(App Móvil)"]):::actor    subgraph Internet["🌐 INTERNET"]    HTTPS["HTTPS / TLS 1.3"]    end    subgraph Codespaces["☁️ GitHub Codespaces | Azure"]    subgraph Container["📦 Contenedor Linux"]    subgraph FastAPI["⚙️ FastAPI | Puerto 8000"]    EP1["POST /evaluar-riesgo"]:::safe    EP2["GET /status"]:::monitor    EP3["GET /datos-financieros/{id}<br/>⚠️ VULNERABLE"]:::vuln    end    end    end    Cliente --> HTTPS --> FastAPI    FastAPI --> EP1 & EP2 & EP3        classDef actor fill:#EBF5FB,stroke:#1A5C9A,stroke-width:2px    classDef safe fill:#C8DDEF,stroke:#1A5C9A,stroke-width:2px    classDef monitor fill:#D5F5E3,stroke:#1E8449,stroke-width:2px    classDef vuln fill:#FADBD8,stroke:#C0392B,stroke-width:4px