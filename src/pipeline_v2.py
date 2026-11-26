# VERSION 2.0 (GREEN ENVIRONMENT) - Add !0% loyalty discount calculation

def run_pipeline():
  print("[GREEN - v2.0] Running enhanced retail sales calculation with discount ...")
  sales = [100, 200, 300]
  total = sum(sales)
  discounted_total = total * 0.90
  print(f"[GREEN - v2.0] Total sales after 10% discount: {discounted_total}")
  return {"version": "2.0", "environment": "green", "total_sales": discounted_total}

if __name__ == "main":
  run_pipeline()
