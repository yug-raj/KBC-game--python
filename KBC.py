q = [
    "who is the Fathere of Nation?", "you" , "me", "M.Gandhi" ,"none of these!" 4
]
 [
    "who is the Fathere of Computer?", "you" , "me", "Charles Babbage" ,"none of these!" 4
]
 [
    "who is the King of jungle?", "you" , "Lion", "me" ,"none of these!" 4
]
 [
    "what is the CAPITAL OF INDIA?", "US" , "New Delhi", "Manipur" ,"none of these!" 4
]
 [
    "what is the CAPITAL OF Bihar?", "Patna" , "Merut", "Assam" ,"none of these!" 4
]
 [
    "what is the Full Form of GK?", "Gyan Kumar" , "Gyan ka Bhandar", "General Knowledge" ,"none of these!" 4
]
 [
    "who is the 1st Precident of India?", "Rajendra Prasad" , "me", "M.Gandhi" ,"none of these!" 4
]
 [
    "who is the Fathere of Fruit?", "Mango" , "Cherry", "Papaya" ,"none of these!" 4
]

 levels = [1000, 2000, 3000, 4000, 5000, 6000, 8000, 10000, ]

for i in range(0, len(q)):
    question = q[i]
    print(f"Question for Rs.{level[i]}")
    print(f"a. {q[1]}       b.{q[2]}")
    print(f"c. {q[3]}       d.{q[4]}")
    reply = int(input("Enter your answer (1-4) "))
    if (reply == q[-1]):
        print(f"Correct answer, you have won {levels[i]}")
        if()
    else:
        print("Wrong Answer")