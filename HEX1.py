import argparse

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def hex_to_bin(hex_str):
    return bin(hex_to_dec(hex_str))[2:]

def hex_to_int(hex_str):
    return int(hex_str, 16)

def signed_hex_to_int(hex_str):
    value = hex_to_int(hex_str)
    if value >= (1 << 31):
        value -= (1 << 32)
    return value

def compare_files(file1_path, file2_path, output_path):
    discrepancies = []

    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        offset = 0
        while True:
            byte1 = file1.read(1)
            byte2 = file2.read(1)
            if not byte1 and not byte2:
                break

            if byte1 != byte2:
                hex1 = byte1.hex()
                hex2 = byte2.hex() if byte2 else '00' 
                
                discrepancy = (
                    f"Offset: {offset:08x} | "
                    f"File1: {hex1.upper()} | "
                    f"File2: {hex2.upper()}"
                )
                discrepancies.append(discrepancy)
            
            offset += 1

    if discrepancies:
        print("Discrepancies found:")
        for line in discrepancies:
            print(line)

        with open(output_path, 'w') as output_file:
            for line in discrepancies:
                output_file.write(line + "\n")
        print(f"\nDiscrepancies written to file: {output_path}")
    else:
        print("No discrepancies found.")

def main():
    parser = argparse.ArgumentParser(description="Compare two files byte by byte.")
    parser.add_argument("file1", help="Path to the first file")
    parser.add_argument("file2", help="Path to the second file")
    parser.add_argument("output", help="Path to the output file for discrepancies")

    args = parser.parse_args()

    compare_files(args.file1, args.file2, args.output)

if __name__ == "__main__":
    main()