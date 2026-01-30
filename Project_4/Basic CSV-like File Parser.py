# 1. Define the filename
DATA_FILE = "products.csv"

def parse_product_data(filename):
    product_list = []
    
    try:
        with open(filename, 'r') as file:
            header = file.readline()
            
            for line in file:
                try:
                    parts = line.strip().split(',')
                    
                    if len(parts) != 3:
                        print(f"Warning: Skipping malformed line: {line.strip()}")
                        continue
                    
                    name = parts[0]
                    price = float(parts[1])
                    quantity = int(parts[2])
                    
                    product_dict = {
                        "Product": name, 
                        "Price": price, 
                        "Quantity": quantity
                    }
                    product_list.append(product_dict)
                    
                except ValueError:
                    print(f"Warning: Skipping invalid data row: {line.strip()}")
        
        return product_list

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def main():
    product_data = parse_product_data(DATA_FILE)
    
    if product_data:
        print("\n--- Product Inventory Report ---")
    
        print(f"{'Product':<10} | {'Price':<10} | {'Qty':<8} | {'Value':<10}")
        print("-" * 45)
        
        total_inventory_value = 0
        
        for item in product_data:
            item_total = item["Price"] * item["Quantity"]
            total_inventory_value += item_total
            
            print(f"{item['Product']:<10} | ${item['Price']:>8.2f} | {item['Quantity']:^8} | ${item_total:>9.2f}")
        
        print("-" * 45)
        print(f"Total Inventory Value: ${total_inventory_value:,.2f}")
    else:
        print("No valid data to display.")

if __name__ == "__main__":
    main()