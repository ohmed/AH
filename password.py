import re

def check_password_strength(password):
	length_error = len(password) < 8
	uppercase_error = not any(char.isupper() for char in password)
	lowercase_error = not any(char.islower() for char in password)
	digit_error = not any(char.isdigit() for char in password)


	errors = {
		"Too short (min 8 characters)": length_error,
		"Must contain at least one uppercase": uppercase_error,
		"Must contain at least one lowercase": lowercase_error,
		"Must contain at least one number": digit_error,
	}

	if any(errors.values()):
		print("Weak password! Issues:")
		for issue, exists in errors.items():
			if exists:
				print(f"- {issue}")
	
	else:
		print("Strong Password!")


if __name__ == "__main__":

	while True:
		user_password = input("Enter a password (or type 'exit' to quit): ")
		if user_password .lower() == 'exit':
			print("Exiting the script. ")
			break


		check_password_strength(user_password)