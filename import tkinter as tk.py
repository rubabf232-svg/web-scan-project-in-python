import tkinter as tk
import requests

def scan():
    url = entry.get()
    result.delete(1.0, tk.END)

    try:
        r = requests.get(url, timeout=5)

        result.insert(tk.END, "Status Code: ")
        result.insert(tk.END, str(r.status_code) + "\n\n")

        # HTTPS check
        if url.startswith("https"):
            result.insert(tk.END, "HTTPS: Enabled\n")
        else:
            result.insert(tk.END, "HTTPS: Not Enabled\n")

        headers = r.headers

        result.insert(tk.END, "\nSecurity Headers:\n")

        if "X-Frame-Options" in headers:
            result.insert(tk.END, "X-Frame-Options: OK\n")
        else:
            result.insert(tk.END, "X-Frame-Options: Missing\n")

        if "Content-Security-Policy" in headers:
            result.insert(tk.END, "CSP: OK\n")
        else:
            result.insert(tk.END, "CSP: Missing\n")

    except:
        result.insert(tk.END, "Website not reachable")

# GUI window
window = tk.Tk()
window.title("Easy Web Scanner")
window.geometry("400x300")

tk.Label(window, text="Enter Website URL").pack()

entry = tk.Entry(window, width=40)
entry.pack(pady=5)

tk.Button(window, text="Scan Website", command=scan).pack(pady=5)

result = tk.Text(window, height=10, width=45)
result.pack()

window.mainloop()
