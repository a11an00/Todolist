const Taskinput= document.getElementById("task-input");
const addTaskBtn= document.getElementById("add-task-btn");
const taskList= document.getElementById("task-list");
const prioritySelect= document.getElementById("priority-select");
const statusSelect= document.getElementById("status-select");
const editBtn= document.getElementsByClassName("edit-btn");
const deleteBtn= document.getElementsByClassName("delete-btn");
let tasks = [];
addTaskBtn.addEventListener("click", addTask);
function addTask() {   
     const taskText = Taskinput.value.trim();
    const priority = prioritySelect.value;
    if (taskText === "") {
        alert("Please enter a task.");
        return;
    }
    const task = {
        id: Date.now(),
        text: taskText,
        priority: priority,
        status: "pending"

    };
    tasks.push(task);
    Taskinput.value = "";
    prioritySelect.value = "low";
    displayTasks();
}
function displayTasks() {
    taskList.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `
            <span class="task-text">${task.text}</span>
            <span class="priority ${task.priority}">${task.priority}</span>
            <div>
                <button class="edit-btn" onclick="editTask(${task.id});changePriority(${task.id}, '${task.priority}')">Edit</button>
                <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
                <select id="status-select" class="status-select" onchange="updateStatus(${task.id}, this.value)">
                    <option value="pending" ${task.status === "pending" ? "selected" : ""}>Pending</option>
                    <option value="completed" ${task.status === "completed" ? "selected" : ""}>Completed</option>
                </select>
            </div>
        `;
        taskList.appendChild(li);

    });
}
editBtn.addEventListener("click", function() {
    const id = parseInt(this.parentElement.parentElement.getAttribute("data-id"));
    editTask(id);
});
function editTask(id) {
    const task = tasks.find(t => t.id === id);
    const newText = prompt("Edit task:", task.text);
    if (newText !== null) {
        task.text = newText.trim();
        displayTasks();
    }

}
function deleteTask(id) {
    tasks = tasks.filter(t => t.id !== id);
    displayTasks();
}
function updateStatus(id, status) {
    const task = tasks.find(t => t.id === id);
    task.status = status;
    displayTasks();
}
function changePriority(id, priority) {
    const task = tasks.find(t => t.id === id);
    task.priority = prompt("Change priority (low, medium, high):", task.priority);

    displayTasks();
}