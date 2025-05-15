import json
import sys

def load_questions(path="questions.json"):
	try:
		with open(path,"r") as f:
			return json.load(f)
	except FileNotFoundError:
		print(f"Error: Couldn't find {path}")
		sys.exit(0)
	except json.JSONDecodeError:
		print(f"Error: Invalid JSON in {path}")
		sys.exit(0)

def ask_questions(questions):
	score = 0
	for idx,q in enumerate(questions,start=1):
		print(f"\nQ{idx}: {q['question']}")
		for opt in q["options"]:
			print(f"	{opt}")
		answer = input("Your answer (A/B/C/D): ").strip().upper()
		if answer == q["answer"]:
			print("Correct!")
			score += 1
		else:
			print(f"Wrong! The correct answer aws {q['answer']}.")
	return score

def main():
	print("Welcome to the CLI Quiz App!")
	print("Welcome to the CLI Quiz App!")
	input("Press Enter to start the quiz...")
	questions = load_questions()
	total = len(questions)
	score = ask_questions(questions)
	print(f"\nYou scored {score}/{total}.")

if __name__ == "__main__":
	main()
