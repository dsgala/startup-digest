# Claude Haiku pricing (as of 2025)
INPUT_COST_PER_MILLION = 0.80   # $0.80 per 1M input tokens
OUTPUT_COST_PER_MILLION = 4.00  # $4.00 per 1M output tokens

def calculate_cost(input_tokens: int, output_tokens: int) -> float:
    input_cost = (input_tokens / 1_000_000) * INPUT_COST_PER_MILLION
    output_cost = (output_tokens / 1_000_000) * OUTPUT_COST_PER_MILLION
    return input_cost + output_cost

def print_cost_report(usage_log: list):
    print("\n" + "="*50)
    print("💰 COST REPORT")
    print("="*50)
    
    total_input = sum(u["input_tokens"] for u in usage_log)
    total_output = sum(u["output_tokens"] for u in usage_log)
    total_cost = calculate_cost(total_input, total_output)
    
    for u in usage_log:
        agent_cost = calculate_cost(u["input_tokens"], u["output_tokens"])
        print(f"{u['agent']:<25} in={u['input_tokens']:>6} out={u['output_tokens']:>6} cost=${agent_cost:.5f}")
    
    print("-"*50)
    print(f"{'TOTAL':<25} in={total_input:>6} out={total_output:>6} cost=${total_cost:.5f}")
    print(f"\nDaily cost:   ${total_cost:.4f}")
    print(f"Monthly cost: ${total_cost * 30:.4f}")
    print(f"Yearly cost:  ${total_cost * 365:.4f}")
    print("="*50)