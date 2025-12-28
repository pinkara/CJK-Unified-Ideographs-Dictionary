import data_processor

print("--- Testing data_processor.py ---")
cjk_data = data_processor.get_cjk_data()

if cjk_data:
    print(f"Successfully retrieved {len(cjk_data)} CJK characters from data_processor.py.")
    print("First 5 entries:")
    for i in range(min(5, len(cjk_data))):
        print(cjk_data[i])
else:
    print("Failed to retrieve CJK data.")

# KANGXI_RADICALS is also moved, just print its length to verify
print(f"KANGXI_RADICALS list length: {len(data_processor.KANGXI_RADICALS)}")
