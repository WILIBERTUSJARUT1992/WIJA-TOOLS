import itertools
import string
import time

class BruteForcePassword:
    """
    Brute Force Password Cracker
    Mencoba kombinasi password untuk login
    """
    
    def __init__(self, target_password, charset=None):
        """
        Inisialisasi Brute Force Password Cracker
        
        Args:
            target_password (str): Password target yang ingin di-crack
            charset (str): Karakter yang digunakan untuk kombinasi
                          Default: huruf kecil + huruf besar + angka + simbol
        """
        self.target_password = target_password
        self.charset = charset or (string.ascii_lowercase + string.ascii_uppercase + 
                                   string.digits + string.punctuation)
        self.attempts = 0
        self.found = False
        self.time_taken = 0
        
    def crack(self, max_length=None):
        """
        Crack password dengan brute force
        
        Args:
            max_length (int): Panjang maksimal password yang dicoba
                             Default: panjang target_password
        """
        if max_length is None:
            max_length = len(self.target_password)
        
        start_time = time.time()
        print(f"[*] Target Password: {self.target_password}")
        print(f"[*] Panjang Password: {len(self.target_password)}")
        print(f"[*] Karakter Set: {len(self.charset)} karakter")
        print(f"[*] Mulai Cracking...\n")
        
        try:
            for length in range(1, max_length + 1):
                print(f"[*] Mencoba password dengan panjang: {length}")
                
                for password_tuple in itertools.product(self.charset, repeat=length):
                    password_guess = ''.join(password_tuple)
                    self.attempts += 1
                    
                    if self.attempts % 10000 == 0:
                        print(f"    Percobaan: {self.attempts} | Last guess: {password_guess}")
                    
                    if password_guess == self.target_password:
                        self.found = True
                        self.time_taken = time.time() - start_time
                        print(f"\n[✓] PASSWORD DITEMUKAN: {password_guess}")
                        print(f"[✓] Total Percobaan: {self.attempts}")
                        print(f"[✓] Waktu: {self.time_taken:.2f} detik")
                        return password_guess
                
        except KeyboardInterrupt:
            print("\n[!] Proses dihentikan oleh user")
            self.time_taken = time.time() - start_time
            
        if not self.found:
            self.time_taken = time.time() - start_time
            print(f"\n[✗] Password tidak ditemukan setelah {self.attempts} percobaan")
            print(f"[✗] Waktu: {self.time_taken:.2f} detik")
            
        return None
    
    def crack_with_wordlist(self, wordlist_file):
        """
        Crack password menggunakan wordlist
        
        Args:
            wordlist_file (str): Path ke file wordlist
        """
        start_time = time.time()
        print(f"[*] Target Password: {self.target_password}")
        print(f"[*] Membuka Wordlist: {wordlist_file}\n")
        
        try:
            with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    password_guess = line.strip()
                    self.attempts += 1
                    
                    if self.attempts % 1000 == 0:
                        print(f"[*] Percobaan: {self.attempts} | Last guess: {password_guess}")
                    
                    if password_guess == self.target_password:
                        self.found = True
                        self.time_taken = time.time() - start_time
                        print(f"\n[✓] PASSWORD DITEMUKAN: {password_guess}")
                        print(f"[✓] Total Percobaan: {self.attempts}")
                        print(f"[✓] Waktu: {self.time_taken:.2f} detik")
                        return password_guess
                        
        except FileNotFoundError:
            print(f"[!] File tidak ditemukan: {wordlist_file}")
        except KeyboardInterrupt:
            print("\n[!] Proses dihentikan oleh user")
            
        self.time_taken = time.time() - start_time
        if not self.found:
            print(f"\n[✗] Password tidak ditemukan setelah {self.attempts} percobaan")
            print(f"[✗] Waktu: {self.time_taken:.2f} detik")
            
        return None


def main():
    """Main function untuk testing"""
    print("=" * 50)
    print("BRUTE FORCE PASSWORD CRACKER")
    print("=" * 50 + "\n")
    
    print("[CONTOH 1] Brute Force Sederhana")
    print("-" * 50)
    cracker = BruteForcePassword("abc")
    
    print("\n[CONTOH 2] Brute Force dengan Wordlist")
    print("-" * 50)


if __name__ == "__main__":
    main()