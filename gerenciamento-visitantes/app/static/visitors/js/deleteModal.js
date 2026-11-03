const deleteModal = document.getElementById('delete-modal');
const deleteForm = document.getElementById('delete-form');
deleteModal.addEventListener('show.bs.modal', function(event) {
    const deleteButton = event.relatedTarget;
    const visitorName = deleteButton.getAttribute('data-visitor-name');
    const visitorId = deleteButton.getAttribute('data-visitor-id');
    document.getElementById('visitor-name').textContent = visitorName;

    deleteForm.action = `./delete/${visitorId}/`
});
