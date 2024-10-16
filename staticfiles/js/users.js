

document.getElementById('add-user-btn').onclick = function() {
    document.getElementById('add-user-modal').style.display = 'block';
};

document.getElementById('close-modal').onclick = function() {
    document.getElementById('add-user-modal').style.display = 'none';
};

document.getElementById('add-user-form').onsubmit = function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '{% url "add_user" %}', true);

    xhr.onload = function() {
        if (xhr.status === 200) {
            const newUser = JSON.parse(xhr.responseText);
            const userList = document.getElementById('user-list').querySelector('tbody');
            const newRow = document.createElement('tr');
            newRow.id = 'user-' + newUser.id;
            newRow.innerHTML = `
                <td>${newUser.username}</td>
                <td>${newUser.email}</td>
                <td>${newUser.is_active ? 'Active' : 'Inactive'}</td>
                <td><button class="remove-btn" data-id="${newUser.id}">✖</button></td>
            `;
            userList.appendChild(newRow);
            document.getElementById('result-message').innerText = 'New user added';
            document.getElementById('add-user-modal').style.display = 'none';
            this.reset(); // Reset the form
        } else {
            document.getElementById('result-message').innerText = 'Error adding user.';
        }
    };

    xhr.send(formData);
};

document.querySelectorAll('.remove-btn').forEach(button => {
    button.onclick = function() {
        const userId = this.getAttribute('data-id');
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '{% url "remove_user" %}', true);
        xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}'); // Send CSRF token
        xhr.setRequestHeader('Content-Type', 'application/json');

        xhr.onload = function() {
            if (xhr.status === 200) {
                document.getElementById('user-' + userId).remove();
                document.getElementById('result-message').innerText = 'User removed successfully';
            } else {
                document.getElementById('result-message').innerText = 'Error removing user.';
            }
        };

        xhr.send(JSON.stringify({ id: userId }));
    };
});
