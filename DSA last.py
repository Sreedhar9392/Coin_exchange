import tkinter as tk

def coin_change(coins, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for coin in coins:
        for i in range(coin, target + 1):
            for way in dp[i - coin]:
                dp[i].append(way + [coin])

    return dp[target]

def solve_coin_change():
    target = int(target_entry.get())
    coin_values = [int(x) for x in coins_entry.get().split()]
    ways = coin_change(coin_values, target)
    
    result_label.config(text=f"Number of ways to make change: {len(ways)}")
    
    ways_text.delete(1.0, tk.END)
    for way in ways:
        ways_text.insert(tk.END, ', '.join([str(coin) for coin in way]) + '\n')

# Create the main window
window = tk.Tk()
window.title("Coin Change Problem Solver")

# Create input fields and labels
tk.Label(window, text="Enter target amount:").pack()
target_entry = tk.Entry(window)
target_entry.pack()

tk.Label(window, text="Enter coin denominations (space-separated):").pack()
coins_entry = tk.Entry(window)
coins_entry.pack()

# Create a button to solve the problem
solve_button = tk.Button(window, text="Solve", command=solve_coin_change)
solve_button.pack()

# Create a label to display the number of ways
result_label = tk.Label(window, text="")
result_label.pack()

# Create a text widget to display the ways
ways_text = tk.Text(window, height=10, width=30)
ways_text.pack()

# Start the Tkinter main loop
window.mainloop()
