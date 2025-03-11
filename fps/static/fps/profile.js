document.addEventListener('DOMContentLoaded', function () {
	// Add hover class to all buttons
	const buttons = document.querySelectorAll('.btn')

	buttons.forEach(button => {
		button.addEventListener('mouseenter', function () {
			this.classList.add('btn-hover')
		})

		button.addEventListener('mouseleave', function () {
			this.classList.remove('btn-hover')
		})
	})
})
function showEditForm() {
	document.getElementById('editForm').style.display = 'block'
}

function hideEditForm() {
	document.getElementById('editForm').style.display = 'none'
}

function showReviewForm(applicationId) {
	document.getElementById(`review-form-${applicationId}`).style.display =
		'block'
}

function hideReviewForm(applicationId) {
	document.getElementById(`review-form-${applicationId}`).style.display = 'none'
}

function showEditReview(reviewId) {
	document.getElementById(`edit-review-${reviewId}`).style.display = 'block'
}

function hideEditReview(reviewId) {
	document.getElementById(`edit-review-${reviewId}`).style.display = 'none'
}