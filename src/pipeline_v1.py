# Version 1.0 (BLUE Environment)
def run_pipeline():
  print("[BLUE - v1.0] Running standard retail sales calculation...")
  sales = [100, 200, 300]
  total = sum(sales)
  print(f"[BLUE - v1.0] Total Sales: {total}")
  return {"version": "1.0", "environment": "blue", "total_sales": total}

if __name__ == "main":
  run_pipeline()
