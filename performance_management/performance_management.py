"""
performance_management.py

Sets and tracks KPIs, monitors progress, and generates performance summaries.
"""

from grifty.ceo_agent import run_llm

class PerformanceManagement:
    def define_kpis(self, team: str, goals: str) -> str:
        prompt = f"Suggest appropriate KPIs for team {team} based on goals: {goals}"
        return run_llm(prompt)

    def track_kpis(self, kpi_data: dict, timeframe: str) -> str:
        prompt = f"Analyze KPI data for {timeframe}: {kpi_data}"
        return run_llm(prompt)

    def report_performance_summary(self) -> str:
        prompt = "Generate a high-level performance summary for the current reporting period."
        return run_llm(prompt)
