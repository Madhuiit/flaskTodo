document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', () => {
            const taskID = button.getAttribute('data-id');
            fetch(`/delete/${taskID}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to delete task');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    document.querySelector(`li[data-id="${taskID}"]`).remove();
                }
            })
            .catch(error => {
                alert('Error deleting task: ' + error.message);
            });
        });
    });
});