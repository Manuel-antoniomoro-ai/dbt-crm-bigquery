#!/usr/bin/env python3
"""
Script para crear repositorio dbt-crm-bigquery en GitHub
Uso: python3 create_repo.py
"""

import os
import subprocess
import json
from pathlib import Path

def run_command(cmd):
    """Ejecuta comando en terminal"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return False
    print(f"✅ {result.stdout}")
    return True

def create_project_structure():
    """Crea estructura de carpetas"""
    folders = [
        "docs",
        "sql_scripts",
        "dbt_project/models/staging",
        "dbt_project/models/intermediate",
        "dbt_project/models/marts"
    ]
    
    for folder in folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"✅ Carpeta creada: {folder}")

def create_files():
    """Crea todos los archivos"""
    
    files = {
        # Archivos raíz
        "README.md": """# 🏢 dbt + BigQuery - Modelo CRM Estándar Completo

![dbt](https://img.shields.io/badge/dbt-1.7+-green)
![BigQuery](https://img.shields.io/badge/BigQuery-Analytics-blue)

**Modelo CRM profesional con dbt + BigQuery + datos ficticios**

## 🎯 Contenido
- 3 documentos completos
- 14 modelos dbt
- 50+ datos ficticios
- Tests automáticos
- Queries de ejemplo

## 🚀 Quick Start
```bash
git clone https://github.com/Manuel-antoniomoro-ai/dbt-crm-bigquery
cd dbt-crm-bigquery
cat QUICK_START.md
