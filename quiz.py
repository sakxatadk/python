questions = [
    ["What is the captial city of China ","Kathmandu","Beijing","London","Tokyo",2],
    ["What is the largest planet in our solar system?","Earth","Mars","Jupiter","Saturn",3],
    ["Who wrote 'Romeo and Juliet'?","Mark Twain","William Shakespeare","Charles Dickens","Jane Austen",2],
    ["What is the chemical symbol for water?","H2O","CO2","NaCl","O2",1],
    ["What year did the Titanic sink?","1912","1905","1898","1920",1],
    ["What is the smallest prime number?","0","1","2","3",3],
    ["What is the hardest natural substance on Earth?","Gold","Iron","Diamond","Silver",3],
    ["Who painted the Mona Lisa?","Vincent van Gogh","Pablo Picasso","Leonardo da Vinci","Claude Monet",3],
    ["What is the largest mammal in the world?","Elephant","Blue Whale","Giraffe","Hippopotamus",2],
    ["What is the main ingredient in guacamole?","Tomato","Avocado","Onion","Pepper",2],     
]
levels = [1000 ,2000,3000,4000,5000,10000,20000,40000,80000,100000]

for i in range(len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}:")
    print(question[0])
    print(f" A. {question[1]}                        B. {question[2]}")
    print(f" C. {question[3]}                        D. {question[4]}")
    reply = int(input("Enter your option (1-4): "))
    if reply == question[-1]:
        print(f"Congratulations! You have won Rs.{levels[i]}\n")
    else:
        print("Sorry, that's incorrect. Better luck next time!")
        break
 