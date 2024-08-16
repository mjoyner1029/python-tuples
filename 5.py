def merge_catalogs(*catalogs):
    combined_catalog = []
    for catalog in catalogs:
        combined_catalog.extend(catalog)  # Use extend to add elements from each catalog
    return combined_catalog

# Sample catalogs for demonstration
catalog1 = [("Laptop", 999), ("Smartphone", 599)]
catalog2 = [("Headphones", 199), ("Keyboard", 89)]
catalog3 = [("Mouse", 49), ("Monitor", 299)]

# Merge catalogs
combined_catalog = merge_catalogs(catalog1, catalog2, catalog3)

print("Combined Catalog:")

for product in combined_catalog:
    print(product[0], "-", "$" + str(product[1]))
