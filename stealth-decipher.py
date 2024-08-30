from scapy.all import rdpcap, ICMP
import string

def extract_icmp_data(pcap_file):
    packets = rdpcap(pcap_file)
    extracted_data = ""

    for packet in packets:
        if ICMP in packet and packet[ICMP].type == 8:  # Echo Request
            payload = bytes(packet[ICMP].payload)
            try:
                # Attempt to decode payload into a string
                extracted_data += payload.decode('utf-8')
            except UnicodeDecodeError:
                # Handle cases where the payload isn't valid UTF-8
                continue

    return extracted_data

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char

    return decrypted_text

def analyze_text(text):
    # A simple heuristic to determine the most likely correct string.
    # The correct string is expected to have the most valid English words.
    common_words = set(["the", "be", "to", "of", "and", "a", "in", "that", "it", "is", "was", "he", "for", "on", "are", "as", "with", "his", "they", "I"])
    words = text.split()
    common_word_count = sum(1 for word in words if word.lower() in common_words)
    return common_word_count

def main():
    # User input for the .pcap file
    pcap_file = input("/workspaces/Laboratorios_cripto/parte2.pcapng")

    # Extract data from the ICMP packets
    extracted_string = extract_icmp_data(pcap_file)

    # Attempt all 26 Caesar cipher shifts and evaluate the results
    possible_decryptions = []
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(extracted_string, shift)
        common_word_count = analyze_text(decrypted_text)
        possible_decryptions.append((decrypted_text, common_word_count))

    # Determine the most likely correct decryption
    most_likely_decryption = max(possible_decryptions, key=lambda item: item[1])

    # Display the results
    print("\nExtracted String:")
    print(extracted_string)
    print("\nMost Likely Decrypted Message:")
    print(most_likely_decryption[0])

    print("\nAll Possible Decryptions:")
    for shift, (decrypted_text, _) in enumerate(possible_decryptions):
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    main()
