import re
def password_strength(password):
   score = 0
   
   
   if len(password) >= 8:
      score += 1
   if re.search("[A-Z]" , password):
      score += 1
   if re.search("[a-z]" , password):
      score += 1
   if re.search("[0-9]" , password):
      score += 1
   if re.search ("[!@#$%^&*()_+]" , password):
      score += 1
    

   if score == 5:
      return "Strong 💪"
   elif score >= 3:
      return "Medium ⚠️"
   else:
        return "Weak ❌"


password = input("Enter your password: ")


if len(password) < 8:
    print("Tip: Use at least 8 characters")

print("Password strength:", password_strength(password))
