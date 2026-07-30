const base_url = '';

function sendEvent() {
	//
}

function createUser() {
	//
}

function loadItems() {
	//
}

document.addEventListener('DOMContentLoaded', () => {
	const card = document.getElementById('card');

	if (card) {
		card.addEventListener('click', () => {
			// 1. Set localStorage
			localStorage.setItem('selectedPerson', 'Ana García');
			alert('')

			// 2. Open Modal
			const modalElement = document.getElementById('myModal');
			const modalInstance = new bootstrap.Modal(modalElement);
			modalInstance.show();
		});
	}
});
