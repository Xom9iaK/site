document.addEventListener('DOMContentLoaded', function () {
	const contents = document.querySelectorAll('.vacancy-content')
	contents.forEach(content => {
		content.style.display = 'none'
	})
})

function toggleVacancy(contentId) {
	const content = document.getElementById(contentId)
	const icon = event.currentTarget.querySelector('.toggle-icon')

	if (content.style.display === 'none') {
		content.style.display = 'block'
		icon.textContent = '▲'
	} else {
		content.style.display = 'none'
		icon.textContent = '▼'
	}
}

function toggleApplicationForm(formId) {
	const form = document.getElementById(formId)
	if (form.style.display === 'none') {
		form.style.display = 'block'
	} else {
		form.style.display = 'none'
	}
}

document.addEventListener('DOMContentLoaded', function () {
	const contents = document.querySelectorAll('.vacancy-content')
	contents.forEach(content => {
		content.style.display = 'none'
	})
})



