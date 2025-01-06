"""
fundraising.py

Handles the intricacies of raising capital, from evaluating funding options to negotiating terms.
"""

from grifty.ceo_agent import run_llm

class Fundraising:
    def evaluate_funding_options(self, current_financial_status: dict, growth_plan: dict) -> str:
        prompt = f"Suggest the best funding approach given {current_financial_status} and {growth_plan}"
        return run_llm(prompt)

    def negotiate_terms(self, funding_source: str, desired_investment: float) -> str:
        prompt = f"Draft negotiation points for {funding_source} seeking an investment of {desired_investment}."
        return run_llm(prompt)

    def manage_cap_table(self, cap_table_state: dict, new_investment_terms: dict) -> dict:
        # Placeholder logic
        updated = {**cap_table_state, **new_investment_terms}
        return updated
