# 🔐 CipherCLI – A Command-Line Caesar Cipher Tool  

CipherCLI is a **simple yet powerful command-line tool** that allows users to **encrypt and decrypt messages** using the **Caesar Cipher algorithm**. With a user-friendly interface and interactive prompts, this tool makes encryption and decryption effortless. 
### (working)
![image (4)](https://github.com/user-attachments/assets/fdfbcbf5-fa16-4b56-915e-94ae10e17bfe)

---

## 🛠️ Installation  
Before using CipherCLI, you need to install **Python (3.x recommended)** and the required dependencies.  

### **1️⃣ Install Python (if not already installed)**  
Check if Python is installed:  
```sh
python --version
sudo git clone https://github.com/Ajay-Bommidi/CipherCLI.git
```
If not installed, download it from [python.org](https://www.python.org/downloads/).  

### **2️⃣ Install Dependencies**  
CipherCLI uses `colorama` for CLI color enhancements. Install it using:  
```sh
cd CipherCLI
sudo python3 -m venv myenv
source myenv/bin/activate
sudo chown -R $USER:$USER /home/kali/CipherCLI/myenv/
pip install colorama

```
or 
```
cd CipherCLI
sudo python3 -m venv myenv
source myenv/bin/activate
sudo chown -R $USER:$USER /home/kali/CipherCLI/myenv/
pip install -r requirements.txt
```
---

## 🚀 Usage  

### **Run the script**  
Save the script as `CipherCLI.py` and execute it from the terminal: for (Windows) 
```sh
python CipherCLI.py
```

### **🔹 Encrypt a Message**  
1. Choose `e` for encryption.  
2. Enter your message (e.g., `"Hello, World!"`).  
3. Input a shift value (1-25).  
4. The encrypted result will be displayed.  

**Example:**  
Enter your choice (e/d): e
Enter your message: Hello, World!
Enter shift value (1-25): 3
✅ Result: Khoor, Zruog!

### **🔹 Decrypt a Message**  
1. Choose `d` for decryption.  
2. Enter the encrypted text.  
3. Input the same shift value used for encryption.  
4. The decrypted message will be displayed.  

**Example:**  
Enter your choice (e/d): d
Enter your message: Khoor, Zruog!
Enter shift value (1-25): 3
✅ Result: Hello, World!
---

## 📌 How It Works  
CipherCLI uses the **Caesar Cipher** algorithm, a simple shift-based encryption method where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.  

Example with a shift of **3**:  
```
A → D, B → E, C → F, ..., X → A, Y → B, Z → C
``` 

---

## 💡 Contributing  
Contributions are welcome! Feel free to fork the repo, create new features, or report issues.  

---

## 📜 License  
This project is licensed under the **MIT License** – free to use, modify, and distribute.  

---

🎉 **Enjoy Encrypting & Decrypting with CipherCLI!** 🚀  

--- 
