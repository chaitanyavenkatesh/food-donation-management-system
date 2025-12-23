import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import date

# Database connection function (exception handling added)
def get_db_connection():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="chai",
            database="food_donation",
            port=3306
        )
        return db
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
        return None


db = get_db_connection()
cursor = db.cursor() if db else None


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Donation Login")
        # Make login window full screen
        self.root.state("zoomed")
        self.root.config(bg="#101F26")

        # Center container frame
        container = tk.Frame(self.root, bg="#101F26")
        container.place(relx=0.5, rely=0.5, anchor="center")

        self.icon_label = tk.Label(
            container,
            text="🍛",
            font=("Arial", 60),
            bg="#101F26",
            fg="white"
        )
        self.icon_label.grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(
            container,
            text="Username",
            bg="#101F26",
            fg="white",
            font=("Arial", 12)
        ).grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.username_entry = tk.Entry(container, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(
            container,
            text="Password",
            bg="#101F26",
            fg="white",
            font=("Arial", 12)
        ).grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.password_entry = tk.Entry(container, font=("Arial", 12), show="*")
        self.password_entry.grid(row=2, column=1, pady=5, padx=10)

        self.login_btn = tk.Button(
            container,
            text="Login",
            bg="white",
            fg="#101F26",
            font=("Arial", 12, "bold"),
            command=self.check_login
        )
        self.login_btn.grid(row=3, column=0, columnspan=2, pady=20)

        # Center grid columns inside container
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        self.root.bind('<Return>', lambda event: self.check_login())

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login Success", "Welcome, admin!")
            self.root.destroy()
            dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")


class FoodDonationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Donation Management System")
        self.root.state("zoomed")
        self.root.config(bg="#101F26")

        # ====== NAVBAR / HEADER (CENTERED + FOOD LOGO) ======
        header_frame = tk.Frame(self.root, bg="#101F26")
        header_frame.pack(pady=(10, 0))   # remove fill="x"


        inner_header = tk.Frame(header_frame, bg="#101F26")
        inner_header.pack()  # this centers it horizontally

        logo_label = tk.Label(inner_header, text="🍲", font=("Arial", 40, "bold"), bg="#101F26", fg="white")
        logo_label.pack()

        welcome_label = tk.Label(
            inner_header,
            text="Welcome",
            font=("Arial", 24, "bold"),
            bg="#101F26",
            fg="white"
        )
        welcome_label.pack()

        title_label = tk.Label(
            inner_header,
            text="Food Donation Management System",
            font=("Arial", 20, "bold"),
            bg="#101F26",
            fg="white"
        )
        title_label.pack()

        # ====== NOTEBOOK (TABS CENTERED IN THE WINDOW) ======
        notebook_outer = tk.Frame(self.root, bg="#101F26")
        notebook_outer.pack(expand=True, fill="both", padx=50, pady=20)

        notebook = ttk.Notebook(notebook_outer)
        notebook.pack(expand=True, fill="both")

        # Donor Tab
        donor_frame = tk.Frame(notebook, bg="white")
        notebook.add(donor_frame, text="Donors")
        self.build_donor_tab(donor_frame)

        # Food Tab
        food_frame = tk.Frame(notebook, bg="white")
        notebook.add(food_frame, text="Food")
        self.build_food_tab(food_frame)

        # NGO Tab
        ngo_frame = tk.Frame(notebook, bg="white")
        notebook.add(ngo_frame, text="NGOs")
        self.build_ngo_tab(ngo_frame)

        # Distribution Tab
        dist_frame = tk.Frame(notebook, bg="white")
        notebook.add(dist_frame, text="Distribution")
        self.build_distribution_tab(dist_frame)

        # Dashboard stats
        stats_frame = tk.Frame(self.root, bg="#101F26")
        stats_frame.pack(fill="x", padx=50, pady=10)
        self.stats_label = tk.Label(
            stats_frame, text="", font=("Arial", 14),
            bg="#101F26", fg="white"
        )
        self.stats_label.pack()
        self.update_stats()

    # Dash Stats
    def update_stats(self):
        if not cursor:
            self.stats_label.config(text="Stats unavailable: No DB connection")
            return
        try:
            cursor.execute("SELECT COUNT(*) FROM Donors")
            donors = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Food")
            foods = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM NGOs")
            ngos = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM Distribution")
            distributed = cursor.fetchone()[0]
            stats = f"Donors: {donors} | Foods: {foods} | NGOs: {ngos} | Distributed: {distributed}"
            self.stats_label.config(text=stats)
        except Exception as e:
            self.stats_label.config(text=f"Stats unavailable: {e}")

    # ================== DONOR TAB ==================
    def build_donor_tab(self, frame):
        # Center form using inner frame
        form_frame = tk.Frame(frame, bg="white")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Name", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.donor_name = tk.Entry(form_frame)
        self.donor_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Phone", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.donor_phone = tk.Entry(form_frame)
        self.donor_phone.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Location", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.donor_location = tk.Entry(form_frame)
        self.donor_location.grid(row=2, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Add Donor", command=self.add_donor).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Donor", command=self.delete_donor).pack(side="left", padx=5)

        # Table centered with pack
        self.donor_table = ttk.Treeview(
            frame,
            columns=("ID", "Name", "Phone", "Location"),
            show="headings"
        )
        for col in ("ID", "Name", "Phone", "Location"):
            self.donor_table.heading(col, text=col)
            self.donor_table.column(col, width=120, anchor="center")
        self.donor_table.pack(pady=10, expand=True, fill="both")
        self.load_donors()

    # ================== FOOD TAB ==================
    def build_food_tab(self, frame):
        form_frame = tk.Frame(frame, bg="white")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="Donor ID", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.food_donor = tk.Entry(form_frame)
        self.food_donor.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Food Type", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.food_type = tk.Entry(form_frame)
        self.food_type.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Quantity", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.food_qty = tk.Entry(form_frame)
        self.food_qty.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Expiry Date (YYYY-MM-DD)", bg="white").grid(
            row=3, column=0, padx=10, pady=5, sticky="e"
        )
        self.food_exp = tk.Entry(form_frame)
        self.food_exp.grid(row=3, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Add Food", command=self.add_food).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Food", command=self.delete_food).pack(side="left", padx=5)

        self.food_table = ttk.Treeview(
            frame,
            columns=("ID", "DonorID", "Type", "Qty", "Expiry", "Status"),
            show="headings"
        )
        for col in ("ID", "DonorID", "Type", "Qty", "Expiry", "Status"):
            self.food_table.heading(col, text=col)
            self.food_table.column(col, width=120, anchor="center")
        self.food_table.pack(pady=10, expand=True, fill="both")
        self.load_food()

    # ================== NGO TAB ==================
    def build_ngo_tab(self, frame):
        form_frame = tk.Frame(frame, bg="white")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="NGO Name", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.ngo_name = tk.Entry(form_frame)
        self.ngo_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Contact", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.ngo_contact = tk.Entry(form_frame)
        self.ngo_contact.grid(row=1, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Add NGO", command=self.add_ngo).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete NGO", command=self.delete_ngo).pack(side="left", padx=5)

        self.ngo_table = ttk.Treeview(
            frame,
            columns=("ID", "Name", "Contact"),
            show="headings"
        )
        for col in ("ID", "Name", "Contact"):
            self.ngo_table.heading(col, text=col)
            self.ngo_table.column(col, width=120, anchor="center")
        self.ngo_table.pack(pady=10, expand=True, fill="both")
        self.load_ngos()

    # ================== DISTRIBUTION TAB ==================
    def build_distribution_tab(self, frame):
        form_frame = tk.Frame(frame, bg="white")
        form_frame.pack(pady=20)

        tk.Label(form_frame, text="NGO ID", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.dist_ngo_id = tk.Entry(form_frame)
        self.dist_ngo_id.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Food ID", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.dist_food_id = tk.Entry(form_frame)
        self.dist_food_id.grid(row=1, column=1, padx=10, pady=5)

        btn_frame = tk.Frame(form_frame, bg="white")
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Distribute", command=self.add_distribution).pack()

        self.dist_table = ttk.Treeview(
            frame,
            columns=("ID", "NGO", "Food", "Date"),
            show="headings"
        )
        for col in ("ID", "NGO", "Food", "Date"):
            self.dist_table.heading(col, text=col)
            self.dist_table.column(col, width=120, anchor="center")
        self.dist_table.pack(pady=10, expand=True, fill="both")
        self.load_distribution()

    # -------- Donor CRUD --------
    def add_donor(self):
        if not cursor:
            messagebox.showerror("Error", "No database connection")
            return
        name = self.donor_name.get()
        phone = self.donor_phone.get()
        location = self.donor_location.get()
        if not name or not phone or not location:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            cursor.execute(
                "INSERT INTO Donors (name, phone, location) VALUES (%s,%s,%s)",
                (name, phone, location)
            )
            db.commit()
            self.load_donors()
            self.update_stats()
            messagebox.showinfo("Success", "Donor added successfully")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete_donor(self):
        if not cursor:
            messagebox.showerror("Error", "No database connection")
            return
        selected = self.donor_table.selection()
        if not selected:
            messagebox.showerror("Error", "Select a donor to delete")
            return
        donor_id = self.donor_table.item(selected[0])["values"][0]
        try:
            cursor.execute("DELETE FROM Donors WHERE donor_id=%s", (donor_id,))
            db.commit()
            self.load_donors()
            self.update_stats()
            messagebox.showinfo("Deleted", "Donor deleted successfully")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def load_donors(self):
        if not cursor:
            return
        for item in self.donor_table.get_children():
            self.donor_table.delete(item)
        cursor.execute("SELECT * FROM Donors")
        for row in cursor.fetchall():
            self.donor_table.insert("", tk.END, values=row)

    # -------- Food CRUD --------
    def add_food(self):
        if not cursor:
            messagebox.showerror("Error", "No database connection")
            return
        donor_id = self.food_donor.get()
        ftype = self.food_type.get()
        qty = self.food_qty.get()
        exp = self.food_exp.get()
        if not donor_id or not ftype or not qty or not exp:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            cursor.execute(
                "INSERT INTO Food (donor_id, food_type, quantity, expiry_date) VALUES (%s,%s,%s,%s)",
                (donor_id, ftype, qty, exp)
            )
            db.commit()
            self.load_food()
            self.update_stats()
            messagebox.showinfo("Success", "Food added successfully")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete_food(self):
        if not cursor:
            messagebox.showerror("Error", "No database connection")
            return
        selected = self.food_table.selection()
        if not selected:
            messagebox.showerror("Error", "Select a food item to delete")
            return
        food_id = self.food_table.item(selected[0])["values"][0]
        try:
            cursor.execute("DELETE FROM Food WHERE food_id=%s", (food_id,))
            db.commit()
            self.load_food()
            self.update_stats()
            messagebox.showinfo("Deleted", "Food item deleted successfully")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def load_food(self):
        if not cursor:
            return
        for item in self.food_table.get_children():
            self.food_table.delete(item)
        cursor.execute("SELECT * FROM Food")
        for row in cursor.fetchall():
            self.food_table.insert("", tk.END, values=row)

    # -------- NGO CRUD --------
    def add_ngo(self):
        if not cursor:
            messagebox.showerror("Error", "No database connection")
            return
        name = self.ngo_name.get()
        contact = self.ngo_contact.get()
        if not name or not contact:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            cursor.execute("INSERT INTO NGOs (name, contact) VALUES (%s,%s)", (name, contact))
            db.commit()
            self.load_ngos()
            self.update_stats()
            messagebox.showinfo("Success", "NGO added successfully")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete_ngo(self):
        if not cursor:
            messagebox.showerror("Error", "No database connection")
            return
        selected = self.ngo_table.selection()
        if not selected:
            messagebox.showerror("Error", "Select NGO to delete")
            return
        ngo_id = self.ngo_table.item(selected[0])["values"][0]
        try:
            cursor.execute("DELETE FROM NGOs WHERE ngo_id=%s", (ngo_id,))
            db.commit()
            self.load_ngos()
            self.update_stats()
            messagebox.showinfo("Deleted", "NGO deleted successfully")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def load_ngos(self):
        if not cursor:
            return
        for item in self.ngo_table.get_children():
            self.ngo_table.delete(item)
        cursor.execute("SELECT * FROM NGOs")
        for row in cursor.fetchall():
            self.ngo_table.insert("", tk.END, values=row)

    # -------- Distribution CRUD --------
    def add_distribution(self):
        if not cursor:
            messagebox.showerror("Error", "No database connection")
            return
        ngo_id = self.dist_ngo_id.get()
        food_id = self.dist_food_id.get()
        if not ngo_id or not food_id:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            cursor.execute(
                "INSERT INTO Distribution (ngo_id, food_id, distribution_date) VALUES (%s,%s,%s)",
                (ngo_id, food_id, date.today())
            )
            cursor.execute("UPDATE Food SET status='Distributed' WHERE food_id=%s", (food_id,))
            db.commit()
            self.load_distribution()
            self.load_food()
            self.update_stats()
            messagebox.showinfo("Success", "Distribution recorded successfully")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def load_distribution(self):
        if not cursor:
            return
        for item in self.dist_table.get_children():
            self.dist_table.delete(item)
        cursor.execute("""
            SELECT d.distribution_id, n.name, f.food_type, d.distribution_date
            FROM Distribution d
            JOIN NGOs n ON d.ngo_id = n.ngo_id
            JOIN Food f ON d.food_id = f.food_id
        """)
        for row in cursor.fetchall():
            self.dist_table.insert("", tk.END, values=row)


def dashboard():
    root = tk.Tk()
    app = FoodDonationApp(root)
    root.mainloop()


if __name__ == "__main__":
    login_root = tk.Tk()
    LoginWindow(login_root)
    login_root.mainloop()
