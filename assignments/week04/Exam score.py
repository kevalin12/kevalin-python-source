PASS_SCORE = 50
NUM_STUDENTS = 5


def main():
   scores = []

   
   for i in range(1, NUM_STUDENTS + 1):
       score = float(input(f"Enter score of student {i}: "))
       scores.append(score)

   print()  

  
   for i, score in enumerate(scores, start=1):
       
       if score >= PASS_SCORE:
           result = "ผ่าน"
       else:
           result = "ไม่ผ่าน"

       
       if score.is_integer():
           score_display = int(score)
       else:
           score_display = score

       print(f"Student {i}: {score_display} -> {result}")


if __name__ == "__main__":
    main()