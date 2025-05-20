# 🗳️ Simple Python Voting System

This is a basic command-line voting system implemented in Python. The program allows a predefined list of voters to vote for two candidates. It keeps track of votes, prevents double voting, and displays the election result once all votes are cast.

---

## 📌 Features

* Supports voting between **two user-defined candidates**.
* Prevents **duplicate voting** by tracking voter IDs.
* Displays the **number of eligible voters**.
* Announces the **winner** after all votes are submitted.
* Handles **tie situations**.
* Includes an example of basic array manipulation (for learning/demo purposes).

---

## 🚀 How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the Script:**

   You need Python installed on your system.

   ```bash
   python voting_system.py
   ```

3. **Input:**

   * Enter the names of two candidates.
   * Enter voter IDs from the predefined list to vote.
   * Voters can vote by choosing `1` or `2` corresponding to candidates.
   * Repeated voting attempts are denied.
   * Voting ends when all registered voters have cast their votes.

---

## 🧑‍💻 Example

```bash
Please Enter 1st Candidate Name: Alice
Please Enter 2nd Candidate Name: Bob
Number of Voters:  8

Please Enter your Id: 101
Alice
Bob
Enter your choice: 1
You voted Alice

...

Voting is Over 🎉🎉🎉🥳🥳🥳
Alice  Won Election with the votes: 5 🏆
```

---

## 📚 Code Structure

* **Candidate Setup:** Accepts names of candidates.
* **Voter Authentication:** Validates voter ID and ensures no double voting.
* **Voting Process:** Accepts vote input and tallies results.
* **Result Declaration:** Displays winner or tie.
* **Bonus Code:** Demonstrates basic array usage from Python's `array` module.

---

## 📝 Notes

* You can expand the voters list or make it dynamic for more realistic simulations.
* To support more than two candidates, additional logic will be needed.
* Consider using a dictionary to map votes to candidates for scalability.

---

## 🛠️ Requirements

* Python 3.x

No external libraries are required.

---
