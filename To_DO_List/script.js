document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const taskInput = document.getElementById('task-input');
    const prioritySelect = document.getElementById('priority-select');
    const addTaskBtn = document.getElementById('add-task-btn');
    const taskList = document.getElementById('task-list');
    const emptyState = document.getElementById('empty-state');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const totalTasksEl = document.getElementById('total-tasks');
    const completedTasksEl = document.getElementById('completed-tasks');
    const activeTasksEl = document.getElementById('active-tasks');
    const editModal = document.getElementById('edit-modal');
    const closeModalBtn = document.getElementById('close-modal');
    const cancelEditBtn = document.getElementById('cancel-edit');
    const editForm = document.getElementById('edit-form');
    const editTaskId = document.getElementById('edit-task-id');
    const editTaskTitle = document.getElementById('edit-task-title');
    const editTaskPriority = document.getElementById('edit-task-priority');
    const editTaskCompleted = document.getElementById('edit-task-completed');
    const successAlert = document.getElementById('success-alert');
    const errorAlert = document.getElementById('error-alert');

    // Tasks array
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    let currentFilter = 'all';

    // Initialize
    renderTasks();
    updateStats();

    // Add task event
    addTaskBtn.addEventListener('click', addTask);

    // Handle enter key in input
    taskInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            addTask();
        }
    });

    // Filter events
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentFilter = this.dataset.filter;
            renderTasks();
        });
    });

    // Modal events
    closeModalBtn.addEventListener('click', closeModal);
    cancelEditBtn.addEventListener('click', closeModal);
    editForm.addEventListener('submit', saveEditedTask);

    // Add task function
    function addTask() {
        const title = taskInput.value.trim();
        const priority = prioritySelect.value;

        if (title === '') {
            showAlert('Please enter a task', 'error');
            return;
        }

        const newTask = {
            id: Date.now(),
            title,
            priority,
            completed: false,
            createdAt: new Date().toISOString()
        };

        tasks.push(newTask);
        saveTasks();
        taskInput.value = '';
        renderTasks();
        updateStats();
        showAlert('Task added successfully', 'success');
    }

    // Render tasks function
    function renderTasks() {
        let filteredTasks = tasks;

        // Apply filters
        if (currentFilter === 'active') {
            filteredTasks = tasks.filter(task => !task.completed);
        } else if (currentFilter === 'completed') {
            filteredTasks = tasks.filter(task => task.completed);
        } else if (['high', 'medium', 'low'].includes(currentFilter)) {
            filteredTasks = tasks.filter(task => task.priority === currentFilter);
        }

        if (filteredTasks.length === 0) {
            taskList.innerHTML = '';
            emptyState.style.display = 'block';
            if (currentFilter !== 'all' && tasks.length > 0) {
                emptyState.innerHTML = `
                    <i>🔍</i>
                    <h3>No ${currentFilter} tasks found</h3>
                    <p>Try a different filter</p>
                `;
            } else {
                emptyState.innerHTML = `
                    <i>📝</i>
                    <h3>No tasks yet</h3>
                    <p>Add a new task to get started</p>
                `;
            }
            return;
        }

        emptyState.style.display = 'none';
        taskList.innerHTML = '';

        filteredTasks.forEach(task => {
            const li = document.createElement('li');
            li.className = `task-item ${task.priority}-priority ${task.completed ? 'completed' : ''}`;
            li.dataset.id = task.id;

            // Format date
            const date = new Date(task.createdAt);
            const formattedDate = date.toLocaleDateString('en-US', {
                month: 'short',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            });

            li.innerHTML = `
                <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''}>
                <div class="task-content">
                    <div class="task-title">${task.title}</div>
                    <div class="task-info">
                        <span class="priority-badge">${task.priority.charAt(0).toUpperCase() + task.priority.slice(1)}</span>
                        <span class="task-date">${formattedDate}</span>
                    </div>
                </div>
                <div class="task-actions">
                    <button class="action-btn edit-btn">✏️</button>
                    <button class="action-btn delete-btn">🗑️</button>
                </div>
            `;

            // Add checkbox event
            const checkbox = li.querySelector('.task-checkbox');
            checkbox.addEventListener('change', function() {
                toggleTaskStatus(task.id);
            });

            // Add edit button event
            const editBtn = li.querySelector('.edit-btn');
            editBtn.addEventListener('click', function() {
                openEditModal(task);
            });

            // Add delete button event
            const deleteBtn = li.querySelector('.delete-btn');
            deleteBtn.addEventListener('click', function() {
                deleteTask(task.id);
            });

            taskList.appendChild(li);
        });
    }

    // Toggle task status
    function toggleTaskStatus(id) {
        const task = tasks.find(t => t.id === id);
        if (task) {
            task.completed = !task.completed;
            saveTasks();
            renderTasks();
            updateStats();
            showAlert(`Task marked as ${task.completed ? 'completed' : 'active'}`, 'success');
        }
    }

    // Delete task
    function deleteTask(id) {
        tasks = tasks.filter(task => task.id !== id);
        saveTasks();
        renderTasks();
        updateStats();
        showAlert('Task deleted successfully', 'success');
    }

    // Open edit modal
    function openEditModal(task) {
        editTaskId.value = task.id;
        editTaskTitle.value = task.title;
        editTaskPriority.value = task.priority;
        editTaskCompleted.value = task.completed.toString();
        editModal.style.display = 'flex';
    }

    // Close modal
    function closeModal() {
        editModal.style.display = 'none';
    }

    // Save edited task
    function saveEditedTask(e) {
        e.preventDefault();
        const id = parseInt(editTaskId.value);
        const task = tasks.find(t => t.id === id);

        if (task) {
            task.title = editTaskTitle.value.trim();
            task.priority = editTaskPriority.value;
            task.completed = editTaskCompleted.value === 'true';
            saveTasks();
            renderTasks();
            updateStats();
            closeModal();
            showAlert('Task updated successfully', 'success');
        }
    }

    // Update stats
    function updateStats() {
        const total = tasks.length;
        const completed = tasks.filter(task => task.completed).length;
        const active = total - completed;

        totalTasksEl.textContent = total;
        completedTasksEl.textContent = completed;
        activeTasksEl.textContent = active;
    }

    // Save tasks to local storage
    function saveTasks() {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    // Show alert
    function showAlert(message, type) {
        const alert = type === 'success' ? successAlert : errorAlert;
        alert.textContent = message;
        alert.style.display = 'block';

        setTimeout(() => {
            alert.style.display = 'none';
        }, 3000);
    }

    // Close modal when clicking outside
    window.addEventListener('click', function(e) {
        if (e.target === editModal) {
            closeModal();
        }
    });
});