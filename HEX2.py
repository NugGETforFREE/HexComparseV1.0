
import argparse

def hex_to_dec(hex_str):
    return int(hex_str, 16) if hex_str else 0

def hex_to_bin(hex_str):
    return bin(hex_to_dec(hex_str))[2:].zfill(8) if hex_str else '00000000'

def hex_to_int(hex_str):
    return int(hex_str, 16) if hex_str else 0

def compare_files(file1_path, file2_path, output_path):
    discrepancies = []

    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        offset = 0
        while True:
            byte1 = file1.read(1)
            byte2 = file2.read(1)

            if not byte1 and not byte2:  # Оба файла закончились
                break

            hex1 = byte1.hex() if byte1 else ''
            hex2 = byte2.hex() if byte2 else '00'  # Если byte2 пуст, используем '00'

            if byte1 != byte2:
                dec1 = hex_to_dec(hex1)
                dec2 = hex_to_dec(hex2)
                int1 = hex_to_int(hex1)
                int2 = hex_to_int(hex2)
                bin1 = hex_to_bin(hex1)
                bin2 = hex_to_bin(hex2)

                discrepancy = (
                    f"Offset: {offset:08x} | "
                    f"File1: HEX={hex1.upper()} | DEC={dec1} | INT={int1} | BIN={bin1} | "
                    f"File2: HEX={hex2.upper()} | DEC={dec2} | INT={int2} | BIN={bin2}"
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