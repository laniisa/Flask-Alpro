from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data tugas (list of dictionaries)
tasks = [
    {"id": 1, "title": "Belajar Flask", "description": "Pelajari cara membuat aplikasi web dengan Flask.", "status": "Pending"},
    {"id": 2, "title": "Olahraga", "description": "Lakukan jogging pagi selama 30 menit.", "status": "Completed"},
]
# Data profil pengguna
profile = {
    "name": "Solani",
    "email": "solani@example.com",
    "bio": "Saya seorang pengembang web yang antusias belajar Flask.",
    "tasks_completed": 2
}

# Fungsi untuk menambahkan tugas baru
def add_new_task(title, description):
    return {"id": len(tasks) + 1, "title": title, "description": description, "status": "Pending"}

# Fungsi untuk memperbarui status tugas menjadi "Completed"
def mark_task_completed(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        task["status"] = "Completed"

# Prosedur untuk menampilkan tugas dengan status Completed
def show_completed_tasks():
    completed_tasks = [task for task in tasks if task["status"] == "Completed"]
    return completed_tasks

# Route Halaman Utama (Dashboard)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')  # Menampilkan halaman dashboard pertama kali

# Route Halaman Daftar Tugas
@app.route('/tasks')
def index():
<<<<<<< HEAD
    query = request.args.get('query')  
    sort_by = request.args.get('sort')
    status_filter = request.args.get('status')
    filtered_tasks = tasks  
=======
    return render_template('welcome.html', profile=profile)

@app.route('/task', methods=['GET', 'POST'])
def task():
    query = request.args.get('query')  # Menangkap query pencarian
    sort_by = request.args.get('sort')  # Menangkap parameter untuk pengurutan
    status_filter = request.args.get('status')  # Menangkap filter status
    filtered_tasks = tasks  # Default, jika tidak ada pencarian
>>>>>>> ca7e7be002589c10ce4297cc3b6617caa0c89de7

    if query:
        filtered_tasks = [task for task in tasks if query.lower() in task["title"].lower() or query.lower() in task["description"].lower()]
    
    if status_filter:
        filtered_tasks = [task for task in filtered_tasks if task["status"] == status_filter]
    
    if sort_by == 'title':
        filtered_tasks.sort(key=lambda x: x["title"].lower())
    elif sort_by == 'status':
        filtered_tasks.sort(key=lambda x: x["status"].lower())

    return render_template('task.html', tasks=filtered_tasks)

# Route Tambah Tugas
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_task = add_new_task(title, description)
        tasks.append(new_task)
        return redirect(url_for('task'))
    return render_template('add_task.html')

# Route Detail Tugas
@app.route('/task/<int:task_id>')
def task_detail(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return "Tugas tidak ditemukan", 404
    return render_template('task_detail.html', task=task)

# Route Tandai Tugas Selesai
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
<<<<<<< HEAD
        mark_task_completed(task_id)
    return redirect(url_for('index'))
=======
        mark_task_completed(task_id)  # Memanggil fungsi untuk menandai tugas selesai
    return redirect(url_for('task'))
>>>>>>> ca7e7be002589c10ce4297cc3b6617caa0c89de7

# Route Hapus Tugas
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for('task'))

# Algoritma Bubble Sort untuk mengurutkan tugas berdasarkan judul
def bubble_sort(tasks):
    n = len(tasks)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tasks[j]["title"] > tasks[j + 1]["title"]:
                tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]  # Menukar posisi tugas


# Route untuk halaman profil
@app.route('/profile')
def profile_page():
    return render_template('profile.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
