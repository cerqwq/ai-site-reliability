"""
AI Site Reliability - AI站点可靠性工具
支持SRE实践、故障管理、容量规划
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AISiteReliabilityTools:
    """
    AI站点可靠性工具
    支持：SRE、故障、容量
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_sre_practices(self, organization: str) -> Dict:
        """设计SRE实践"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{organization}设计SRE实践：

请返回JSON格式：
{{
    "principles": ["原则"],
    "processes": ["流程"],
    "tools": ["工具"],
    "metrics": ["指标"],
    "team_structure": "团队结构"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"sre": content}

    def generate_incident_management(self, severity_levels: List[str]) -> Dict:
        """生成事故管理流程"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        levels_text = ", ".join(severity_levels)

        prompt = f"""请生成事故管理流程：

严重级别：{levels_text}

请返回JSON格式：
{{
    "detection": "检测流程",
    "response": "响应流程",
    "communication": "沟通流程",
    "resolution": "解决流程",
    "postmortem": "事后分析流程"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"incident_management": content}

    def design_capacity_plan(self, service: str, growth_forecast: Dict) -> Dict:
        """设计容量规划"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        forecast_text = json.dumps(growth_forecast, ensure_ascii=False)

        prompt = f"""请为{service}设计容量规划：

增长预测：{forecast_text}

请返回JSON格式：
{{
    "current_capacity": "当前容量",
    "projected_needs": "预测需求",
    "scaling_strategy": "扩展策略",
    "cost_estimate": "成本估算",
    "timeline": "时间计划"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"capacity": content}

    def generate_runbook(self, service: str, scenarios: List[str]) -> str:
        """生成运维手册"""
        if not self.client:
            return "LLM客户端未配置"

        scenarios_text = "\n".join(f"- {s}" for s in scenarios)

        prompt = f"""请为{service}生成运维手册：

场景：
{scenarios_text}

要求：
1. 健康检查
2. 故障排查
3. 扩缩容
4. 回滚操作"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_error_budget(self, slos: List[Dict], actual_performance: Dict) -> Dict:
        """分析错误预算"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        slos_text = json.dumps(slos, ensure_ascii=False)
        perf_text = json.dumps(actual_performance, ensure_ascii=False)

        prompt = f"""请分析错误预算：

SLO：{slos_text}
实际表现：{perf_text}

请返回JSON格式：
{{
    "budget_status": "预算状态",
    "remaining": "剩余预算",
    "burn_rate": "消耗速率",
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"error_budget": content}

    def design_blameless_postmortem(self, incident: Dict) -> str:
        """设计无责事后分析"""
        if not self.client:
            return "LLM客户端未配置"

        incident_text = json.dumps(incident, ensure_ascii=False)

        prompt = f"""请根据以下事故设计无责事后分析：

{incident_text}

要求：
1. 时间线
2. 根因分析
3. 影响评估
4. 行动项
5. 经验教训"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AISiteReliabilityTools:
    """创建站点可靠性工具"""
    return AISiteReliabilityTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Site Reliability Tools")
    print()

    # 测试
    sre = tools.design_sre_practices("科技公司")
    print(json.dumps(sre, ensure_ascii=False, indent=2))
