# 🏗️ AI Site Reliability

AI站点可靠性工具，支持SRE实践、故障管理、容量规划。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ SRE实践设计
- 🚨 事故管理流程
- 📊 容量规划
- 📖 运维手册生成
- 📏 错误预算分析
- 📝 无责事后分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_site_reliability import create_tools

tools = create_tools()

# SRE实践
sre = tools.design_sre_practices("科技公司")

# 事故管理
incident = tools.generate_incident_management(["P0", "P1", "P2", "P3"])

# 容量规划
capacity = tools.design_capacity_plan("API服务", growth_forecast)

# 运维手册
runbook = tools.generate_runbook("API服务", scenarios)

# 错误预算
budget = tools.analyze_error_budget(slos, actual_performance)

# 事后分析
postmortem = tools.design_blameless_postmortem(incident)
```

## 📁 项目结构

```
ai-site-reliability/
├── tools.py       # 站点可靠性工具核心
└── README.md
```

## 📄 许可证

MIT License
