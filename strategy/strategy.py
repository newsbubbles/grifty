"""
strategy.py

Contains functions for defining company vision, strategic goals, and market analysis.
"""

from grifty.ceo_agent import run_llm

class Strategy:
    def define_long_term_vision(self, vision_statement: str, time_frame: str) -> str:
        prompt = f"Define a comprehensive long-term vision statement for '{vision_statement}' over {time_frame}."
        return run_llm(prompt)

    def develop_strategic_goals(self, time_frame: str) -> str:
        prompt = f"Propose strategic goals for the next {time_frame} in the context of our business."
        return run_llm(prompt)

    def perform_market_analysis(self, industry: str) -> str:
        prompt = f"Perform a detailed market analysis for the {industry} industry."
        return run_llm(prompt)

    def create_roadmap(self, goals: str) -> str:
        prompt = f"Create a high-level roadmap for achieving these strategic goals: {goals}"
        return run_llm(prompt)
